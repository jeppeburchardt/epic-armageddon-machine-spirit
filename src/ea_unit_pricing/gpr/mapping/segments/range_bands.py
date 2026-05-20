from __future__ import annotations

from ea_unit_pricing.domain.unit import Unit
from ea_unit_pricing.domain.weapons import RangedWeapon


def range_bands(unit: Unit) -> list[float]:
    """Return 4 features counting weapons in each range band."""
    weapons = unit.get_all_ranged_weapons()
    return [
        sum(1 for w in weapons if isinstance(w, RangedWeapon) and w.range >= 100),
        sum(1 for w in weapons if isinstance(w, RangedWeapon) and 50 <= w.range < 100),
        sum(1 for w in weapons if isinstance(w, RangedWeapon) and 30 < w.range < 50),
        sum(1 for w in weapons if isinstance(w, RangedWeapon) and w.range < 30),
    ]
