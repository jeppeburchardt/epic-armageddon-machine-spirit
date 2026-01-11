from enum import Enum


class UnitType(Enum):
    CHARACTER = 0
    INFANTRY = 1
    LIGHT_VEHICLE = 2
    ARMORED_VEHICLE = 3
    AIRCRAFT = 4
    WAR_ENGINE = 5
    AIRCRAFT_WAR_ENGINE = 6


def unit_type_to_string(unit_type):
    """
    Maps a UnitType enum value to a human-readable string.
    """
    mapping = {
        UnitType.CHARACTER: "CHR",
        UnitType.INFANTRY: "INF",
        UnitType.LIGHT_VEHICLE: "LV",
        UnitType.ARMORED_VEHICLE: "AV",
        UnitType.AIRCRAFT: "AC",
        UnitType.WAR_ENGINE: "WE",
        UnitType.AIRCRAFT_WAR_ENGINE: "AC/WE",
    }
    return mapping.get(unit_type, str(unit_type))


class Unit:
    name: str
    strategy_rating: int
    initiative: int
    type: UnitType
    speed: int
    armour: int
    cc: int
    ff: int
    transport_capacity: int
    damage_capacity: int
    single_unit_cost: int
    weapons: list["RangedWeapon", "AssaultWeapon", "SmallArms"]
    traits: list["Traits"] = []

    def __init__(
        self,
        name,
        strategy_rating,
        initiative,
        type,
        speed,
        armour,
        cc,
        ff,
        single_unit_cost=0,
        weapons=[],
        traits=[],
        transport_capacity=0,
        damage_capacity=1,
    ):
        self.name = name
        self.strategy_rating = strategy_rating
        self.initiative = initiative
        self.type = type
        self.speed = speed
        self.armour = armour
        self.cc = cc
        self.ff = ff
        self.transport_capacity = transport_capacity
        self.damage_capacity = damage_capacity
        self.single_unit_cost = single_unit_cost
        self.weapons = weapons
        self.traits = traits

    def to_list(self):
        return [
            self.name,
            unit_type_to_string(self.type),
            self.speed,
            self.armour,
            self.cc,
            self.ff,
        ]

    def traits_to_str(self):
        return ", ".join(map(trait_to_string, self.traits))


class Army:
    name: str
    units: list["Unit"]
    # strategy_rating: int
    # initiative: int

    def __init__(self, name=""):
        self.name = name
        self.units = []
        # self.strategy_rating = strategy_rating
        # self.initiative = initiative

    def add_unit(self, unit: Unit):
        if not hasattr(self, "units") or self.units is None:
            self.units = []
        self.units.append(unit)

    def get_sorted_units(self):
        if not hasattr(self, "units") or self.units is None:
            return []
        return sorted(self.units, key=lambda unit: unit.type.value)


class Traits(Enum):
    EXTRA_ATTACK_1 = 1
    EXTRA_ATTACK_2 = 2
    EXTRA_ATTACK_3 = 3
    INDIRECT = 4
    SINGLE_SHOT = 5
    IGNORE_COVER = 6
    FIXED_FORWARD = 7
    RIENFORCED_ARMOUR = 8
    TELEPORT = 9
    THICK_REAR_ARMOUR = 10
    MW = 11
    ASTARTES = 12
    JUMP_PACKS = 13
    SCOUT = 14
    INFILTRQATOR = 15
    MOUNTED = 16
    FIRST_STRIKE = 17
    WALKER = 18
    PLANETFALL = 19
    TITAN_KILLER_D3 = 20
    TITAN_KILLER_1 = 21
    VOID_SHIELDS = 22
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


def trait_to_string(trait):
    """
    Maps a Traits enum value to a human-readable string.
    """
    mapping = {
        Traits.EXTRA_ATTACK_1: "Extra Attack +1",
        Traits.EXTRA_ATTACK_2: "Extra Attack +2",
        Traits.EXTRA_ATTACK_3: "Extra Attack +3",
        Traits.INDIRECT: "Indirect",
        Traits.SINGLE_SHOT: "Single Shot",
        Traits.IGNORE_COVER: "Ignore Cover",
        Traits.FIXED_FORWARD: "Fixed Forward",
        Traits.RIENFORCED_ARMOUR: "Reinforced Armour",
        Traits.TELEPORT: "Teleport",
        Traits.THICK_REAR_ARMOUR: "Thick Rear Armour",
        Traits.MW: "Macro-Weapon",
        Traits.ASTARTES: "Astartes",
        Traits.JUMP_PACKS: "Jump Packs",
        Traits.SCOUT: "Scout",
        Traits.INFILTRQATOR: "Infiltrator",
        Traits.MOUNTED: "Mounted",
        Traits.FIRST_STRIKE: "First Strike",
        Traits.WALKER: "Walker",
        Traits.PLANETFALL: "Planetfall",
        Traits.TITAN_KILLER_D3: "Titan Killer (D3)",
        Traits.VOID_SHIELDS: "Void Shields",
        Traits.DISRUPT: "Disrupt",
        Traits.FEARLESS: "Fearless",
        Traits.SKIMMER: "Skimmer",
        Traits.LANCE: "Lance",
        Traits.SUPREME_COMMANDER: "Supreme Commander",
        Traits.LEADER: "Leader",
        Traits.COMMANDER: "Commander",
        Traits.INVULNERABLE_SAVE: "Invulnerable Save",
        Traits.SLOW_FIRING: "Slow Firing",
        Traits.REAR: "Rear",
        Traits.FxF: "FxF",
    }
    return mapping.get(trait, str(trait))


class RangedWeapon:
    name: str
    range: int
    at: int
    ap: int
    aa: int
    bp: int
    mw: int
    traits: list[Traits]

    def __init__(self, range, at=0, ap=0, aa=0, bp=0, traits=[], mw=0, name="--"):
        self.name = name
        self.range = range
        self.at = at
        self.ap = ap
        self.aa = aa
        self.bp = bp
        self.mw = mw
        self.traits = traits

    def to_list(self):
        parts = []
        if self.at > 0:
            parts.append(f"AT{self.at}+")
        if self.ap > 0:
            parts.append(f"AP{self.ap}+")
        if self.mw > 0:
            parts.append(f"MW{self.mw}+")
        if self.aa > 0:
            parts.append(f"AA{self.aa}+")
        if self.bp > 0:
            parts.append(f"{self.bp}BP")
        firepower = " ".join(parts)
        traits_str = ", ".join(map(trait_to_string, self.traits))
        if firepower and traits_str:
            firepower = f"{firepower}, {traits_str}"
        elif traits_str:
            firepower = traits_str
        return [
            self.name,
            self.range,
            firepower,
        ]


class AssaultWeapon:
    name: str
    traits: list[Traits]

    def __init__(self, traits=[], name="--"):
        self.name = name
        self.traits = traits

    def to_list(self):
        return [
            self.name,
            "(base contact)",
            ", ".join(map(trait_to_string, self.traits)),
        ]


class SmallArms:
    name: str
    traits: list[Traits]

    def __init__(self, traits=[], name="Small Arms"):
        self.name = name
        self.traits = traits

    def to_list(self):
        return [
            self.name,
            "(15cm)",
            ", ".join(map(trait_to_string, self.traits)),
        ]
