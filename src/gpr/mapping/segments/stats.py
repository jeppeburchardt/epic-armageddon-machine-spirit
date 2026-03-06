from models.units import Unit


def dice_test_to_score(dice_test: int) -> int:
    return (6 - dice_test) / 6


def stats(unit: Unit) -> list[float]:
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
