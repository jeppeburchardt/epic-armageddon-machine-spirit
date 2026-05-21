"""GPR trainer that trains one model per unit-type group."""

from __future__ import annotations

import logging
from typing import Any, Callable

from ea_unit_pricing.domain.enums import UnitType
from ea_unit_pricing.domain.result import Result
from ea_unit_pricing.domain.unit import Unit
from ea_unit_pricing.gpr.trainer import GPRTrainer

__all__ = ["GPRSplitTrainer"]

logger = logging.getLogger(__name__)


def _split_by_type(unit: Unit) -> UnitType | None:
    return getattr(unit, "type", None)


class GPRSplitTrainer:
    """Trains a separate ``GPRTrainer`` for each group defined by *splitter*.

    Args:
        mapper: Feature-vector callable passed to each ``GPRTrainer``.
        splitter: Callable ``(Unit) -> Hashable`` used to partition the
            training set.  Defaults to splitting by ``UnitType``.
        random_state: Seed for each underlying ``GPRTrainer``.
    """

    def __init__(
        self,
        mapper: Callable[[Unit], Any] | None = None,
        splitter: Callable[[Unit], object] = _split_by_type,
        random_state: int = 42,
    ) -> None:
        self.mapper: Callable[[Unit], Any] | None = mapper
        self.splitter = splitter
        self.random_state = random_state
        self.trainers: dict[object, GPRTrainer] = {}

    def train(self, units: list[Unit]) -> None:
        """Partition *units* by *splitter* and fit one model per group."""
        split_units: dict[object, list[Unit]] = {}
        for unit in units:
            key = self.splitter(unit)
            split_units.setdefault(key, []).append(unit)

        for key, group in split_units.items():
            trainer = GPRTrainer(self.mapper, random_state=self.random_state)
            trainer.train(group)
            self.trainers[key] = trainer
            logger.info("Trained %d units in group %s", len(group), key)

    def validate(self) -> None:
        for trainer in self.trainers.values():
            trainer.validate()

    def predict(self, unit: Unit) -> Result | None:
        key = self.splitter(unit)
        if key in self.trainers:
            try:
                return self.trainers[key].predict(unit)
            except ValueError:
                return None
        raise KeyError(f"Training set does not include unit type {key!r}")
