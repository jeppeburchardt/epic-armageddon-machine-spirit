from __future__ import annotations

from ea_unit_pricing.domain.enums import Traits
from ea_unit_pricing.domain.unit import Unit
from ea_unit_pricing.domain.weapons import RangedWeapon


def trait_groups(unit: Unit) -> list[float]:
    """Return 5 features grouping traits by tactical role."""
    weapons = unit.get_all_ranged_weapons()
    return [
        sum(
            (1 if Traits.INDIRECT in w.traits else 0)
            + (1 if Traits.IGNORE_COVER in w.traits else 0)
            + (1 if Traits.DISRUPT in w.traits else 0)
            + (1 if Traits.LANCE in w.traits else 0)
            + (1 if Traits.MW in w.traits else 0)
            for w in weapons
            if isinstance(w, RangedWeapon) and hasattr(w, "traits")
        ),
        (
            (1 if Traits.SKIMMER in unit.traits else 0)
            + (1 if Traits.PLANET_FALL in unit.traits else 0)
            + (1 if Traits.TELEPORT in unit.traits else 0)
            + (1 if Traits.JUMP_PACKS in unit.traits else 0)
            + (1 if Traits.SCOUT in unit.traits else 0)
            + (1 if Traits.INFILTRATOR in unit.traits else 0)
        ),
        (
            (1 if Traits.REINFORCED_ARMOUR in unit.traits else 0)
            + (1 if Traits.THICK_REAR_ARMOUR in unit.traits else 0)
            + (1 if Traits.FEARLESS in unit.traits else 0)
            + (1 if Traits.INVULNERABLE_SAVE in unit.traits else 0)
        ),
        1 if Traits.KNOW_NO_FEAR in unit.traits else 0,
        1 if Traits.WALKER in unit.traits else 0,
    ]
