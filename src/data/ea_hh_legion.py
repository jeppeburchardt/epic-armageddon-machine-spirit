from data.models import (
    RangedWeapon,
    SmallArms,
    Traits,
    UnitType,
    Unit,
    AssaultWeapon,
    Army,
)
from .ea_hh_weapons import (
    HeavyBolter,
    LasCannon,
    TwinLinkedLasCannon,
    QuadLasCannon,
    TwinHeavyBolter,
    VanquisherBattleCannon,
    BattleCannon,
    DemolisherCannon,
)

legiones_astartes = Army("Legiones Astartes")


legiones_astartes.add_unit(
    Unit(
        "Legion Tactical Squad",
        5,
        1,
        UnitType.INFANTRY,
        15,
        4,
        4,
        4,
        34,
        [SmallArms()],
        [Traits.ASTARTES],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Legion Assault Squad",
        strategy_rating=5,
        initiative=1,
        type=UnitType.INFANTRY,
        speed=30,
        armour=4,
        cc=3,
        ff=5,
        single_unit_cost=300 / 8,
        weapons=[SmallArms()],
        traits=[Traits.ASTARTES, Traits.JUMP_PACKS],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Legion Heavy Support Squad",
        strategy_rating=5,
        initiative=1,
        type=UnitType.INFANTRY,
        speed=15,
        armour=4,
        cc=5,
        ff=3,
        single_unit_cost=50,
        weapons=[
            SmallArms(),
            RangedWeapon(45, at=6, ap=5),
            RangedWeapon(45, at=6, ap=5),
            RangedWeapon(30, aa=6),
        ],
        traits=[Traits.ASTARTES],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Legion Tactical Support Squad",
        strategy_rating=5,
        initiative=1,
        type=UnitType.INFANTRY,
        speed=15,
        armour=4,
        cc=4,
        ff=4,
        single_unit_cost=50,
        weapons=[
            SmallArms(),
            RangedWeapon(45, ap=4, traits=[Traits.IGNORE_COVER]),
            RangedWeapon(45, ap=4, traits=[Traits.IGNORE_COVER]),
            AssaultWeapon([Traits.EXTRA_ATTACK_1, Traits.IGNORE_COVER]),
        ],
        traits=[Traits.ASTARTES],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Legion Terminator Squad",
        strategy_rating=5,
        initiative=1,
        type=UnitType.INFANTRY,
        speed=15,
        armour=4,
        cc=3,
        ff=3,
        single_unit_cost=75,
        weapons=[
            AssaultWeapon([Traits.EXTRA_ATTACK_1, Traits.MW]),
            RangedWeapon(30, ap=4, at=6),
            RangedWeapon(30, ap=4, at=6),
        ],
        traits=[Traits.ASTARTES, Traits.RIENFORCED_ARMOUR],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Legion Sicaran Battle Tank (Accelerator Cannon + Lascannons)",
        5,
        1,
        UnitType.ARMORED_VEHICLE,
        35,
        5,
        6,
        4,
        300 / 4,
        [RangedWeapon(45, 5, 4), RangedWeapon(45, 5, 4), LasCannon()],
        [Traits.ASTARTES, Traits.RIENFORCED_ARMOUR],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Legion Sicaran Battle Tank (Accelerator Cannon + Heavy Bolters)",
        5,
        1,
        UnitType.ARMORED_VEHICLE,
        35,
        5,
        6,
        3,
        300 / 4,
        [RangedWeapon(45, 5, 4), RangedWeapon(45, 5, 4), HeavyBolter()],
        [Traits.ASTARTES, Traits.RIENFORCED_ARMOUR],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Legion Sicaran Battle Tank, with Omega plasma array",
        5,
        1,
        UnitType.ARMORED_VEHICLE,
        35,
        5,
        6,
        3,
        300 / 4,
        [RangedWeapon(45, 3, 0), RangedWeapon(45, 3, 0), HeavyBolter()],
        [Traits.ASTARTES, Traits.RIENFORCED_ARMOUR],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Predator Annihilator",
        5,
        1,
        UnitType.ARMORED_VEHICLE,
        30,
        4,
        6,
        5,
        240 / 4,
        [TwinLinkedLasCannon(), LasCannon(), LasCannon()],
        [Traits.ASTARTES],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Predator Destructor",
        5,
        1,
        UnitType.ARMORED_VEHICLE,
        30,
        4,
        6,
        3,
        240 / 4,
        [RangedWeapon(45, 5, 5), HeavyBolter(), HeavyBolter()],
        [Traits.ASTARTES],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Land Raider",
        5,
        1,
        UnitType.ARMORED_VEHICLE,
        speed=25,
        armour=4,
        cc=6,
        ff=4,
        weapons=[
            TwinLinkedLasCannon(),
            TwinLinkedLasCannon(),
        ],
        traits=[Traits.ASTARTES, Traits.RIENFORCED_ARMOUR, Traits.THICK_REAR_ARMOUR],
        transport_capacity=2,
        single_unit_cost=75,
    )
)

