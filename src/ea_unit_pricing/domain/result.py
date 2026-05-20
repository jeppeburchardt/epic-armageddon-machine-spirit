"""Prediction result types returned by the GPR trainer."""

from __future__ import annotations

import numpy as np

from ea_unit_pricing.domain.enums import Quality
from ea_unit_pricing.domain.unit import Unit

__all__ = [
    "MultipleChoiceResult",
    "Result",
    "TrainingSetValidationResult",
]


class Result:
    """Prediction for a single concrete unit (no weapon choices).

    ``quality`` and ``score`` are derived automatically from the uncertainty
    relative to the predicted cost.

    Attributes:
        unit: The unit that was predicted.
        predicted_cost: Mean cost predicted by the GPR model.
        uncertainty: One standard deviation returned by the model.
        score: Confidence score in the range 0–100 (higher = better).
        quality: Categorical quality bucket derived from *score*.
    """

    def __init__(self, unit: Unit, predicted_cost: float = 0, uncertainty: float = 0) -> None:
        self.unit = unit
        self.predicted_cost = predicted_cost
        self.uncertainty = uncertainty
        self.score = round((1 - (uncertainty / predicted_cost)) * 100) if predicted_cost else 0

        if self.score > 80 or self.uncertainty < 10:
            self.quality = Quality.SAFE
        elif self.score > 70 or self.uncertainty < 15:
            self.quality = Quality.REVIEW
        else:
            self.quality = Quality.EXPERIMENTAL


class MultipleChoiceResult:
    """Wraps predictions for all weapon-option variants of a unit.

    ``best_result`` holds the variant with the highest predicted cost and is
    used as the canonical answer.  ``spread`` is the relative difference
    between the most and least expensive variant::

        spread = (max_cost - min_cost) / max_cost

    A spread above 15 % is flagged via ``is_wide_spread``.  The properties
    ``unit``, ``predicted_cost``, ``uncertainty``, ``quality``, and ``score``
    delegate to ``best_result`` so this class can be used as a drop-in
    replacement for ``Result`` in most downstream code.  The ``unit``
    property returns the *original* unit (with ``MultipleChoiceWeapon`` slots
    intact) so that its base name is used in tables and JSON output.
    """

    SPREAD_THRESHOLD = 0.15

    def __init__(self, original_unit: Unit, results: list[Result]) -> None:
        self.original_unit = original_unit
        self.all_results = results
        self.best_result = max(results, key=lambda r: r.predicted_cost)
        min_cost = min(r.predicted_cost for r in results)
        max_cost = self.best_result.predicted_cost
        self.spread = (max_cost - min_cost) / max_cost if max_cost > 0 else 0.0

    @property
    def is_wide_spread(self) -> bool:
        return self.spread > self.SPREAD_THRESHOLD

    @property
    def unit(self) -> Unit:
        return self.original_unit

    @property
    def predicted_cost(self) -> float:
        return self.best_result.predicted_cost

    @property
    def uncertainty(self) -> float:
        return self.best_result.uncertainty

    @property
    def quality(self) -> Quality:
        return self.best_result.quality

    @property
    def score(self) -> float:
        return self.best_result.score


class TrainingSetValidationResult:
    """Aggregated leave-one-out validation errors for the training set."""

    def __init__(self) -> None:
        self.units: list[tuple[float, Result]] = []

    def get_errors(self) -> list[float]:
        return [r[0] for r in self.units]

    def get_mean_absolute_error(self) -> float:
        return float(np.mean(np.abs(self.get_errors())))

    def get_avg_absolute_error(self) -> float:
        return float(np.average(np.abs(self.get_errors())))
