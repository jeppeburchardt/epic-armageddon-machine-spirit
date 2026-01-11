from data.models import (
    RangedWeapon,
    SmallArms,
    Traits,
    UnitType,
    Unit,
    AssaultWeapon,
    Army,
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
