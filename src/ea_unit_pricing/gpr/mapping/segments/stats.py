from __future__ import annotations

from ea_unit_pricing.domain.unit import Unit


def dice_test_to_score(dice_test: int) -> float:
    return (6 - dice_test) / 6


def stats(unit: Unit) -> list[float]:
    """Return 9 basic stat features for the GPR vector."""
    return [
        unit.strategy_rating,
        dice_test_to_score(unit.initiative),
        unit.speed,
        dice_test_to_score(unit.armour),
        dice_test_to_score(unit.ff),
        dice_test_to_score(unit.cc),
        unit.damage_capacity,
        unit.void_shields,
        unit.transport_capacity,
    ]
