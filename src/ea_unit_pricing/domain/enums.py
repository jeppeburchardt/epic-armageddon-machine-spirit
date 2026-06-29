"""Domain enumerations for unit types, traits, and quality ratings."""

from __future__ import annotations

from enum import Enum

__all__ = [
    "AircraftSpeed",
    "Quality",
    "Traits",
    "UnitType",
    "aircraft_speed_to_string",
    "quality_to_str",
    "trait_to_string",
    "unit_type_to_string",
]


class UnitType(Enum):
    CHARACTER = 0
    INFANTRY = 1
    LIGHT_VEHICLE = 2
    ARMORED_VEHICLE = 3
    AIRCRAFT = 4
    WAR_ENGINE = 5
    AIRCRAFT_WAR_ENGINE = 6
    SPACESHIP = 7


class AircraftSpeed(Enum):
    NONE = None
    FIGHTER = 0
    BOMBER = 1
    FIGHTER_BOMBER = 2


class Traits(Enum):
    EXTRA_ATTACK_1 = 1
    EXTRA_ATTACK_2 = 2
    EXTRA_ATTACK_3 = 3
    INDIRECT = 4
    SINGLE_SHOT = 5
    IGNORE_COVER = 6
    FIXED_FORWARD = 7
    REINFORCED_ARMOUR = 8
    TELEPORT = 9
    THICK_REAR_ARMOUR = 10
    MW = 11
    KNOW_NO_FEAR = 12
    JUMP_PACKS = 13
    SCOUT = 14
    INFILTRATOR = 15
    MOUNTED = 16
    FIRST_STRIKE = 17
    WALKER = 18
    PLANET_FALL = 19
    TITAN_KILLER_D3 = 20
    TITAN_KILLER_1 = 21
    EXPENDABLE = 22
    DISRUPT = 23
    FEARLESS = 24
    SKIMMER = 25
    LANCE = 26
    SUPREME_COMMANDER = 27
    LEADER = 28
    COMMANDER = 29
    INVULNERABLE_SAVE = 30
    SLOW_FIRING = 31
    REAR = 32
    FxF = 33
    LEFT = 34
    RIGHT = 35
    INSPIRING = 36
    TITAN_KILLER_D6 = 37
    TUNNELER = 38


class Quality(Enum):
    SAFE = 0
    REVIEW = 1
    EXPERIMENTAL = 2


# ---------------------------------------------------------------------------
# String converters
# ---------------------------------------------------------------------------


def unit_type_to_string(unit_type: UnitType) -> str:
    """Return the short display abbreviation for a unit type."""
    mapping: dict[UnitType, str] = {
        UnitType.CHARACTER: "CH",
        UnitType.INFANTRY: "INF",
        UnitType.LIGHT_VEHICLE: "LV",
        UnitType.ARMORED_VEHICLE: "AV",
        UnitType.AIRCRAFT: "AC",
        UnitType.WAR_ENGINE: "WE",
        UnitType.AIRCRAFT_WAR_ENGINE: "AC/WE",
    }
    return mapping.get(unit_type, str(unit_type))


def aircraft_speed_to_string(speed: AircraftSpeed) -> str:
    """Return the human-readable aircraft speed label."""
    mapping: dict[AircraftSpeed, str] = {
        AircraftSpeed.FIGHTER: "Fighter",
        AircraftSpeed.BOMBER: "Bomber",
        AircraftSpeed.FIGHTER_BOMBER: "Fighter bomber",
    }
    return mapping.get(speed, str(speed))


def trait_to_string(trait: Traits) -> str:
    """Return the human-readable label for a trait."""
    mapping: dict[Traits, str] = {
        Traits.EXTRA_ATTACK_1: "Extra Attack +1",
        Traits.EXTRA_ATTACK_2: "Extra Attack +2",
        Traits.EXTRA_ATTACK_3: "Extra Attack +3",
        Traits.INDIRECT: "Indirect",
        Traits.SINGLE_SHOT: "Single Shot",
        Traits.IGNORE_COVER: "Ignore Cover",
        Traits.FIXED_FORWARD: "FxF",
        Traits.REINFORCED_ARMOUR: "Reinforced Armour",
        Traits.TELEPORT: "Teleport",
        Traits.THICK_REAR_ARMOUR: "Thick Rear Armour",
        Traits.MW: "Macro-Weapon",
        Traits.KNOW_NO_FEAR: "Know no fear",
        Traits.JUMP_PACKS: "Jump Packs",
        Traits.SCOUT: "Scout",
        Traits.INFILTRATOR: "Infiltrator",
        Traits.MOUNTED: "Mounted",
        Traits.FIRST_STRIKE: "First Strike",
        Traits.WALKER: "Walker",
        Traits.PLANET_FALL: "Planetfall",
        Traits.TITAN_KILLER_D3: "Titan Killer (D3)",
        Traits.DISRUPT: "Disrupt",
        Traits.FEARLESS: "Fearless",
        Traits.SKIMMER: "Skimmer",
        Traits.LANCE: "Lance",
        Traits.SUPREME_COMMANDER: "Supreme Commander",
        Traits.LEADER: "Leader",
        Traits.COMMANDER: "Commander",
        Traits.INVULNERABLE_SAVE: "Invulnerable Save",
        Traits.SLOW_FIRING: "Slow Firing",
        Traits.REAR: "Rear Arc",
        Traits.FxF: "FxF",
        Traits.LEFT: "Left Arc",
        Traits.RIGHT: "Right Arc",
        Traits.TITAN_KILLER_1: "Titan Killer (1)",
    }
    return mapping.get(trait, str(trait))


def quality_to_str(quality: Quality) -> str:
    """Return the human-readable label for a prediction quality level."""
    mapping: dict[Quality, str] = {
        Quality.SAFE: "Safe",
        Quality.REVIEW: "Review",
        Quality.EXPERIMENTAL: "Experimental",
    }
    return mapping.get(quality, str(quality))
