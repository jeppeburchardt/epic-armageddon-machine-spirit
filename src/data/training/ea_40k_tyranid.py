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

tyranids = Army("Hive Fleet Onachus Tyranid")
# TODO: Brood and Synapse traits are not added to training set

tyranids.add_unit(
    Unit(
        "Hormagaunts",
        1,
        1,
        UnitType.INFANTRY,
        speed=20,
        cc=3,
        traits=[Traits.EXPENDABLE, Traits.INFILTRATOR],
        single_unit_cost=15,
    )
)

tyranids.add_unit(
    Unit(
        "Termagants",
        1,
        1,
        UnitType.INFANTRY,
        speed=20,
        cc=6,
        ff=5,
        traits=[Traits.EXPENDABLE],
        weapons=[SmallArms()],
        single_unit_cost=15,
    )
)

tyranids.add_unit(
    Unit(
        "Gargoyles",
        1,
        1,
        UnitType.INFANTRY,
        speed=30,
        cc=6,
        ff=5,
        weapons=[SmallArms([Traits.IGNORE_COVER])],
        traits=[Traits.EXPENDABLE, Traits.JUMP_PACKS],
        single_unit_cost=20,
    )
)

tyranids.add_unit(
    Unit(
        "Raveners",
        1,
        1,
        UnitType.INFANTRY,
        speed=20,
        armour=5,
        cc=4,
        weapons=[AssaultWeapon([Traits.EXTRA_ATTACK_1])],
        traits=[Traits.INFILTRATOR, Traits.EXPENDABLE, Traits.TUNNELER],
        single_unit_cost=30,
    )
)

tyranids.add_unit(
    Unit(
        "Genestealers",
        1,
        1,
        UnitType.INFANTRY,
        speed=20,
        armour=6,
        cc=2,
        weapons=[AssaultWeapon([Traits.FIRST_STRIKE])],
        traits=[Traits.INFILTRATOR, Traits.SCOUT],
        single_unit_cost=20,
    )
)

tyranids.add_unit(
    Unit(
        "Carnifix",
        1,
        1,
        UnitType.ARMORED_VEHICLE,
        speed=20,
        armour=4,
        cc=6,
        ff=5,
        weapons=[SmallArms(), AssaultWeapon([Traits.EXTRA_ATTACK_1, Traits.MW])],
        traits=[Traits.FEARLESS, Traits.REINFORCED_ARMOUR],
        single_unit_cost=50,
    )
)

tyranids.add_unit(
    Unit(
        "Tyranid Warriors",
        1,
        1,
        UnitType.INFANTRY,
        speed=20,
        armour=5,
        cc=2,
        ff=5,
        weapons=[RangedWeapon(30, ap=5)],
        traits=[Traits.FEARLESS],
        single_unit_cost=50,
    )
)
