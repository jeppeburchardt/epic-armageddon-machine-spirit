from data.models import Unit, RangedWeapon, AssaultWeapon, Traits, UnitType, SmallArms

marauder = Unit(
    "Marauder Bomber",
    2,
    2,
    UnitType.AIRCRAFT,
    200,
    4,
    0,
    0,
    125,
    [
        RangedWeapon(45, 4, 0, 4),
        RangedWeapon(15, 0, 0, 0, 3),
        RangedWeapon(15, 0, 0, 5),
        RangedWeapon(15, 0, 0, 5),
    ],
    [],
)

thunderbolt = Unit(
    "Thunderbolt Fighter",
    2,
    2,
    UnitType.AIRCRAFT,
    200,
    6,
    0,
    0,
    75,
    [RangedWeapon(30, 6, 5, 5), RangedWeapon(30, 4, 0), RangedWeapon(15, 0, 4, 5)],
    [],
)

ea_40k_imperial_navy_units = [
    marauder,
    thunderbolt,
]
