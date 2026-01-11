import numpy as np
from data.models import Unit
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
