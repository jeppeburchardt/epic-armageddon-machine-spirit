from __future__ import annotations

from ea_unit_pricing.domain.unit import Unit
from ea_unit_pricing.domain.weapons import RangedWeapon


def dice_test_to_score(dice_test: int) -> float:
    return (6 - dice_test) / 6


def fire_power(unit: Unit) -> list[float]:
    """Return 5 features summarising total ranged firepower by category."""
    weapons = unit.get_all_ranged_weapons()
    return [
        sum(dice_test_to_score(w.at) for w in weapons if isinstance(w, RangedWeapon) and w.at > 0),
        sum(dice_test_to_score(w.ap) for w in weapons if isinstance(w, RangedWeapon) and w.ap > 0),
        sum(dice_test_to_score(w.aa) for w in weapons if isinstance(w, RangedWeapon) and w.aa > 0),
        sum(w.bp for w in weapons if isinstance(w, RangedWeapon) and w.bp > 0),
        sum(dice_test_to_score(w.mw) for w in weapons if isinstance(w, RangedWeapon) and w.mw > 0),
    ]
