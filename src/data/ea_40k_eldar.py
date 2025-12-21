from data.models import Unit, RangedWeapon, AssaultWeapon, Traits, UnitType, SmallArms

dark_reapoers = Unit(
    "Dark Reapers",
    4,
    1,
    UnitType.INFANTRY,
    speed=15,
    armour=5,
    cc=6,
    ff=3,
    weapons=[
        RangedWeapon(45, ap=5),
        RangedWeapon(45, ap=5),
    ],
    traits=[],
    single_unit_cost=225 / 6,
)

dire_avengers = Unit(
    "Dire Avengers",
    4,
    1,
    UnitType.INFANTRY,
    speed=15,
    armour=5,
    cc=5,
    ff=4,
    weapons=[SmallArms([Traits.EXTRA_ATTACK_1])],
    single_unit_cost=225 / 6,
)

fire_dragons = Unit(
    "Fire Dragons",
    4,
    1,
    UnitType.INFANTRY,
    speed=15,
    armour=5,
    cc=5,
    ff=4,
    weapons=[RangedWeapon(15, mw=5), SmallArms([Traits.MW])],
    single_unit_cost=225 / 6,
)

guardians = Unit(
    "Guardians",
    4,
    1,
    UnitType.INFANTRY,
    speed=15,
    armour=0,
    cc=6,
    ff=4,
    weapons=[SmallArms()],
    single_unit_cost=150 / 8,
)

heavy_weapon_platform = Unit(
    "Heavu weapon platform",
    4,
    1,
    UnitType.INFANTRY,
    speed=15,
    armour=0,
    cc=6,
    ff=5,
    weapons=[RangedWeapon(30, ap=5, at=5)],
    single_unit_cost=50 / 3,
)

howling_banshees = Unit(
    "Howling Banshees",
    4,
    1,
    UnitType.INFANTRY,
    speed=15,
    armour=5,
    cc=2,
    ff=5,
    weapons=[SmallArms([]), AssaultWeapon([Traits.FIRST_STRIKE])],
    single_unit_cost=225 / 6,
)

# warp spiders

# swoioping hawks

jet_bike = Unit(
    "Jetbikes",
    4,
    1,
    UnitType.INFANTRY,
    speed=35,
    armour=5,
    cc=6,
    ff=4,
    weapons=[
        SmallArms(),
    ],
    traits=[Traits.MOUNTED, Traits.SKIMMER],
    single_unit_cost=200 / 6,
)

shining_spear = Unit(
    "Shining Spears",
    4,
    1,
    UnitType.INFANTRY,
    speed=35,
    armour=4,
    cc=4,
    ff=5,
    weapons=[SmallArms(), AssaultWeapon([Traits.LANCE])],
    traits=[Traits.MOUNTED, Traits.SKIMMER],
    single_unit_cost=225 / 6,
)

vyper = Unit(
    "Vyper",
    4,
    1,
    UnitType.LIGHT_VEHICLE,
    speed=35,
    armour=4,
    cc=6,
    ff=5,
    weapons=[RangedWeapon(30, ap=5, at=5)],
    traits=[Traits.SKIMMER],
    single_unit_cost=200 / 6,
)

ea_40k_eldar = [
    dark_reapoers,
    dire_avengers,
    fire_dragons,
    guardians,
    heavy_weapon_platform,
    howling_banshees,
    jet_bike,
    shining_spear,
    vyper,
]
