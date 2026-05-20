from __future__ import annotations

from ea_unit_pricing.domain.enums import Traits
from ea_unit_pricing.domain.unit import Unit
from ea_unit_pricing.domain.weapons import AssaultWeapon


def extra_damage(unit: Unit) -> list[float]:
    """Return 2 features for titan-killer capability and assault extra attacks."""
    weapons = unit.get_all_ranged_weapons()
    return [
        sum(
            (1 if Traits.TITAN_KILLER_1 in w.traits else 0)
            + (1.5 if Traits.TITAN_KILLER_D3 in w.traits else 0)
            + (3 if Traits.TITAN_KILLER_D6 in w.traits else 0)
            for w in weapons
            if hasattr(w, "traits")
        ),
        sum(
            (1 if Traits.EXTRA_ATTACK_1 in w.traits else 0)
            + (2 if Traits.EXTRA_ATTACK_2 in w.traits else 0)
            + (3 if Traits.EXTRA_ATTACK_3 in w.traits else 0)
            for w in weapons
            if isinstance(w, AssaultWeapon) and hasattr(w, "traits")
        ),
    ]
