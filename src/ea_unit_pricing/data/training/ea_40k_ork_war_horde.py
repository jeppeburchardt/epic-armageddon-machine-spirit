from ea_unit_pricing.domain import (
    AircraftSpeed,
    AssaultWeapon,
    Multiplier,
    RangedWeapon,
    Traits,
    Unit,
    UnitType,
)

battle_wagon = Unit(
    "Battle Wagon",
    3,
    3,
    UnitType.ARMORED_VEHICLE,
    speed=30,
    armour=5,
    cc=6,
    ff=5,
    weapons=[RangedWeapon(30, ap=5, at=6), RangedWeapon(30, ap=5, at=6)],
    transport_capacity=2,
    single_unit_cost=25,
)

deth_kopta = Unit(
    "Deth Kopta",
    3,
    3,
    UnitType.LIGHT_VEHICLE,
    speed=35,
    armour=4,
    cc=6,
    ff=5,
    weapons=[
        RangedWeapon(30, ap=5, at=6),
    ],
    traits=[Traits.SKIMMER],
    single_unit_cost=35,
)

warbuggy = Unit(
    "Warbuggy",
    3,
    3,
    UnitType.LIGHT_VEHICLE,
    speed=35,
    armour=5,
    cc=5,
    ff=5,
    weapons=[RangedWeapon(30, ap=5, at=6)],
    single_unit_cost=25,
)

warbikes = Unit(
    "Warbikes",
    3,
    3,
    UnitType.INFANTRY,
    speed=35,
    armour=5,
    cc=4,
    ff=6,
    weapons=[RangedWeapon(15, ap=5, at=5)],
    single_unit_cost=25,
)

gunwagon = Unit(
    "Gunwagon",
    3,
    3,
    UnitType.ARMORED_VEHICLE,
    speed=30,
    armour=5,
    cc=5,
    ff=5,
    weapons=[RangedWeapon(45, ap=5, at=5)],
    transport_capacity=1,
    single_unit_cost=35,
)

flakwagon = Unit(
    "Flakwagon",
    3,
    3,
    UnitType.ARMORED_VEHICLE,
    speed=30,
    armour=5,
    cc=5,
    ff=5,
    weapons=[RangedWeapon(30, ap=6, at=6, aa=6)],
    transport_capacity=1,
    single_unit_cost=35,
)

gun_fortress = Unit(
    "Gun Fortress",
    3,
    3,
    UnitType.WAR_ENGINE,
    speed=30,
    armour=4,
    cc=4,
    ff=4,
    weapons=[
        RangedWeapon(30, ap=5, at=6),
        RangedWeapon(30, ap=5, at=6),
        RangedWeapon(30, ap=5, at=6),
        RangedWeapon(30, ap=5, at=6),
        RangedWeapon(30, ap=5, at=6),
        RangedWeapon(45, ap=5, at=5),
        RangedWeapon(45, ap=5, at=5),
        RangedWeapon(45, ap=5, at=5),
    ],
    damage_capacity=3,
    transport_capacity=4,
    single_unit_cost=125,
)

battle_fortress = Unit(
    "Battle Fortress",
    3,
    3,
    UnitType.WAR_ENGINE,
    speed=30,
    armour=4,
    cc=4,
    ff=4,
    weapons=[
        RangedWeapon(30, ap=5, at=6),
        RangedWeapon(30, ap=5, at=6),
        RangedWeapon(30, ap=5, at=6),
        RangedWeapon(30, ap=5, at=6),
        RangedWeapon(45, ap=5, at=5),
    ],
    damage_capacity=3,
    transport_capacity=8,
    single_unit_cost=115,
)

dreadnought = Unit(
    "Ork Dreadnought",
    3,
    3,
    UnitType.ARMORED_VEHICLE,
    speed=15,
    armour=4,
    cc=4,
    ff=5,
    weapons=[
        RangedWeapon(30, ap=6, at=6),
        RangedWeapon(30, ap=6, at=6),
        AssaultWeapon([Traits.EXTRA_ATTACK_1, Traits.MW]),
    ],
    traits=[Traits.WALKER],
    single_unit_cost=35,
)

killer_kan = Unit(
    "Killer Kan",
    3,
    3,
    UnitType.ARMORED_VEHICLE,
    speed=15,
    armour=5,
    cc=5,
    ff=6,
    weapons=[
        RangedWeapon(30, ap=6, at=6),
        AssaultWeapon([Traits.EXTRA_ATTACK_1, Traits.MW]),
    ],
    traits=[Traits.WALKER],
    single_unit_cost=25,
)

stompa = Unit(
    "Stompa",
    3,
    3,
    UnitType.ARMORED_VEHICLE,
    speed=15,
    armour=4,
    cc=4,
    ff=4,
    weapons=[
        RangedWeapon(45, ap=5, at=5),
        RangedWeapon(45, ap=5, at=5),
        RangedWeapon(30, ap=5, at=6),
        AssaultWeapon([Traits.EXTRA_ATTACK_1, Traits.MW]),
    ],
    single_unit_cost=50,
)

fighta_bommer = Unit(
    "Fighta Bommer",
    3,
    3,
    UnitType.AIRCRAFT,
    speed=200,
    armour=6,
    cc=0,
    ff=0,
    weapons=[RangedWeapon(15, ap=5, aa=5), RangedWeapon(30, at=4)],
    aircraft_speed=AircraftSpeed.FIGHTER,
    single_unit_cost=50,
)

landa = Unit(
    "Landa",
    3,
    3,
    UnitType.AIRCRAFT_WAR_ENGINE,
    speed=200,
    armour=5,
    cc=6,
    ff=4,
    weapons=[
        Multiplier(6, RangedWeapon(15, ap=5, aa=5)),
        Multiplier(2, RangedWeapon(30, at=4, traits=[Traits.FIXED_FORWARD])),
    ],
    single_unit_cost=200,
    damage_capacity=3,
    traits=[Traits.PLANET_FALL, Traits.REINFORCED_ARMOUR],
    aircraft_speed=AircraftSpeed.BOMBER,
)


ea_40k_ork_war_horde = [
    battle_wagon,
    deth_kopta,
    warbikes,
    warbuggy,
    gunwagon,
    flakwagon,
    battle_fortress,
    gun_fortress,
    dreadnought,
    killer_kan,
    stompa,
    fighta_bommer,
    landa,
]
