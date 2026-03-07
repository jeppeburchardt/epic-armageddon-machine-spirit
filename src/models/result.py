import numpy as np
from models.units import Unit
from enum import Enum


class Quality(Enum):
    SAFE = 0
    REVIEW = 1
    EXPERIMENTAL = 2


def quality_to_str(quality: Quality):
    mapping = {
        Quality.SAFE: "Safe",
        Quality.REVIEW: "Review",
        Quality.EXPERIMENTAL: "Experimental",
    }
    return mapping.get(quality, str(quality))


class Result:
    unit: Unit
    predicted_cost: int
    uncertainty: float
    quality: Quality
    score: float

    def __init__(self, unit: Unit, predicted_cost=0, uncertainty=0):
        self.unit = unit
        self.predicted_cost = predicted_cost
        self.uncertainty = uncertainty
        self.score = round((1 - (uncertainty / predicted_cost)) * 100)

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

    A spread above 0.15 (15 %) is flagged via ``is_wide_spread``.
    The properties ``unit``, ``predicted_cost``, ``uncertainty``,
    ``quality``, and ``score`` delegate to ``best_result`` so this class can
    be used as a drop-in replacement for ``Result`` in most downstream code.
    The ``unit`` property returns the *original* unit (with
    ``MultipleChoiceWeapon`` slots intact) so that its base name is used in
    tables and JSON output.
    """

    SPREAD_THRESHOLD = 0.15

    all_results: list[Result]
    best_result: Result
    spread: float

    def __init__(self, original_unit: Unit, results: list[Result]):
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
    units: list[tuple[float, Result]]

    def __init__(self):
        self.units = []

    def get_errors(self):
        return map(lambda r: r[0], self.units)

    def get_mean_absolute_error(self):
        return np.mean(np.abs(self.get_errors()))

    def get_avg_absolute_error(self):
        return np.average(np.abs(self.get_errors()))
