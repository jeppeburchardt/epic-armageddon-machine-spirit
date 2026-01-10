from enum import Enum


class UnitType(Enum):
    CHARACTER = 0
    INFANTRY = 1
    LIGHT_VEHICLE = 2
    ARMORED_VEHICLE = 3
    AIRCRAFT = 4
    WAR_ENGINE = 5
    AIRCRAFT_WAR_ENGINE = 6


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
        single_unit_cost,
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
    VOID_SHIELDS = 21
    DISRUPT = 22
    FEARLESS = 23
    SKIMMER = 24
    LANCE = 25
    SUPREME_COMMANDER = 26
    LEADER = 27
    COMMANDER = 28
    INVULNERABLE_SAVE = 29
    SLOW_FIRING = 30
    REAR = 31
    FxF = 32


class RangedWeapon:
    range: int
    at: int
    ap: int
    aa: int
    bp: int
    mw: int
    traits: list[Traits]

    def __init__(self, range, at=0, ap=0, aa=0, bp=0, traits=[], mw=0):
        self.range = range
        self.at = at
        self.ap = ap
        self.aa = aa
        self.bp = bp
        self.mw = mw
        self.traits = traits


class AssaultWeapon:
    traits: list[Traits]

    def __init__(self, traits=[]):
        self.traits = traits


class SmallArms:
    traits: list[Traits]

    def __init__(self, traits=[]):
        self.traits = traits
