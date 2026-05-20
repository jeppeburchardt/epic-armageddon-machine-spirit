"""Tests for weapon dataclasses — no mutable-default bugs."""

from __future__ import annotations

from ea_unit_pricing.domain import Traits
from ea_unit_pricing.domain.weapons import (
    AssaultWeapon,
    Multiplier,
    MultipleChoiceWeapon,
    RangedWeapon,
    SmallArms,
)


def test_ranged_weapon_default_traits_not_shared() -> None:
    a = RangedWeapon(30)
    b = RangedWeapon(30)
    a.traits.append(Traits.INDIRECT)
    assert Traits.INDIRECT not in b.traits, "traits lists must not be shared between instances"


def test_assault_weapon_default_traits_not_shared() -> None:
    a = AssaultWeapon()
    b = AssaultWeapon()
    a.traits.append(Traits.MW)
    assert Traits.MW not in b.traits


def test_small_arms_default_traits_not_shared() -> None:
    a = SmallArms()
    b = SmallArms()
    a.traits.append(Traits.FIRST_STRIKE)
    assert Traits.FIRST_STRIKE not in b.traits


def test_ranged_weapon_default_stat_modifiers_not_shared() -> None:
    a = RangedWeapon(30)
    b = RangedWeapon(30)
    a.stat_modifiers["cc"] = -1
    assert "cc" not in b.stat_modifiers


def test_multiplier_name() -> None:
    w = RangedWeapon(30, ap=5, name="Bolter")
    m = Multiplier(3, w)
    assert m.name == "3X Bolter"


def test_multiple_choice_weapon_options() -> None:
    opts = [RangedWeapon(30, name="A"), RangedWeapon(45, name="B")]
    mc = MultipleChoiceWeapon(opts)
    assert len(mc.options) == 2
    assert mc.options[0].name == "A"


def test_ranged_weapon_to_list() -> None:
    w = RangedWeapon(45, at=5, ap=6, name="Lascannon")
    row = w.to_list()
    assert row[0] == "Lascannon"
    assert row[1] == 45
    assert "AT5+" in str(row[2])
