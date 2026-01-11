import numpy as np
import warnings
from .result import Result, TrainingSetValidationResult

warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")
from sklearn.preprocessing import MinMaxScaler
from sklearn.gaussian_process.kernels import RBF, WhiteKernel, ConstantKernel
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.model_selection import LeaveOneOut

from data.models import Unit


def unit_to_cost(unit: Unit) -> int:
    return unit.single_unit_cost


# GPRTrainer class encapsulating training, validation, and prediction
class GPRTrainer:
    def __init__(self, mapper=None):
        self.scaler = MinMaxScaler()
        self.gpr = None
        self.X = None
        self.y = None
        self.units = None
        self.mapper = mapper

    def train(self, units: list[Unit]):
        self.units = units
        unit_vectors = np.array([self.mapper(unit) for unit in units])
        self.X = self.scaler.fit_transform(unit_vectors)
        self.y = np.array([unit_to_cost(unit) for unit in units])

        kernel = ConstantKernel(1.0, (1e-2, 1e2)) * RBF(
            length_scale=1.0, length_scale_bounds=(1e-2, 1e2)
        ) + WhiteKernel(noise_level=1.0, noise_level_bounds=(1e-3, 1e1))

        self.gpr = GaussianProcessRegressor(
            kernel=kernel,
            alpha=0.0,  # handled by WhiteKernel
            normalize_y=True,  # important for point costs
            n_restarts_optimizer=10,
            random_state=42,
        )
        self.gpr.fit(self.X, self.y)
        # print("Kernel after training:")
        # print(self.gpr.kernel_)
        # print("Small length scale → pricing is sensitive to small stat changes")
        # print("Large noise → game designers priced inconsistently")

    def validate(self) -> TrainingSetValidationResult:
        if self.gpr is None or self.X is None or self.y is None:
            raise RuntimeError("Model must be trained before validation.")
        loo = LeaveOneOut()
        results = TrainingSetValidationResult()
        for train_idx, test_idx in loo.split(self.X):
            self.gpr.fit(self.X[train_idx], self.y[train_idx])
            pred, std_dev = self.gpr.predict(self.X[test_idx], return_std=True)
            error = pred[0] - self.y[test_idx][0]
            unit = self.units[test_idx[0]]
            results.units.append((error, Result(unit, pred[0], std_dev[0])))
        return results

    def predict(self, unit: Unit) -> Result:
        if self.gpr is None or self.scaler is None:
            raise RuntimeError("Model must be trained before prediction.")
        new_unit_vector = np.array(self.mapper(unit))
        new_unit_vector_scaled = self.scaler.transform([new_unit_vector])
        mean_cost, std_dev = self.gpr.predict(new_unit_vector_scaled, return_std=True)
        return Result(unit, predicted_cost=mean_cost[0], uncertainty=std_dev[0])