legiones_astartes.add_unit(
    Unit(
        "Spartan Assault Tank",
        5,
        1,
        UnitType.WAR_ENGINE,
        speed=25,
        armour=4,
        cc=6,
        ff=5,
        weapons=[
            QuadLasCannon(),
            QuadLasCannon(),
            TwinHeavyBolter(),
        ],
        traits=[Traits.ASTARTES, Traits.RIENFORCED_ARMOUR, Traits.THICK_REAR_ARMOUR],
        damage_capacity=2,
        single_unit_cost=125,
        transport_capacity=4,
    )
)

legiones_astartes.add_unit(
    Unit(
        "Legion Thunderhawk Gunship",
        5,
        1,
        UnitType.AIRCRAFT_WAR_ENGINE,
        200,
        4,
        6,
        4,
        250,
        [
            RangedWeapon(45, 3, 6),
            RangedWeapon(45, 3, 6),
            RangedWeapon(45, 4, 0, 5),
            RangedWeapon(30, 0, 4),
            RangedWeapon(30, 0, 4),
            RangedWeapon(15, 0, 4),
            RangedWeapon(15, 0, 4),
        ],
        [Traits.ASTARTES, Traits.PLANETFALL, Traits.RIENFORCED_ARMOUR],
        8,
        2,
    )
)

legiones_astartes.add_unit(
    Unit(
        "Fire Raptor Gunship",
        5,
        1,
        UnitType.AIRCRAFT,
        200,
        5,
        0,
        0,
        150,
        [
            RangedWeapon(30, ap=2, at=5),
            RangedWeapon(30, ap=2, at=5),
            LasCannon(),
            LasCannon(),
            RangedWeapon(15, ap=4, aa=6),
            RangedWeapon(15, ap=4, aa=6),
        ],
        traits=[Traits.ASTARTES, Traits.RIENFORCED_ARMOUR],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Xiphon Interceptor",
        5,
        1,
        UnitType.AIRCRAFT,
        200,
        5,
        0,
        0,
        125,
        [
            RangedWeapon(30, at=4, aa=5),
            RangedWeapon(30, at=4, aa=5),
            RangedWeapon(45, at=5),
        ],
        traits=[Traits.ASTARTES],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Storm Eagle Attack Ship",
        5,
        1,
        UnitType.AIRCRAFT_WAR_ENGINE,
        200,
        5,
        6,
        5,
        125,
        [
            RangedWeapon(45, at=4),
            RangedWeapon(45, at=4),
            RangedWeapon(45, bp=1),
            RangedWeapon(30, ap=4, aa=5),
        ],
        traits=[Traits.ASTARTES, Traits.RIENFORCED_ARMOUR, Traits.PLANETFALL],
        transport_capacity=4,
        damage_capacity=1,
    )
)

legiones_astartes.add_unit(
    Unit(
        "Contemptor Dreadnought with Lascannon",
        5,
        1,
        UnitType.ARMORED_VEHICLE,
        15,
        3,
        4,
        4,
        60,
        [
            LasCannon(),
            AssaultWeapon([Traits.MW, Traits.EXTRA_ATTACK_1]),
        ],
        [Traits.ASTARTES, Traits.WALKER],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Contemptor Dreadnought with Assault Cannon",
        5,
        1,
        UnitType.ARMORED_VEHICLE,
        15,
        3,
        4,
        4,
        60,
        [
            RangedWeapon(30, 5, 4, 0, name="Assault Cannon"),
            AssaultWeapon([Traits.MW, Traits.EXTRA_ATTACK_1]),
        ],
        [Traits.ASTARTES, Traits.WALKER],
    )
)


