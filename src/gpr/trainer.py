import numpy as np
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")
from sklearn.preprocessing import MinMaxScaler
from sklearn.gaussian_process.kernels import RBF, WhiteKernel, ConstantKernel
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.model_selection import LeaveOneOut

from data.models import  Unit

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
        print("\n## Preparing data...")
        print("Units in training set:")
        for unit in units:
            print(f"\t{unit.name}\t{unit.single_unit_cost} points")
        print()
        self.units = units
        unit_vectors = np.array([self.mapper(unit) for unit in units])
        self.X = self.scaler.fit_transform(unit_vectors)
        self.y = np.array([unit_to_cost(unit) for unit in units])

        kernel = (
            ConstantKernel(1.0, (1e-2, 1e2)) *
            RBF(length_scale=1.0, length_scale_bounds=(1e-2, 1e2)) +
            WhiteKernel(noise_level=1.0, noise_level_bounds=(1e-3, 1e1))
        )

        print("## Training model...")
        self.gpr = GaussianProcessRegressor(
            kernel=kernel,
            alpha=0.0,            # handled by WhiteKernel
            normalize_y=True,     # important for point costs
            n_restarts_optimizer=10,
            random_state=42
        )
        self.gpr.fit(self.X, self.y)
        print("Kernel after training:")
        print(self.gpr.kernel_)
        print("Small length scale → pricing is sensitive to small stat changes")
        print("Large noise → game designers priced inconsistently")

    def validate(self):
        if self.gpr is None or self.X is None or self.y is None:
            raise RuntimeError("Model must be trained before validation.")
        print("\n## Cross-validation with Leave-One-Out:")
        loo = LeaveOneOut()
        errors = []
        for train_idx, test_idx in loo.split(self.X):
            self.gpr.fit(self.X[train_idx], self.y[train_idx])
            pred = self.gpr.predict(self.X[test_idx])[0]
            errors.append(pred - self.y[test_idx][0])
            print(f"\t{self.units[test_idx[0]].name}\t{round(pred - self.y[test_idx][0]):+} points")
        print(f"Mean absolute error: {np.mean(np.abs(errors)):.1f}")
        print(f"Avg absolute error: {np.average(np.abs(errors)):.1f}")

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
        uncertancy_comared =  std_dev[0] / mean_cost[0]

        status = f"{C.BAD}BAD {round(uncertancy_comared, 1)}{C.ENDC}" 
        name = f"{C.BAD}{unit.name}{C.ENDC}" 
        if (uncertancy_comared <= 0.1):
            status = f"{C.EXELENT}EXELENT {round(uncertancy_comared, 1)}{C.ENDC}"
            name = f"{C.EXELENT}{unit.name}{C.ENDC}" 
        elif (uncertancy_comared <= 0.25):
            status = f"{C.GOOD}GOOD {round(uncertancy_comared, 1)}{C.ENDC}"
            name = f"{C.GOOD}{unit.name}{C.ENDC}" 
        elif (uncertancy_comared <= 0.35):
            status = f"{C.MEDIOCRE}MEDIOCRE {round(uncertancy_comared, 1)}{C.ENDC}"
            name = f"{C.MEDIOCRE}{unit.name}{C.ENDC}" 

        return name, predicted_cost, std_dev[0], unit.single_unit_cost, status


class C:
    # EXELENT = '\033[94m'
    EXELENT = '\033[92m'
    GOOD = '\033[92m'
    MEDIOCRE = '\033[93m'
    ENDC = '\033[0m'
    BAD = '\033[91m'

