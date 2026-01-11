from data.models import Unit, RangedWeapon, AssaultWeapon, Traits, UnitType, SmallArms

boys = Unit(
    "Ork Boyz", 3, 3, UnitType.INFANTRY, 15, 5, 4, 6, 25, [RangedWeapon(30, ap=6, at=6)]
)

nobz = Unit(
    "Ork Nobz",
    3,
    3,
    UnitType.INFANTRY,
    15,
    4,
    3,
    5,
    35,
    [RangedWeapon(30, ap=6, at=6), AssaultWeapon([Traits.EXTRA_ATTACK_1])],
)

squig_katapult = Unit(
    "Squig Katapult",
    3,
    3,
    UnitType.INFANTRY,
    10,
    0,
    6,
    5,
    25,
    [RangedWeapon(15, bp=1, traits=[Traits.DISRUPT])],
)

squiggoth = Unit(
    "Squiggoth",
    3,
    3,
    UnitType.LIGHT_VEHICLE,
    20,
    4,
    4,
    5,
    50,
    [
        RangedWeapon(45, ap=5, at=5),
        RangedWeapon(30, ap=5, at=6),
        RangedWeapon(30, ap=5, at=6),
        AssaultWeapon([Traits.MW, Traits.EXTRA_ATTACK_2]),  # TODO: D3 extra attacks
    ],
    transport_capacity=4,
    traits=[Traits.REINFORCED_ARMOUR, Traits.THICK_REAR_ARMOUR],
)

orkeosaurus = Unit(
    "Orkeosaurus",
    3,
    3,
    UnitType.WAR_ENGINE,
    15,
    4,
    5,
    4,
    175,
    [
        RangedWeapon(45, ap=5, at=5),
        RangedWeapon(45, ap=5, at=5),
        RangedWeapon(30, ap=5, at=6),
        RangedWeapon(30, ap=5, at=6),
        RangedWeapon(30, ap=5, at=6),
        RangedWeapon(30, ap=5, at=6),
        AssaultWeapon([Traits.MW, Traits.EXTRA_ATTACK_2]),  # TODO: D3 extra attacks
    ],
    damage_capacity=6,
    transport_capacity=12,
    traits=[Traits.REINFORCED_ARMOUR, Traits.THICK_REAR_ARMOUR],
)

steam_gargant = Unit(
    "Steam Gargant",
    3,
    3,
    UnitType.WAR_ENGINE,
    15,
    4,
    4,
    4,
    200,
    [
        RangedWeapon(60, bp=2, traits=[Traits.MW]),
        AssaultWeapon([Traits.EXTRA_ATTACK_1, Traits.TITAN_KILLER_D3]),
        RangedWeapon(45, mw=5, aa=5, traits=[Traits.MW]),
    ],
    damage_capacity=4,
    traits=[Traits.FEARLESS, Traits.REINFORCED_ARMOUR, Traits.WALKER],
)

ea_40k_feral_orks = [
    boys,
    nobz,
    squig_katapult,
    squig_katapult,
    squiggoth,
    orkeosaurus,
    steam_gargant,
]
