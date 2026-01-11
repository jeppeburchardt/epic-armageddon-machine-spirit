from data.models import Unit, RangedWeapon, AssaultWeapon, Traits, UnitType, SmallArms

tactical_marines = Unit(
    "Tactical Marines",
    5,
    1,
    UnitType.INFANTRY,
    15,
    4,
    4,
    4,
    275 / 6,
    [RangedWeapon(45, 6, 5)],
    [Traits.ASTARTES],
)

# tactical_marines_captain = Unit(
#     "Tactical Marines Captain",
#     5,
#     1,
#     UnitType.INFANTRY,
#     speed=15,
#     armour=4,
#     cc=4,
#     ff=4,
#     weapons=[RangedWeapon(45, 6, 5), AssaultWeapon([Traits.EXTRA_ATTACK_1, Traits.MW])],
#     traits=[Traits.ASTARTES, Traits.COMMANDER, Traits.LEADER, Traits.INVULNERABLE_SAVE],
#     single_unit_cost=(275 / 6) + 50,
# )

# tactical_marines_supreme_commander = Unit(
#     "Tactical Marines Supreme Commander",
#     5,
#     1,
#     UnitType.INFANTRY,
#     speed=15,
#     armour=4,
#     cc=4,
#     ff=4,
#     weapons=[RangedWeapon(45, 6, 5), AssaultWeapon([Traits.EXTRA_ATTACK_1, Traits.MW])],
#     traits=[
#         Traits.ASTARTES,
#         Traits.COMMANDER,
#         Traits.LEADER,
#         Traits.INVULNERABLE_SAVE,
#         Traits.SUPREME_COMMANDER,
#     ],
#     single_unit_cost=(275 / 6) + 100,
# )

terminators = Unit(
    "Terminators",
    5,
    1,
    UnitType.INFANTRY,
    15,
    4,
    4,
    3,
    350 / 4,
    [
        RangedWeapon(30, 5, 5),
        RangedWeapon(30, 5, 5),
        AssaultWeapon([Traits.EXTRA_ATTACK_1, Traits.MW]),
    ],
    [
        Traits.TELEPORT,
        Traits.RIENFORCED_ARMOUR,
        Traits.THICK_REAR_ARMOUR,
        Traits.ASTARTES,
    ],
)

assualt = Unit(
    "Assualt Squad",
    5,
    1,
    UnitType.INFANTRY,
    30,
    4,
    3,
    5,
    175 / 4,
    [SmallArms()],
    [Traits.ASTARTES, Traits.JUMP_PACKS],
)

scout = Unit(
    "Scout Squad",
    5,
    1,
    UnitType.INFANTRY,
    15,
    5,
    4,
    5,
    150 / 4,
    [RangedWeapon(30, 0, 5)],
    [Traits.ASTARTES, Traits.SCOUT, Traits.INFILTRQATOR],
)

devastator = Unit(
    "Devastator Squad",
    5,
    1,
    UnitType.INFANTRY,
    15,
    4,
    5,
    3,
    250 / 4,
    [RangedWeapon(45, 6, 5), RangedWeapon(45, 6, 5)],
    [Traits.ASTARTES],
)

bike = Unit(
    "Bike Squad",
    5,
    1,
    UnitType.INFANTRY,
    35,
    4,
    3,
    5,
    200 / 5,
    weapons=[SmallArms()],
    traits=[Traits.ASTARTES, Traits.MOUNTED],
)

predator_annihilator = Unit(
    "Predator Annihilator",
    5,
    1,
    UnitType.ARMORED_VEHICLE,
    30,
    4,
    6,
    5,
    250 / 4,
    [RangedWeapon(45, 4, 0), RangedWeapon(45, 5, 0), RangedWeapon(45, 5, 0)],
    [Traits.ASTARTES],
)

predator_destructor = Unit(
    "Predator Destructor",
    5,
    1,
    UnitType.ARMORED_VEHICLE,
    30,
    4,
    6,
    3,
    250 / 4,
    [RangedWeapon(45, 6, 5), RangedWeapon(30, 0, 5), RangedWeapon(30, 0, 5)],
    [Traits.ASTARTES],
)

landraider = Unit(
    "Land Raider",
    5,
    1,
    UnitType.ARMORED_VEHICLE,
    30,
    4,
    6,
    4,
    325 / 4,
    [RangedWeapon(45, 4, 0), RangedWeapon(45, 4, 0), RangedWeapon(30, 0, 4)],
    [Traits.ASTARTES, Traits.RIENFORCED_ARMOUR, Traits.THICK_REAR_ARMOUR],
    2,
)

dreadnought_a = Unit(
    "Dreadnought (missile + lascannons)",
    5,
    1,
    UnitType.ARMORED_VEHICLE,
    15,
    3,
    4,
    4,
    50,
    [RangedWeapon(45, 6, 5), RangedWeapon(30, 4, 0)],
    [Traits.WALKER, Traits.ASTARTES],
)

dreadnought_b = Unit(
    "Dreadnought (power fist + assault cannon)",
    5,
    1,
    UnitType.ARMORED_VEHICLE,
    15,
    3,
    4,
    4,
    50,
    [RangedWeapon(30, 5, 5), AssaultWeapon([Traits.EXTRA_ATTACK_1, Traits.MW])],
    [Traits.WALKER, Traits.ASTARTES],
)

