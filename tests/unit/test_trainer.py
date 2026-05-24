"""Tests for the GPR trainer pipeline."""

from __future__ import annotations

import pytest

from ea_unit_pricing.domain import Unit, UnitType
from ea_unit_pricing.domain.result import Result
from ea_unit_pricing.gpr.mapping.universal_unit import universal_unit
from ea_unit_pricing.gpr.trainer import GPRTrainer


def test_trainer_predict_returns_result(
    trained_trainer: GPRTrainer, sample_infantry_unit: Unit
) -> None:
    result = trained_trainer.predict(sample_infantry_unit)
    assert isinstance(result, Result)
    assert result.predicted_cost > 0
    assert result.uncertainty >= 0


def test_trainer_predict_has_reasonable_cost(
    trained_trainer: GPRTrainer, sample_infantry_unit: Unit
) -> None:
    result = trained_trainer.predict(sample_infantry_unit)
    # Predicted cost should be within a wide but sane range
    assert 0 < result.predicted_cost < 2000


def test_trainer_predict_uncertainty_positive(
    trained_trainer: GPRTrainer, sample_infantry_unit: Unit
) -> None:
    result = trained_trainer.predict(sample_infantry_unit)
    assert result.uncertainty >= 0


def test_trainer_requires_training_before_predict() -> None:
    trainer = GPRTrainer(mapper=universal_unit)
    unit = Unit("X", 5, 1, UnitType.INFANTRY)
    with pytest.raises(RuntimeError, match="trained"):
        trainer.predict(unit)


def test_trainer_random_state_reproducibility(sample_infantry_unit: Unit) -> None:
    units = [
        Unit("A", 5, 1, UnitType.INFANTRY, speed=15, armour=4, cc=4, ff=4, single_unit_cost=50),
        Unit(
            "B",
            3,
            2,
            UnitType.ARMORED_VEHICLE,
            speed=25,
            armour=4,
            cc=6,
            ff=5,
            single_unit_cost=100,
        ),
        Unit(
            "C",
            2,
            3,
            UnitType.WAR_ENGINE,
            speed=20,
            armour=3,
            cc=5,
            ff=5,
            single_unit_cost=400,
            damage_capacity=4,
        ),
    ]
    t1 = GPRTrainer(mapper=universal_unit, random_state=42)
    t2 = GPRTrainer(mapper=universal_unit, random_state=42)
    t1.train(units)
    t2.train(units)

    r1 = t1.predict(sample_infantry_unit)
    r2 = t2.predict(sample_infantry_unit)
    assert abs(r1.predicted_cost - r2.predicted_cost) < 1e-6
