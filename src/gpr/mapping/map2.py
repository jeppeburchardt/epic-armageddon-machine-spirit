import numpy as np
from data.models import Traits, Unit, UnitType, RangedWeapon, SmallArms, AssaultWeapon


def dice_test_to_score(dice_test: int) -> int:
    return (6 - dice_test) / 6


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
        unit.void_shields,
        (1 if unit.type == UnitType.CHARACTER or unit.type == UnitType.INFANTRY else 0),
        (
            1
            if unit.type == UnitType.LIGHT_VEHICLE
            or unit.type == UnitType.ARMORED_VEHICLE
            else 0
        ),
        (
            1
            if unit.type == UnitType.WAR_ENGINE
            or unit.type == UnitType.AIRCRAFT_WAR_ENGINE
            else 0
        ),
        (
            1
            if unit.type == UnitType.AIRCRAFT
            or unit.type == UnitType.AIRCRAFT_WAR_ENGINE
            else 0
        ),
        (1 if Traits.KNOW_NO_FEAR in unit.traits else 0),
        (1 if Traits.WALKER in unit.traits else 0),
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
    ]
    return np.array(vector)
