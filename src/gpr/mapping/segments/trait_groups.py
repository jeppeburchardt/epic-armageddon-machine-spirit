from data.models import Unit, Traits, RangedWeapon


def trait_groups(unit: Unit) -> list[float]:
    weapons = unit.get_all_ranged_weapons()
    return [
        # Sum ranged weapons traits:
        (
            sum(
                (1 if Traits.INDIRECT in w.traits else 0)
                + (1 if Traits.IGNORE_COVER in w.traits else 0)
                + (1 if Traits.DISRUPT in w.traits else 0)
                + (1 if Traits.LANCE in w.traits else 0)
                + (1 if Traits.MW in w.traits else 0)
                for w in weapons
                if isinstance(w, RangedWeapon) and hasattr(w, "traits")
            )
        ),
        # Mobility traits:
        (
            (1 if Traits.SKIMMER in unit.traits else 0)
            + (1 if Traits.PLANET_FALL in unit.traits else 0)
            + (1 if Traits.TELEPORT in unit.traits else 0)
            + (1 if Traits.JUMP_PACKS in unit.traits else 0)
            + (1 if Traits.SCOUT in unit.traits else 0)
            + (1 if Traits.INFILTRATOR in unit.traits else 0)
        ),
        # Survivability traits:
        (
            (1 if Traits.REINFORCED_ARMOUR in unit.traits else 0)
            + (1 if Traits.THICK_REAR_ARMOUR in unit.traits else 0)
            + (1 if Traits.FEARLESS in unit.traits else 0)
            + (1 if Traits.INVULNERABLE_SAVE in unit.traits else 0)
        ),
        # Traits without categories
        (1 if Traits.KNOW_NO_FEAR in unit.traits else 0),
        (1 if Traits.WALKER in unit.traits else 0),
    ]
