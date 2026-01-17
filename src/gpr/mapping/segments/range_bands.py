from data.models import Unit, RangedWeapon


def range_bands(unit: Unit) -> list[float]:
    weapons = unit.get_all_ranged_weapons()
    return [
        # weapon count:
        sum(1 for w in weapons if isinstance(w, RangedWeapon) and w.range >= 100),
        sum(
            1
            for w in weapons
            if isinstance(w, RangedWeapon) and w.range >= 50 and w.range < 100
        ),
        sum(
            1
            for w in weapons
            if isinstance(w, RangedWeapon) and w.range > 30 and w.range < 50
        ),
        sum(1 for w in weapons if isinstance(w, RangedWeapon) and w.range < 30),
    ]
