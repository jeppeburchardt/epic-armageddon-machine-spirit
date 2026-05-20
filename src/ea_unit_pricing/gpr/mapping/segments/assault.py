from __future__ import annotations

from ea_unit_pricing.domain.enums import Traits
from ea_unit_pricing.domain.unit import Unit
from ea_unit_pricing.domain.weapons import AssaultWeapon


def assault(unit: Unit) -> list[float]:
    """Return 1 feature indicating presence of a macro-weapon assault weapon."""
    weapons = unit.get_all_ranged_weapons()
    return [
        1
        if any(
            isinstance(w, AssaultWeapon) and hasattr(w, "traits") and Traits.MW in w.traits
            for w in weapons
        )
        else 0
    ]
