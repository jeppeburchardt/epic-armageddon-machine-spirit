from models.units import Unit, RangedWeapon, Traits, UnitType, AircraftSpeed, Multiplier

raven = Unit(
    "Raven Fighter",
    3,
    1,
    UnitType.AIRCRAFT,
    armour=4,
    cc=0,
    ff=0,
    weapons=[
        RangedWeapon(30, at=4, aa=5, traits=[Traits.FIXED_FORWARD, Traits.LANCE]),
        RangedWeapon(30, ap=5, aa=5, traits=[Traits.FIXED_FORWARD]),
    ],
    aircraft_speed=AircraftSpeed.FIGHTER,
    single_unit_cost=33.333,
)

razor = Unit(
    "Razorwing",
    3,
    1,
    UnitType.AIRCRAFT,
    armour=4,
    cc=0,
    ff=0,
    weapons=[
        RangedWeapon(
            30,
            mw=3,
            traits=[Traits.SLOW_FIRING, Traits.FIXED_FORWARD, Traits.TITAN_KILLER_1],
        ),
        Multiplier(2, RangedWeapon(30, ap=5, aa=5, traits=[Traits.FIXED_FORWARD])),
        RangedWeapon(15, ap=6, traits=[Traits.DISRUPT]),
    ],
    single_unit_cost=125,
)


ea_40k_dark_eldar_units = [raven, razor]
