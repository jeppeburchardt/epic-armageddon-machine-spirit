from models.units import Unit
from gpr.trainer import GPRTrainer
from models.result import Result


def splitByType(unit: Unit):
    return getattr(unit, "type", None)


class GPRSplitTrainer:
    def __init__(self, mapper=None, splitter=splitByType):
        self.mapper = mapper
        self.splitter = splitter
        self.trainers = {}

    def train(self, units: list[Unit]):
        split_units = {}
        for unit in units:
            key = self.splitter(unit)
            if key not in split_units:
                split_units[key] = []
            split_units[key].append(unit)

        # Create a GPRTrainer for each unit type
        for key, group in split_units.items():
            trainer = GPRTrainer(self.mapper)
            trainer.train(group)
            self.trainers[key] = trainer
            print(f"Training {len(group)} units in group {key}")

    def validate(self):
        for key, trainer in self.trainers.items():
            trainer.validate()

    def predict(self, unit: Unit) -> Result:
        key = self.splitter(unit)
        if key in self.trainers:
            try:
                return self.trainers[key].predict(unit)
            except ValueError:
                return None
        else:
            raise f"Training set does not include unit type {key}"
