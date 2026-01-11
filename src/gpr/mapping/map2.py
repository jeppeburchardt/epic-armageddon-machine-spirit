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


def map2(unit: Unit) -> np.ndarray:
    weapons = unit.get_all_ranged_weapons()
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
        (1 if Traits.JUMP_PACKS in unit.traits else 0),
        (1 if Traits.INFILTRQATOR in unit.traits else 0),
        unit.transport_capacity,
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
        sum(1 for w in weapons if isinstance(w, SmallArms)),
        sum(1 for w in weapons if isinstance(w, AssaultWeapon)),
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
        # sum weapon traits:
        # sum(1 for w in weapons if hasattr(w, 'traits') and Traits.MW in w.traits),
        # sum(1 for w in weapons if hasattr(w, 'traits') and Traits.FIRST_STRIKE in w.traits),
        # sum(1 for w in weapons if hasattr(w, 'traits') and Traits.EXTRA_ATTACK_1 in w.traits),
        # sum(1 for w in weapons if hasattr(w, 'traits') and Traits.IGNORE_COVER in w.traits),
        # sum(1 for w in weapons if hasattr(w, 'traits') and Traits.INDIRECT in w.traits),
        # bool weapon traits:
        (
            1
            if any(hasattr(w, "traits") and Traits.MW in w.traits for w in weapons)
            else 0
        ),
        (
            1
            if any(
                hasattr(w, "traits") and Traits.FIRST_STRIKE in w.traits
                for w in weapons
            )
            else 0
        ),
        (
            1
            if any(
                hasattr(w, "traits") and Traits.EXTRA_ATTACK_1 in w.traits
                for w in weapons
            )
            else 0
        ),
        (
            1
            if any(
                hasattr(w, "traits") and Traits.EXTRA_ATTACK_2 in w.traits
                for w in weapons
            )
            else 0
        ),
        (
            1
            if any(
                hasattr(w, "traits") and Traits.IGNORE_COVER in w.traits
                for w in weapons
            )
            else 0
        ),
        (
            1
            if any(
                hasattr(w, "traits") and Traits.INDIRECT in w.traits for w in weapons
            )
            else 0
        ),
        (
            1
            if any(hasattr(w, "traits") and Traits.DISRUPT in w.traits for w in weapons)
            else 0
        ),
        (
            1
            if any(
                hasattr(w, "traits") and Traits.VOID_SHIELDS in w.traits
                for w in weapons
            )
            else 0
        ),
        (
            1
            if any(hasattr(w, "traits") and Traits.LEADER in w.traits for w in weapons)
            else 0
        ),
        (
            1
            if any(
                hasattr(w, "traits") and Traits.COMMANDER in w.traits for w in weapons
            )
            else 0
        ),
        (
            1
            if any(
                hasattr(w, "traits") and Traits.SUPREME_COMMANDER in w.traits
                for w in weapons
            )
            else 0
        ),
        (
            1
            if any(
                hasattr(w, "traits") and Traits.INVULNERABLE_SAVE in w.traits
                for w in weapons
            )
            else 0
        ),
    ]
    # print(f"Mapping unit '{vector}' {unit.name}")
    return np.array(vector)
