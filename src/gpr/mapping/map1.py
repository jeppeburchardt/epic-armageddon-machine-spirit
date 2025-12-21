import numpy as np
from data.models import Traits, Unit, UnitType, RangedWeapon, SmallArms, AssaultWeapon


def dice_test_to_score(dice_test: int) -> int:
    if dice_test <= 2:
        return 5
    elif dice_test <= 4:
        return 4
    elif dice_test <= 6:
        return 3
    elif dice_test <= 8:
        return 2
    elif dice_test <= 10:
        return 1
    else:
        return 0


def map1(unit: Unit) -> np.ndarray:
    vector = [
        unit.strategy_rating,
        dice_test_to_score(unit.initiative),
        unit.speed,
        dice_test_to_score(unit.armour),
        dice_test_to_score(unit.ff),
        dice_test_to_score(unit.cc),
        unit.damage_capacity,
        (1 if unit.type == UnitType.CHARACTER else 0),
        (1 if unit.type == UnitType.INFANTRY else 0),
        (1 if unit.type == UnitType.LIGHT_VEHICLE else 0),
        (1 if unit.type == UnitType.ARMORED_VEHICLE else 0),
        (1 if unit.type == UnitType.CHARACTER else 0),
        (1 if unit.type == UnitType.WAR_ENGINE else 0),
        (1 if unit.type == UnitType.AIRCRAFT else 0),
        (1 if Traits.TELEPORT in unit.traits else 0),
        (1 if Traits.ASTARTES in unit.traits else 0),
        (1 if Traits.WALKER in unit.traits else 0),
        (1 if Traits.PLANETFALL in unit.traits else 0),
        (1 if Traits.RIENFORCED_ARMOUR in unit.traits else 0),
        unit.transport_capacity,
        # weapon count:
        sum(1 for w in unit.weapons if isinstance(w, RangedWeapon)),
        sum(1 for w in unit.weapons if isinstance(w, SmallArms)),
        sum(1 for w in unit.weapons if isinstance(w, AssaultWeapon)),
        # range max:
        max(
            (
                weapon.range
                for weapon in unit.weapons
                if isinstance(weapon, RangedWeapon)
            ),
            default=0,
        ),
        # range min:
        min(
            (
                weapon.range
                for weapon in unit.weapons
                if isinstance(weapon, RangedWeapon)
            ),
            default=0,
        ),
        # range mean:
        # np.mean([weapon.range for weapon in unit.weapons if isinstance(weapon, RangedWeapon)]) if unit.weapons else 0,
        # at total:
        sum(
            (
                dice_test_to_score(weapon.at)
                for weapon in unit.weapons
                if hasattr(weapon, "at")
            )
        ),
        # ap total:
        sum(
            (
                dice_test_to_score(weapon.ap)
                for weapon in unit.weapons
                if hasattr(weapon, "ap")
            )
        ),
        # aa total:
        sum(
            (
                dice_test_to_score(weapon.aa)
                for weapon in unit.weapons
                if hasattr(weapon, "aa")
            )
        ),
        # bp total:
        sum(
            (
                dice_test_to_score(weapon.bp)
                for weapon in unit.weapons
                if hasattr(weapon, "bp")
            )
        ),
        # mw total:
        sum(
            (
                dice_test_to_score(weapon.mw)
                for weapon in unit.weapons
                if hasattr(weapon, "mw")
            )
        ),
        # weapon traits:
        sum(1 for w in unit.weapons if hasattr(w, "traits") and Traits.MW in w.traits),
        sum(
            1
            for w in unit.weapons
            if hasattr(w, "traits") and Traits.FIRST_STRIKE in w.traits
        ),
        sum(
            1
            for w in unit.weapons
            if hasattr(w, "traits") and Traits.EXTRA_ATTACK_1 in w.traits
        ),
    ]
    return np.array(vector)
