import numpy as np
from data.models import Unit


class Result:
    unit: Unit
    predicted_cost: int
    uncertainty: float
    quality: str
    score: float

    def __init__(self, unit: Unit, predicted_cost=0, uncertainty=0):
        self.unit = unit
        self.predicted_cost = predicted_cost
        self.uncertainty = uncertainty
        self.quality = "TBD"
        self.score = round((1 - (uncertainty / predicted_cost)) * 100)


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
