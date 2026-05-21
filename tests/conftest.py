"""Shared pytest fixtures."""

from __future__ import annotations

from pathlib import Path

import pytest

from ea_unit_pricing.domain import (
    RangedWeapon,
    Traits,
    Unit,
    UnitType,
)
from ea_unit_pricing.gpr.mapping.universal_unit import universal_unit
from ea_unit_pricing.gpr.trainer import GPRTrainer


@pytest.fixture(scope="session")
def golden_dir() -> Path:
    return Path(__file__).parent / "golden"


@pytest.fixture(scope="session")
def sample_infantry_unit() -> Unit:
    return Unit(
        "Test Infantry",
        strategy_rating=5,
        initiative=1,
        type=UnitType.INFANTRY,
        speed=15,
        armour=4,
        cc=4,
        ff=4,
        single_unit_cost=50,
        weapons=[RangedWeapon(45, at=6, ap=5)],
        traits=[Traits.KNOW_NO_FEAR],
    )


@pytest.fixture(scope="session")
def sample_vehicle_unit() -> Unit:
    return Unit(
        "Test Tank",
        strategy_rating=3,
        initiative=2,
        type=UnitType.ARMORED_VEHICLE,
        speed=25,
        armour=4,
        cc=6,
        ff=5,
        single_unit_cost=100,
        weapons=[RangedWeapon(75, at=4, ap=4), RangedWeapon(30, ap=5)],
        damage_capacity=1,
    )


@pytest.fixture(scope="session")
def trained_trainer(sample_infantry_unit: Unit, sample_vehicle_unit: Unit) -> GPRTrainer:
    """Return a GPRTrainer fitted on a tiny synthetic training set."""

    units = [
        sample_infantry_unit,
        sample_vehicle_unit,
        Unit(
            "War Engine",
            strategy_rating=2,
            initiative=3,
            type=UnitType.WAR_ENGINE,
            speed=20,
            armour=3,
            cc=5,
            ff=5,
            single_unit_cost=400,
            weapons=[RangedWeapon(75, at=3, ap=3), RangedWeapon(45, at=5)],
            damage_capacity=4,
            void_shields=2,
        ),
        Unit(
            "Scout",
            strategy_rating=5,
            initiative=1,
            type=UnitType.INFANTRY,
            speed=20,
            armour=5,
            cc=4,
            ff=4,
            single_unit_cost=30,
            weapons=[RangedWeapon(30, ap=5)],
            traits=[Traits.SCOUT, Traits.INFILTRATOR],
        ),
    ]
    trainer = GPRTrainer(mapper=universal_unit, random_state=42)
    trainer.train(units)
    return trainer


@pytest.fixture()
def tmp_output_dir(tmp_path: Path) -> Path:
    d = tmp_path / "output"
    d.mkdir()
    return d
