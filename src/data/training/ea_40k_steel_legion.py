from data.models import Unit, RangedWeapon, AssaultWeapon, Traits, UnitType, SmallArms

infantry = Unit(
    "Infantry Squad",
    2,
    2,
    UnitType.INFANTRY,
    15,
    0,
    6,
    5,
    12,
    [RangedWeapon(45, 6, 5), SmallArms()],
)
ogryns = Unit(
    "Ogryns Squad",
    2,
    2,
    UnitType.INFANTRY,
    15,
    3,
    4,
    5,
    25,
    [SmallArms(), AssaultWeapon([Traits.EXTRA_ATTACK_1, Traits.MW])],
)
leman_russ = Unit(
    "Leman Russ Battle Tank",
    2,
    2,
    UnitType.ARMORED_VEHICLE,
    20,
    4,
    6,
    4,
    65,
    [
        RangedWeapon(75, 4, 4),
        RangedWeapon(45, 5, 0),
        RangedWeapon(30, 0, 5),
        RangedWeapon(30, 0, 5),
    ],
)

rought_riders = Unit(
    "Rought Riders Squad",
    2,
    3,
    UnitType.INFANTRY,
    20,
    6,
    4,
    5,
    150 / 6,
    [SmallArms(), AssaultWeapon([Traits.EXTRA_ATTACK_1, Traits.FIRST_STRIKE])],
    [Traits.INFILTRATOR, Traits.MOUNTED],
)

storm_troopers = Unit(
    "Storm Troopers Squad",
    2,
    3,
    UnitType.INFANTRY,
    15,
    5,
    5,
    4,
    200 / 8,
    [RangedWeapon(15, 5, 5)],
)

support_squad = Unit(
    "Support Squad",
    2,
    3,
    UnitType.INFANTRY,
    15,
    0,
    6,
    4,
    100 / 4,
    [RangedWeapon(45, 6, 5), RangedWeapon(45, 6, 5)],
)

baneblade = Unit(
    "Baneblade Super Heavy Tank",
    2,
    2,
    UnitType.WAR_ENGINE,
    15,
    4,
    6,
    4,
    500 / 3,
    [
        RangedWeapon(75, 3, 3),
        RangedWeapon(75, 3, 3),
        RangedWeapon(45, 6, 5),
        RangedWeapon(30, 4, 3, traits=[Traits.IGNORE_COVER]),
        RangedWeapon(45, 5, 0),
        RangedWeapon(45, 5, 0),
        RangedWeapon(30, 0, 4),
        RangedWeapon(30, 0, 4),
        RangedWeapon(30, 0, 4),
    ],
    [Traits.REINFORCED_ARMOUR],
    0,
    3,
)

shadowsword = Unit(
    "Shadowsword Super Heavy Tank",
    2,
    2,
    UnitType.WAR_ENGINE,
    15,
    4,
    6,
    5,
    500 / 3,
    [
        RangedWeapon(90, traits=[Traits.TITAN_KILLER_D3], mw=2),
        RangedWeapon(30, ap=5),
        RangedWeapon(30, ap=5),
    ],
    [Traits.REINFORCED_ARMOUR],
    0,
    3,
)

sentinel = Unit(
    "Sentinel Walker",
    2,
    2,
    UnitType.LIGHT_VEHICLE,
    20,
    6,
    6,
    5,
    25,
    [RangedWeapon(30, at=6, ap=5)],
    [Traits.WALKER, Traits.SCOUT],
)

basilisk_a = Unit(
    "Basilisk Artillery Tank (barrage munitions)",
    2,
    2,
    UnitType.ARMORED_VEHICLE,
    20,
    5,
    6,
    5,
    225 / 3,
    [RangedWeapon(120, bp=1, traits=[Traits.INDIRECT])],
    [],
)

basilisk_b = Unit(
    "Basilisk Artillery Tank",
    2,
    2,
    UnitType.ARMORED_VEHICLE,
    20,
    5,
    6,
    5,
    225 / 3,
    [RangedWeapon(120, at=4, ap=4)],
    [],
)

bombard = Unit(
    "Bombard Artillery Tank",
    2,
    2,
    UnitType.ARMORED_VEHICLE,
    20,
    6,
    6,
    5,
    250 / 3,
    [
        RangedWeapon(45, bp=2, traits=[Traits.INDIRECT, Traits.IGNORE_COVER]),
        RangedWeapon(30, ap=5),
    ],
    [],
)

chimera = Unit(
    "Chimera Armored Transport",
    2,
    2,
    UnitType.ARMORED_VEHICLE,
    30,
    5,
    6,
    5,
    25,
    [RangedWeapon(30, ap=5, at=5), RangedWeapon(15, ap=5)],
    [],
    2,
)

ea_40k_steel_legion_units = [
    infantry,
    ogryns,
    leman_russ,
    rought_riders,
    storm_troopers,
    support_squad,
    baneblade,
    shadowsword,
    sentinel,
    basilisk_a,
    basilisk_b,
    bombard,
]