legiones_astartes.add_unit(
    Unit(
        "Deredo Dreadnought",
        5,
        1,
        UnitType.ARMORED_VEHICLE,
        speed=15,
        armour=3,
        cc=5,
        ff=3,
        weapons=[
            RangedWeapon(30, ap=4),
            RangedWeapon(45, ap=5, at=6, traits=[Traits.DISRUPT]),
            RangedWeapon(30, aa=5),
            RangedWeapon(30, aa=5),
            RangedWeapon(45, ap=5, at=2),
            RangedWeapon(45, ap=5, at=2),
        ],
        traits=[Traits.ASTARTES, Traits.WALKER],
        single_unit_cost=100,
    )
)

# legiones_astartes.add_unit(Unit(
#     "Leviathan Dreadnought",
#     5,1,UnitType.ARMORED_VEHICLE,
#     15,
#     cc=4,
#     ff=4,
#     weapons=[ ##TODO, small arms with ap and at

#     ]
#     traits=[Traits.ASTARTES, Traits.WALKER, Traits.RIENFORCED_ARMOUR]
# )

legiones_astartes.add_unit(
    Unit(
        "Vindicator",
        5,
        1,
        UnitType.ARMORED_VEHICLE,
        speed=25,
        armour=4,
        cc=6,
        ff=4,
        weapons=[DemolisherCannon()],
        traits=[Traits.ASTARTES, Traits.WALKER],
        single_unit_cost=50,
    )
)

legiones_astartes.add_unit(
    Unit(
        "Vindicator Laser Destroyer",
        5,
        1,
        UnitType.ARMORED_VEHICLE,
        speed=25,
        armour=4,
        cc=6,
        ff=5,
        weapons=[
            RangedWeapon(60, name="Laser Destroyer Array", ap=6, at=3),
        ],
        traits=[Traits.ASTARTES, Traits.WALKER],
        single_unit_cost=70,
    )
)

