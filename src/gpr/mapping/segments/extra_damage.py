from data.models import Unit, Traits, AssaultWeapon


def extra_damage(unit: Unit) -> list[float]:
    weapons = unit.get_all_ranged_weapons()
    return [
        # Sum titan killer stats:
        (
            sum(
                (1 if Traits.TITAN_KILLER_1 in w.traits else 0)
                + (1.5 if Traits.TITAN_KILLER_D3 in w.traits else 0)
                + (3 if Traits.TITAN_KILLER_D6 in w.traits else 0)
                for w in weapons
                if hasattr(w, "traits")
            )
        ),
        # Sum Assault Weapons extra attacks:
        (
            sum(
                (1 if Traits.EXTRA_ATTACK_1 in w.traits else 0)
                + (2 if Traits.EXTRA_ATTACK_2 in w.traits else 0)
                + (3 if Traits.EXTRA_ATTACK_3 in w.traits else 0)
                for w in weapons
                if isinstance(w, AssaultWeapon) and hasattr(w, "traits")
            )
        ),
    ]
