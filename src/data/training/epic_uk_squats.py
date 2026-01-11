from data.models import (
    RangedWeapon,
    SmallArms,
    Traits,
    UnitType,
    Unit,
    AssaultWeapon,
    Army,
    Multiplier,
)

squats = Army("Epic UK Squats")

squats.add_unit(
    Unit(
        "Warrior",
        2,
        2,
        UnitType.INFANTRY,
        speed=15,
        armour=6,
        cc=5,
        ff=5,
        weapons=[SmallArms(), RangedWeapon(45, ap=5, at=6)],
        single_unit_cost=25,
    )
)

squats.add_unit(
    Unit(
        "Berserkers",
        2,
        2,
        UnitType.INFANTRY,
        speed=15,
        armour=6,
        cc=5,
        ff=5,
        weapons=[SmallArms(), AssaultWeapon()],
        single_unit_cost=20,
    )
)

squats.add_unit(
    Unit(
        "Mole Mortar",
        2,
        2,
        UnitType.INFANTRY,
        speed=10,
        armour=6,
        cc=6,
        ff=6,
        weapons=[RangedWeapon(30, bp=1, traits=[Traits.INDIRECT, Traits.DISRUPT])],
        single_unit_cost=25,
    )
)

squats.add_unit(
    Unit(
        "Rapier",
        2,
        2,
        UnitType.INFANTRY,
        speed=10,
        armour=6,
        cc=6,
        ff=5,
        weapons=[RangedWeapon(45, at=4, ap=6)],
        single_unit_cost=25,
    )
)

squats.add_unit(
    Unit(
        "Light Artillery",
        2,
        2,
        UnitType.INFANTRY,
        speed=10,
        armour=6,
        cc=6,
        ff=5,
        weapons=[RangedWeapon(45, at=6, ap=4, traits=[Traits.INDIRECT])],
        single_unit_cost=25,
    )
)

squats.add_unit(
    Unit(
        "Bikers",
        2,
        2,
        UnitType.INFANTRY,
        speed=35,
        armour=5,
        cc=4,
        ff=5,
        weapons=[SmallArms()],
        traits=[Traits.MOUNTED],
        single_unit_cost=33,
    )
)

squats.add_unit(
    Unit(
        "Hearthguard",
        2,
        2,
        UnitType.INFANTRY,
        speed=15,
        armour=5,
        cc=4,
        ff=5,
        weapons=[AssaultWeapon(), RangedWeapon(30, ap=5, at=5)],
        traits=[Traits.INSPIRING, Traits.LEADER],
        single_unit_cost=25,
    )
)

squats.add_unit(
    Unit(
        "Rhino",
        2,
        2,
        UnitType.ARMORED_VEHICLE,
        30,
        armour=5,
        cc=6,
        ff=6,
        weapons=[SmallArms()],
        transport_capacity=2,
        single_unit_cost=10,
    )
)

squats.add_unit(
    Unit(
        "Iron Eagle",
        2,
        2,
        UnitType.ARMORED_VEHICLE,
        speed=35,
        armour=4,
        cc=6,
        ff=5,
        weapons=[
            Multiplier(2, RangedWeapon(45, ap=5, at=6)),
            RangedWeapon(75, ap=4, at=4),
        ],
        traits=[Traits.SCOUT, Traits.SKIMMER],
        single_unit_cost=63,
    )
)

squats.add_unit(
    Unit(
        "Overlord",
        2,
        2,
        UnitType.WAR_ENGINE,
        speed=20,
        armour=4,
        cc=0,
        ff=4,
        weapons=[
            Multiplier(3, RangedWeapon(75, ap=4, at=5, traits=[Traits.LEFT])),
            Multiplier(3, RangedWeapon(75, ap=4, at=5, traits=[Traits.RIGHT])),
            Multiplier(4, RangedWeapon(45, ap=5, at=6, traits=[Traits.FIXED_FORWARD])),
            RangedWeapon(45, aa=5),
            RangedWeapon(15, bp=2),
        ],
        traits=[Traits.REINFORCED_ARMOUR],
        damage_capacity=3,
        single_unit_cost=250,
    )
)


squats.add_unit(
    Unit(
        "Colossus",
        2,
        2,
        UnitType.WAR_ENGINE,
        speed=15,
        armour=4,
        cc=5,
        ff=4,
        weapons=[
            RangedWeapon(90, bp=3, traits=[Traits.MW, Traits.FIXED_FORWARD]),
            Multiplier(4, RangedWeapon(75, ap=4, at=4, traits=[Traits.FIXED_FORWARD])),
            RangedWeapon(
                30, ap=3, at=4, traits=[Traits.IGNORE_COVER, Traits.FIXED_FORWARD]
            ),
            Multiplier(
                4,
                RangedWeapon(
                    60,
                    bp=2,
                    traits=[Traits.FIXED_FORWARD, Traits.INDIRECT, Traits.SINGLE_SHOT],
                ),
            ),
            SmallArms(traits=[Traits.EXTRA_ATTACK_1]),
        ],
        traits=[
            Traits.FEARLESS,
            Traits.REINFORCED_ARMOUR,
            Traits.THICK_REAR_ARMOUR,
        ],
        damage_capacity=5,
        void_shields=4,
        single_unit_cost=525,
    )
)

squats.add_unit(
    Unit(
        "Cyclop",
        2,
        2,
        UnitType.WAR_ENGINE,
        speed=15,
        armour=4,
        cc=5,
        ff=4,
        weapons=[
            RangedWeapon(
                90, mw=2, traits=[Traits.TITAN_KILLER_D6, Traits.FIXED_FORWARD]
            ),
            RangedWeapon(75, ap=4, at=4),
            Multiplier(
                2,
                RangedWeapon(
                    30, ap=3, at=4, traits=[Traits.IGNORE_COVER, Traits.FIXED_FORWARD]
                ),
            ),
            Multiplier(
                6,
                RangedWeapon(
                    90, at=2, traits=[Traits.SINGLE_SHOT, Traits.FIXED_FORWARD]
                ),
            ),
            SmallArms(traits=[Traits.EXTRA_ATTACK_1]),
        ],
        traits=[
            Traits.FEARLESS,
            Traits.REINFORCED_ARMOUR,
            Traits.THICK_REAR_ARMOUR,
        ],
        damage_capacity=5,
        void_shields=4,
        single_unit_cost=525,
    )
)
