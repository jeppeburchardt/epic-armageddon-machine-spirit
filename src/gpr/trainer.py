import numpy as np
import warnings

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
        print("Preparing data...")
        # print("Units in training set:")
        # for unit in units:
        #     print(f"\t{unit.name}\t{unit.single_unit_cost} points")
        # print()
        self.units = units
        unit_vectors = np.array([self.mapper(unit) for unit in units])
        self.X = self.scaler.fit_transform(unit_vectors)
        self.y = np.array([unit_to_cost(unit) for unit in units])

        kernel = ConstantKernel(1.0, (1e-2, 1e2)) * RBF(
            length_scale=1.0, length_scale_bounds=(1e-2, 1e2)
        ) + WhiteKernel(noise_level=1.0, noise_level_bounds=(1e-3, 1e1))

        print("Training model...")
        self.gpr = GaussianProcessRegressor(
            kernel=kernel,
            alpha=0.0,  # handled by WhiteKernel
            normalize_y=True,  # important for point costs
            n_restarts_optimizer=10,
            random_state=42,
        )
        self.gpr.fit(self.X, self.y)
        print("Kernel after training:")
        print(self.gpr.kernel_)
        print("Small length scale → pricing is sensitive to small stat changes")
        print("Large noise → game designers priced inconsistently")

    def validate(self):
        if self.gpr is None or self.X is None or self.y is None:
            raise RuntimeError("Model must be trained before validation.")
        loo = LeaveOneOut()
        results = []
        errors = []
        for train_idx, test_idx in loo.split(self.X):
            self.gpr.fit(self.X[train_idx], self.y[train_idx])
            pred, std_dev = self.gpr.predict(self.X[test_idx], return_std=True)
            error = pred[0] - self.y[test_idx][0]
            errors.append(error)
            unit = self.units[test_idx[0]]
            original_cost = round(unit.single_unit_cost, 0)
            predicted_cost = round(pred[0], 0)
            error_str = f"{error:+.1f}"
            uncertainty = f"±{std_dev[0]:.1f}"
            uncertainty_comared = std_dev[0] / pred[0]
            score = round((1 - uncertainty_comared) * 100)
            quality = f"{C.BAD}BAD{C.ENDC}"
            name = f"{C.BAD}{unit.name}{C.ENDC}"
            if uncertainty_comared <= 0.1:
                quality = f"{C.EXCELLENT}EXCELLENT{C.ENDC}"
                name = f"{C.EXCELLENT}{unit.name}{C.ENDC}"
            elif uncertainty_comared <= 0.25:
                quality = f"{C.GOOD}GOOD{C.ENDC}"
                name = f"{C.GOOD}{unit.name}{C.ENDC}"
            elif uncertainty_comared <= 0.35:
                quality = f"{C.MEDIOCRE}MEDIOCRE{C.ENDC}"
                name = f"{C.MEDIOCRE}{unit.name}{C.ENDC}"
            results.append(
                (
                    name,
                    original_cost,
                    predicted_cost,
                    error_str,
                    uncertainty,
                    quality,
                    score,
                )
            )
        # Optionally print summary stats
        # print(f"Mean absolute error: {np.mean(np.abs(errors)):.1f}")
        # print(f"Avg absolute error: {np.average(np.abs(errors)):.1f}")
        return results

    """ Predict the cost of a new unit """
    """ retrurns: (unit name, predicted cost, uncertainty, original cost) """

    def predict(self, unit: Unit) -> tuple[str, float, float, float]:
        if self.gpr is None or self.scaler is None:
            raise RuntimeError("Model must be trained before prediction.")
        new_unit_vector = np.array(self.mapper(unit))
        new_unit_vector_scaled = self.scaler.transform([new_unit_vector])
        mean_cost, std_dev = self.gpr.predict(new_unit_vector_scaled, return_std=True)
        # print("\n## Predicting new unit:")
        # print(f"Prediction for '{unit.name}':")
        # print(f"Predicted cost: {mean_cost[0]:.1f} points")
        # print(f"Uncertainty: ±{std_dev[0]:.1f} points")
        # print(f"Original unit cost: {unit.single_unit_cost} points")

        predicted_cost = round(mean_cost[0], 0)
        uncertainty_comared = std_dev[0] / mean_cost[0]
        uncertainty = f"±{std_dev[0]:.1f}"
        original_cost = round(unit.single_unit_cost, 0)
        score = round((1 - uncertainty_comared) * 100)

        quality = f"{C.BAD}BAD{C.ENDC}"
        name = f"{C.BAD}{unit.name}{C.ENDC}"
        if uncertainty_comared <= 0.1:
            quality = f"{C.EXCELLENT}EXCELLENT{C.ENDC}"
            name = f"{C.EXCELLENT}{unit.name}{C.ENDC}"
        elif uncertainty_comared <= 0.25:
            quality = f"{C.GOOD}GOOD{C.ENDC}"
            name = f"{C.GOOD}{unit.name}{C.ENDC}"
        elif uncertainty_comared <= 0.35:
            quality = f"{C.MEDIOCRE}MEDIOCRE{C.ENDC}"
            name = f"{C.MEDIOCRE}{unit.name}{C.ENDC}"

        return name, original_cost, predicted_cost, uncertainty, quality, score


class C:
    # EXCELLENT = '\033[94m'
    EXCELLENT = "\033[92m"
    GOOD = "\033[92m"
    MEDIOCRE = "\033[93m"
    ENDC = "\033[0m"
    BAD = "\033[91m"
