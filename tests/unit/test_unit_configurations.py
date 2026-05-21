"""Tests for MultipleChoiceWeapon expansion."""

from __future__ import annotations

import pytest

from ea_unit_pricing.domain import RangedWeapon, Unit, UnitType
from ea_unit_pricing.domain.unit import expand_choices
from ea_unit_pricing.domain.weapons import MultipleChoiceWeapon


@pytest.fixture()
def plain_unit() -> Unit:
    return Unit(
        "Plain",
        strategy_rating=5,
        initiative=1,
        type=UnitType.INFANTRY,
        weapons=[RangedWeapon(45, at=5)],
    )


@pytest.fixture()
def choice_unit() -> Unit:
    return Unit(
        "Choice",
        strategy_rating=5,
        initiative=1,
        type=UnitType.INFANTRY,
        weapons=[
            RangedWeapon(45, at=5, name="Lascannon"),
            MultipleChoiceWeapon(
                [
                    RangedWeapon(30, ap=5, name="Bolter"),
                    RangedWeapon(30, ap=4, name="Plasma"),
                ]
            ),
        ],
    )


def test_plain_unit_returns_self(plain_unit: Unit) -> None:
    configs = expand_choices(plain_unit)
    assert configs == [plain_unit]


def test_choice_unit_expands_to_two(choice_unit: Unit) -> None:
    configs = expand_choices(choice_unit)
    assert len(configs) == 2


def test_choice_variant_names(choice_unit: Unit) -> None:
    configs = expand_choices(choice_unit)
    names = {c.name for c in configs}
    assert "Choice [Bolter]" in names
    assert "Choice [Plasma]" in names


def test_choice_variants_keep_fixed_weapon(choice_unit: Unit) -> None:
    configs = expand_choices(choice_unit)
    for config in configs:
        assert any(w.name == "Lascannon" for w in config.weapons if hasattr(w, "name"))


def test_stat_modifiers_applied() -> None:
    unit = Unit(
        "Modded",
        strategy_rating=5,
        initiative=1,
        type=UnitType.INFANTRY,
        cc=4,
        weapons=[
            MultipleChoiceWeapon(
                [
                    RangedWeapon(30, ap=5, name="Basic"),
                    RangedWeapon(30, ap=4, name="CC-Boost", stat_modifiers={"cc": -1}),
                ]
            )
        ],
    )
    configs = expand_choices(unit)
    basic = next(c for c in configs if "Basic" in c.name)
    boosted = next(c for c in configs if "CC-Boost" in c.name)
    assert basic.cc == 4
    assert boosted.cc == 3  # cc improved by -1 (lower = better)


def test_cartesian_product_two_choice_slots() -> None:
    unit = Unit(
        "Double Choice",
        strategy_rating=5,
        initiative=1,
        type=UnitType.INFANTRY,
        weapons=[
            MultipleChoiceWeapon([RangedWeapon(30, name="A"), RangedWeapon(30, name="B")]),
            MultipleChoiceWeapon([RangedWeapon(45, name="X"), RangedWeapon(45, name="Y")]),
        ],
    )
    configs = expand_choices(unit)
    assert len(configs) == 4
    names = {c.name for c in configs}
    assert "Double Choice [A | X]" in names
    assert "Double Choice [B | Y]" in names
