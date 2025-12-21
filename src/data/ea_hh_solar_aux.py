from data.models import RangedWeapon, SmallArms, Traits, UnitType, Unit, AssaultWeapon

leman_russ_bh = Unit(
    "Leman Russ (Battle cannon + H.B.)",
    3,
    2,
    UnitType.ARMORED_VEHICLE,
    speed=25,
    armour=4,
    cc=6,
    ff=4,
    weapons=[RangedWeapon(75, ap=4, at=4), RangedWeapon(30, ap=5)],
    traits=[Traits.RIENFORCED_ARMOUR],
    single_unit_cost=350 / 6,
)
leman_russ_bl = Unit(
    "Leman Russ (Battle cannon + Las)",
    3,
    2,
    UnitType.ARMORED_VEHICLE,
    speed=25,
    armour=4,
    cc=6,
    ff=5,
    weapons=[RangedWeapon(75, ap=4, at=4), RangedWeapon(45, at=5)],
    traits=[Traits.RIENFORCED_ARMOUR],
    single_unit_cost=350 / 6,
)
leman_russ_vh = Unit(
    "Leman Russ (Vanquisher + H.B.)",
    3,
    2,
    UnitType.ARMORED_VEHICLE,
    speed=25,
    armour=4,
    cc=6,
    ff=4,
    weapons=[RangedWeapon(75, ap=6, at=3), RangedWeapon(30, ap=5)],
    traits=[Traits.RIENFORCED_ARMOUR],
    single_unit_cost=350 / 6,
)
leman_russ_vl = Unit(
    "Leman Russ (Vanquisher + Las)",
    3,
    2,
    UnitType.ARMORED_VEHICLE,
    speed=25,
    armour=4,
    cc=6,
    ff=5,
    weapons=[RangedWeapon(75, ap=6, at=3), RangedWeapon(45, at=5)],
    traits=[Traits.RIENFORCED_ARMOUR],
    single_unit_cost=350 / 6,
)
leman_russ_annihilator = Unit(
    "Leman Russ (Annihilator)",
    3,
    2,
    UnitType.ARMORED_VEHICLE,
    speed=25,
    armour=4,
    cc=6,
    ff=5,
    weapons=[RangedWeapon(45, at=5), RangedWeapon(45, at=5), RangedWeapon(45, at=5)],
    traits=[Traits.RIENFORCED_ARMOUR],
    single_unit_cost=350 / 6,
)
leman_russ_demolisher = Unit(
    "Leman Russ (Demolisher)",
    3,
    2,
    UnitType.ARMORED_VEHICLE,
    speed=25,
    armour=4,
    cc=6,
    ff=5,
    weapons=[
        RangedWeapon(30, ap=3, at=4, traits=[Traits.IGNORE_COVER, Traits.DISRUPT]),
        SmallArms([Traits.IGNORE_COVER]),
        RangedWeapon(45, at=5),
    ],
    traits=[Traits.RIENFORCED_ARMOUR],
    single_unit_cost=350 / 6,
)
leman_russ_executioner = Unit(
    "Leman Russ (Executioner)",
    3,
    2,
    UnitType.ARMORED_VEHICLE,
    speed=25,
    armour=4,
    cc=6,
    ff=4,
    weapons=[
        RangedWeapon(30, ap=4, at=4, traits=[]),  # TODO: fleshbane
        RangedWeapon(45, at=5),
    ],
    traits=[Traits.RIENFORCED_ARMOUR],
    single_unit_cost=350 / 6,
)
leman_russ_exterminator = Unit(
    "Leman Russ (Exterminator)",
    3,
    2,
    UnitType.ARMORED_VEHICLE,
    speed=25,
    armour=4,
    cc=6,
    ff=4,
    weapons=[
        RangedWeapon(45, ap=4, at=5, traits=[]),  # TODO: fleshbane
        RangedWeapon(45, at=5),
    ],
    traits=[Traits.RIENFORCED_ARMOUR],
    single_unit_cost=350 / 6,
)

malcador_a = Unit(
    "Malcador (battle cannon, demiólisher, las.spon.)",
    3,
    2,
    UnitType.ARMORED_VEHICLE,
    speed=15,
    armour=4,
    cc=6,
    ff=5,
    weapons=[
        RangedWeapon(75, ap=4, at=4),
        RangedWeapon(30, ap=3, at=4, traits=[Traits.DISRUPT, Traits.IGNORE_COVER]),
        RangedWeapon(45, at=5),
        RangedWeapon(45, at=5),
    ],
    traits=[Traits.RIENFORCED_ARMOUR, Traits.THICK_REAR_ARMOUR],
    single_unit_cost=100,
)

malcador_b = Unit(
    "Malcador (vanquisher, demiólisher, h.b.spon.)",
    3,
    2,
    UnitType.ARMORED_VEHICLE,
    speed=15,
    armour=4,
    cc=6,
    ff=4,
    weapons=[
        RangedWeapon(75, ap=6, at=3),
        RangedWeapon(30, ap=3, at=4, traits=[Traits.DISRUPT, Traits.IGNORE_COVER]),
        RangedWeapon(30, ap=5),
        RangedWeapon(30, ap=5),
    ],
    traits=[Traits.RIENFORCED_ARMOUR, Traits.THICK_REAR_ARMOUR],
    single_unit_cost=100,
)

malcador_c = Unit(
    "Malcador (las cannons)",
    3,
    2,
    UnitType.ARMORED_VEHICLE,
    speed=15,
    armour=4,
    cc=6,
    ff=5,
    weapons=[
        RangedWeapon(45, at=5),
        RangedWeapon(45, at=5),
        RangedWeapon(45, at=5),
        RangedWeapon(45, at=5),
        RangedWeapon(45, at=5),
    ],
    traits=[Traits.RIENFORCED_ARMOUR, Traits.THICK_REAR_ARMOUR],
    single_unit_cost=70,
)

ea_hh_solar_aux = [
    leman_russ_bl,
    leman_russ_bh,
    leman_russ_vl,
    leman_russ_vh,
    leman_russ_annihilator,
    leman_russ_demolisher,
    leman_russ_exterminator,
    leman_russ_executioner,
    malcador_a,
    malcador_b,
    malcador_c,
]
