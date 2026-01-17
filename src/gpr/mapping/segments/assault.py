from data.models import Traits, Unit, AssaultWeapon


def assault(unit: Unit) -> list[float]:
    weapons = unit.get_all_ranged_weapons()
    return [
        # Has any MW Assault Weapon:
        (
            1
            if any(
                isinstance(w, AssaultWeapon)
                and hasattr(w, "traits")
                and Traits.MW in w.traits
                for w in weapons
            )
            else 0
        ),
    ]
