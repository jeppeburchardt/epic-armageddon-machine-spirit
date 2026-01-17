from data.models import Unit


def dice_test_to_score(dice_test: int) -> int:
    return (6 - dice_test) / 6


def fire_power(unit: Unit) -> list[float]:
    weapons = unit.get_all_ranged_weapons()
    return [
        # at total:
        sum(
            (
                dice_test_to_score(weapon.at)
                for weapon in weapons
                if hasattr(weapon, "at") and weapon.at > 0
            )
        ),
        # ap total:
        sum(
            (
                dice_test_to_score(weapon.ap)
                for weapon in weapons
                if hasattr(weapon, "ap") and weapon.ap > 0
            )
        ),
        # aa total:
        sum(
            (
                dice_test_to_score(weapon.aa)
                for weapon in weapons
                if hasattr(weapon, "aa") and weapon.aa > 0
            )
        ),
        # bp total:
        sum(
            (
                (weapon.bp)
                for weapon in weapons
                if hasattr(weapon, "bp") and weapon.bp > 0
            )
        ),
        # mw total:
        sum(
            (
                dice_test_to_score(weapon.mw)
                for weapon in weapons
                if hasattr(weapon, "mw") and weapon.mw > 0
            )
        ),
    ]