razorback_a = Unit(
    "Razorback (lascannons)",
    5,
    1,
    UnitType.ARMORED_VEHICLE,
    30,
    5,
    6,
    5,
    25,
    [RangedWeapon(45, 4, 0)],
    [Traits.ASTARTES],
    1,
)

razorback_b = Unit(
    "Razorback (heavy bolter)",
    5,
    1,
    UnitType.ARMORED_VEHICLE,
    30,
    5,
    6,
    4,
    25,
    [RangedWeapon(30, 0, 5)],
    [Traits.ASTARTES],
    1,
)

vindicator = Unit(
    "Vindicator",
    5,
    1,
    UnitType.ARMORED_VEHICLE,
    25,
    4,
    6,
    4,
    225 / 4,
    [RangedWeapon(30, 4, 3, 0, 0, [Traits.IGNORE_COVER])],
    [Traits.ASTARTES, Traits.WALKER],
)

whirlwind = Unit(
    "Whirlwind",
    5,
    1,
    UnitType.ARMORED_VEHICLE,
    30,
    5,
    6,
    5,
    275 / 4,
    [RangedWeapon(45, bp=1, traits=[Traits.INDIRECT])],
    [Traits.ASTARTES],
)

thunderhawk_gunship = Unit(
    "Thunderhawk Gunship",
    5,
    1,
    UnitType.AIRCRAFT_WAR_ENGINE,
    200,
    4,
    6,
    4,
    200,
    [
        RangedWeapon(75, 4, 4),
        RangedWeapon(30, 4, 0, 5),
        RangedWeapon(30, 4, 0, 5),
        RangedWeapon(30, 4, 0, 5),
        RangedWeapon(30, 4, 0, 5),
    ],
    [Traits.ASTARTES, Traits.RIENFORCED_ARMOUR, Traits.PLANETFALL],
    8,
    2,
)

imp_fists_fellblade = Unit(
    "Imperial Fists Fellblade",
    5,
    1,
    UnitType.WAR_ENGINE,
    speed=15,
    armour=4,
    cc=6,
    ff=4,
    damage_capacity=4,
    single_unit_cost=325,
    traits=[Traits.ASTARTES, Traits.RIENFORCED_ARMOUR],
    weapons=[
        RangedWeapon(75, mw=3),
        RangedWeapon(75, mw=3),
        RangedWeapon(45, at=4),
        RangedWeapon(45, at=4),
        RangedWeapon(45, at=4),
        RangedWeapon(45, at=4),
        RangedWeapon(30, at=4, ap=3, traits=[Traits.IGNORE_COVER]),
        RangedWeapon(30, ap=4),
    ],
)

imp_fists_tarantula_a = Unit(
    "Tarantula Platform",
    5,
    1,
    UnitType.LIGHT_VEHICLE,
    speed=0,
    armour=6,
    cc=6,
    ff=6,
    weapons=[RangedWeapon(45, at=4)],
    single_unit_cost=25,
)


imp_fists_tarantula_b = Unit(
    "Tarantula Platform",
    5,
    1,
    UnitType.LIGHT_VEHICLE,
    speed=0,
    armour=6,
    cc=6,
    ff=5,
    weapons=[RangedWeapon(30, ap=4)],
    single_unit_cost=25,
)
land_speeder = Unit(
    "Land Speeder",
    5,
    1,
    UnitType.LIGHT_VEHICLE,
    speed=35,
    armour=4,
    cc=6,
    ff=5,
    weapons=[RangedWeapon(15, mw=5), SmallArms([Traits.MW])],
    traits=[Traits.SKIMMER, Traits.ASTARTES, Traits.SCOUT],
    single_unit_cost=40,
)

land_speeder_tornado = Unit(
    "Land Speeder Tornado",
    5,
    1,
    UnitType.LIGHT_VEHICLE,
    speed=35,
    armour=4,
    cc=6,
    ff=5,
    weapons=[
        RangedWeapon(30, ap=5, at=5),
        RangedWeapon(30, ap=5),
    ],
    traits=[Traits.ASTARTES, Traits.SKIMMER, Traits.SCOUT],
    single_unit_cost=40,
)

land_speeder_typhoon = Unit(
    "Land Speeder Typhoon",
    5,
    1,
    UnitType.LIGHT_VEHICLE,
    speed=35,
    armour=4,
    cc=6,
    ff=5,
    weapons=[
        RangedWeapon(45, ap=3, at=5),
        RangedWeapon(30, ap=5),
    ],
    traits=[Traits.ASTARTES, Traits.SKIMMER, Traits.SCOUT],
    single_unit_cost=40,
)

ea_40k_astartes_units = [
    tactical_marines,
    # tactical_marines_captain,
    # tactical_marines_supreme_commander,
    terminators,
    assualt,
    scout,
    devastator,
    land_speeder,
    land_speeder_tornado,
    land_speeder_typhoon,
    predator_annihilator,
    predator_destructor,
    landraider,
    dreadnought_a,
    dreadnought_b,
    razorback_a,
    razorback_b,
    vindicator,
    whirlwind,
    thunderhawk_gunship,
    imp_fists_fellblade,
    imp_fists_tarantula_a,
    imp_fists_tarantula_b,
]
