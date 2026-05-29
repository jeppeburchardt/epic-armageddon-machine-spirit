"""GPR trainer: fits a Gaussian Process Regressor and generates predictions."""

from __future__ import annotations

import logging
import warnings
from typing import Any, Callable

import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel, WhiteKernel
from sklearn.model_selection import LeaveOneOut
from sklearn.preprocessing import MinMaxScaler

from ea_unit_pricing.domain.result import Result, TrainingSetValidationResult
from ea_unit_pricing.domain.unit import Unit

__all__ = ["GPRTrainer"]

logger = logging.getLogger(__name__)


def _unit_to_cost(unit: Unit) -> float:
    return unit.single_unit_cost


class GPRTrainer:
    """Trains a GPR model on a list of units and predicts costs for new ones.

    Args:
        mapper: Callable that converts a ``Unit`` into a feature vector
            (``list[float]`` or ``np.ndarray``).
        random_state: Seed passed to ``GaussianProcessRegressor`` for
            reproducible results.  Defaults to ``42``.
    """

    def __init__(self, mapper: Callable[[Unit], Any] | None = None, random_state: int = 42) -> None:
        self.scaler: MinMaxScaler = MinMaxScaler()
        self.gpr: GaussianProcessRegressor | None = None
        self.X: np.ndarray[Any, np.dtype[Any]] | None = None
        self.y: np.ndarray[Any, np.dtype[Any]] | None = None
        self.units: list[Unit] | None = None
        self.mapper = mapper
        self.random_state = random_state

    def train(self, units: list[Unit]) -> None:
        """Fit the GPR model on *units* with known costs."""
        assert self.mapper is not None, "A mapper must be provided before training."
        self.units = units
        unit_vectors = np.array([self.mapper(unit) for unit in units])
        self.X = self.scaler.fit_transform(unit_vectors)
        self.y = np.array([_unit_to_cost(unit) for unit in units])

        kernel = ConstantKernel(1.0, (1e-2, 1e2)) * RBF(
            length_scale=1.0, length_scale_bounds=(1e-2, 1e2)
        ) + WhiteKernel(noise_level=1.0, noise_level_bounds=(1e-3, 1e1))
        self.gpr = GaussianProcessRegressor(
            kernel=kernel,
            alpha=0.0,
            normalize_y=True,
            n_restarts_optimizer=10,
            random_state=self.random_state,
        )
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")
            self.gpr.fit(self.X, self.y)
        logger.debug("Trained on %d units. Kernel: %s", len(units), self.gpr.kernel_)

    def validate(self) -> TrainingSetValidationResult:
        """Run leave-one-out cross-validation and return per-unit errors."""
        if self.gpr is None or self.X is None or self.y is None or self.units is None:
            raise RuntimeError("Model must be trained before validation.")
        loo = LeaveOneOut()
        results = TrainingSetValidationResult()
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")
            for train_idx, test_idx in loo.split(self.X):
                self.gpr.fit(self.X[train_idx], self.y[train_idx])
                pred, std_dev = self.gpr.predict(self.X[test_idx], return_std=True)
                error = float(pred[0] - self.y[test_idx][0])
                unit = self.units[test_idx[0]]
                results.units.append((error, Result(unit, float(pred[0]), float(std_dev[0]))))
        return results

    def predict(self, unit: Unit) -> Result:
        """Predict cost and uncertainty for a single unit."""
        assert self.mapper is not None, "A mapper must be provided before prediction."
        if (
            self.gpr is None
            or self.scaler is None
            or self.X is None
            or self.y is None
            or self.units is None
        ):
            raise RuntimeError("Model must be trained before prediction.")
        new_vector = np.array(self.mapper(unit))
        scaled = self.scaler.transform([new_vector])
        mean_cost, std_dev = self.gpr.predict(scaled, return_std=True)
        distances = np.linalg.norm(self.X - scaled[0], axis=1)
        nearest_indexes = np.argsort(distances)[:5]
        nearest_neighbours = [
            (self.units[int(i)].name, float(self.y[int(i)]), float(distances[int(i)]))
            for i in nearest_indexes
        ]
        return Result(
            unit,
            predicted_cost=float(mean_cost[0]),
            uncertainty=float(std_dev[0]),
            nearest_neighbours=nearest_neighbours,
            training_price_values=[float(v) for v in self.y.tolist()],
            model_kernel=str(self.gpr.kernel_),
            training_set_size=len(self.units),
        )