legiones_astartes.add_unit(
    Unit(
        "Legion Whirlwind",
        5,
        1,
        UnitType.ARMORED_VEHICLE,
        speed=30,
        armour=5,
        cc=6,
        ff=5,
        weapons=[RangedWeapon(45, bp=1, traits=[Traits.IGNORE_COVER, Traits.INDIRECT])],
        single_unit_cost=300 / 4,
        traits=[Traits.ASTARTES],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Legion Whirlwind Scorpius",
        5,
        1,
        UnitType.ARMORED_VEHICLE,
        speed=30,
        armour=5,
        cc=6,
        ff=5,
        weapons=[
            RangedWeapon(45, ap=5, at=5, traits=[Traits.INDIRECT]),
            RangedWeapon(45, ap=5, at=5, traits=[Traits.INDIRECT]),
        ],
        single_unit_cost=300 / 4,
        traits=[Traits.ASTARTES],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Legion Mastodon Armored Transport",
        5,
        1,
        UnitType.WAR_ENGINE,
        speed=20,
        armour=4,
        cc=5,
        ff=4,
        single_unit_cost=200,
        damage_capacity=4,
        transport_capacity=8,
        weapons=[
            SmallArms([Traits.EXTRA_ATTACK_1, Traits.MW]),
            LasCannon(),
            LasCannon(),
            RangedWeapon(15, ap=4, traits=[Traits.IGNORE_COVER]),
            RangedWeapon(15, ap=4, traits=[Traits.IGNORE_COVER]),
            RangedWeapon(30, ap=4, at=4, aa=5),
            RangedWeapon(30, ap=4, at=4, aa=5),
        ],
        traits=[Traits.ASTARTES, Traits.RIENFORCED_ARMOUR, Traits.VOID_SHIELDS],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Typhon Siege Tank",
        5,
        1,
        UnitType.WAR_ENGINE,
        25,
        4,
        6,
        5,
        400 / 3,
        [
            RangedWeapon(
                45,
                name="Typhon Siege Cannon",
                bp=3,
                traits=[Traits.INDIRECT, Traits.IGNORE_COVER],
            ),
            AssaultWeapon([Traits.IGNORE_COVER]),
            HeavyBolter(),
            HeavyBolter(),
        ],
        damage_capacity=2,
        traits=[Traits.ASTARTES, Traits.RIENFORCED_ARMOUR],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Cerberus Heavy Tank Destroyer",
        5,
        1,
        UnitType.WAR_ENGINE,
        25,
        4,
        6,
        5,
        400 / 3,
        [
            RangedWeapon(60, name="Neutron Laser Array", at=3, traits=[Traits.DISRUPT]),
            RangedWeapon(60, name="Neutron Laser Array", at=3, traits=[Traits.DISRUPT]),
            HeavyBolter(),
            HeavyBolter(),
        ],
        damage_capacity=2,
        traits=[Traits.ASTARTES, Traits.RIENFORCED_ARMOUR],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Kratos Battle Tank with H.B.",
        5,
        1,
        UnitType.WAR_ENGINE,
        25,
        armour=4,
        cc=6,
        ff=5,
        weapons=[
            RangedWeapon(45, name="Kratos Cannon", at=3, ap=3),
            RangedWeapon(45, name="Co-axial Auto Cannon", at=6, ap=5),
            HeavyBolter(),
            HeavyBolter(),
            HeavyBolter(),
            HeavyBolter(),
        ],
        single_unit_cost=100,
        damage_capacity=2,
        traits=[Traits.ASTARTES, Traits.RIENFORCED_ARMOUR, Traits.THICK_REAR_ARMOUR],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Kratos Battle Tank with Las.",
        5,
        1,
        UnitType.WAR_ENGINE,
        25,
        armour=4,
        cc=6,
        ff=5,
        weapons=[
            RangedWeapon(45, name="Kratos Cannon", at=3, ap=3),
            RangedWeapon(45, name="Co-axial Auto Cannon", at=6, ap=5),
            LasCannon(),
            LasCannon(),
            LasCannon(),
            LasCannon(),
        ],
        single_unit_cost=100,
        damage_capacity=2,
        traits=[Traits.ASTARTES, Traits.RIENFORCED_ARMOUR, Traits.THICK_REAR_ARMOUR],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Land Speeder with Plasma",
        5,
        1,
        UnitType.LIGHT_VEHICLE,
        speed=35,
        armour=5,
        cc=6,
        ff=5,
        weapons=[RangedWeapon(30, name="Plasma Cannon", ap=5, at=5), HeavyBolter()],
        traits=[Traits.ASTARTES, Traits.SKIMMER, Traits.SCOUT],
        single_unit_cost=40,
    )
)

legiones_astartes.add_unit(
    Unit(
        "Land Speeder with Melta",
        5,
        1,
        UnitType.LIGHT_VEHICLE,
        speed=35,
        armour=5,
        cc=6,
        ff=5,
        weapons=[
            RangedWeapon(15, name="Melta Cannon", mw=5),
            SmallArms([Traits.MW], name="Melta Cannon"),
        ],
        traits=[Traits.ASTARTES, Traits.SKIMMER, Traits.SCOUT],
        single_unit_cost=40,
    )
)

legiones_astartes.add_unit(
    Unit(
        "Javelin Attack Speeder Cyclone",
        5,
        1,
        UnitType.LIGHT_VEHICLE,
        speed=35,
        armour=4,
        cc=6,
        ff=5,
        weapons=[
            RangedWeapon(45, name="Cyclone Missile Launcher", ap=3, at=5),
            HeavyBolter(),
        ],
        single_unit_cost=50,
        traits=[Traits.ASTARTES, Traits.SKIMMER, Traits.SCOUT],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Javelin Attack Speeder Lascannons",
        5,
        1,
        UnitType.LIGHT_VEHICLE,
        35,
        armour=4,
        cc=6,
        ff=5,
        weapons=[TwinLinkedLasCannon(), HeavyBolter()],
        single_unit_cost=50,
        traits=[Traits.ASTARTES, Traits.SKIMMER, Traits.SCOUT],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Outrider squad",
        5,
        1,
        UnitType.INFANTRY,
        35,
        armour=4,
        cc=3,
        ff=5,
        weapons=[SmallArms()],
        traits=[Traits.ASTARTES, Traits.MOUNTED, Traits.SCOUT],
        single_unit_cost=140 / 4,
    )
)
