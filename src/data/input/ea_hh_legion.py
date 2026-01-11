from data.models import (
    RangedWeapon,
    Multiplier,
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
    DemolisherCannon,
)

legiones_astartes = Army("Legiones Astartes")


legiones_astartes.add_unit(
    Unit(
        "Tactical Squad",
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
        "Assault Squad",
        strategy_rating=5,
        initiative=1,
        type=UnitType.INFANTRY,
        speed=30,
        armour=4,
        cc=3,
        ff=5,
        weapons=[SmallArms()],
        traits=[Traits.ASTARTES, Traits.JUMP_PACKS],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Heavy Support Squad",
        strategy_rating=5,
        initiative=1,
        type=UnitType.INFANTRY,
        speed=15,
        armour=4,
        cc=5,
        ff=3,
        weapons=[
            SmallArms(),
            RangedWeapon(45, name="Missile Launchers", at=5, ap=4, aa=6),
        ],
        traits=[Traits.ASTARTES],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Tactical Support Squad",
        strategy_rating=5,
        initiative=1,
        type=UnitType.INFANTRY,
        speed=15,
        armour=4,
        cc=4,
        ff=4,
        weapons=[
            SmallArms(),
            RangedWeapon(
                45, name="Plasma Guns", ap=5, at=5, traits=[Traits.IGNORE_COVER]
            ),
        ],
        traits=[Traits.ASTARTES],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Terminator Squad",
        strategy_rating=5,
        initiative=1,
        type=UnitType.INFANTRY,
        speed=15,
        armour=4,
        cc=3,
        ff=3,
        weapons=[
            AssaultWeapon([Traits.EXTRA_ATTACK_1, Traits.MW], name="Power Fists"),
            SmallArms(name="Storm Bolters"),
        ],
        traits=[Traits.ASTARTES, Traits.RIENFORCED_ARMOUR],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Saturnine Terminator Squad (Plasma Bombards)",
        strategy_rating=5,
        initiative=1,
        type=UnitType.INFANTRY,
        speed=15,
        armour=3,
        cc=3,
        ff=3,
        weapons=[
            AssaultWeapon([Traits.EXTRA_ATTACK_1, Traits.MW], name="Disruption Fists"),
            RangedWeapon(name="Plasma Bombards", range=20, at=4),
        ],
        traits=[Traits.ASTARTES, Traits.RIENFORCED_ARMOUR, Traits.TELEPORT],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Saturnine Terminator Squad (Twin Heavy Disintegrators)",
        strategy_rating=5,
        initiative=1,
        type=UnitType.INFANTRY,
        speed=15,
        armour=3,
        cc=3,
        ff=3,
        weapons=[
            AssaultWeapon([Traits.EXTRA_ATTACK_1, Traits.MW], name="Disruption Fists"),
            RangedWeapon(name="Twin Heavy Disintegrators", range=20, ap=4),
        ],
        traits=[Traits.ASTARTES, Traits.RIENFORCED_ARMOUR, Traits.TELEPORT],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Saturnine Dreadnought a",
        5,
        1,
        UnitType.ARMORED_VEHICLE,
        speed=15,
        armour=4,
        cc=4,
        ff=4,
        weapons=[
            RangedWeapon(30, name="Heavy Plasma Bombards", at=3),
            RangedWeapon(15, name="Inversion Beamer", at=2, traits=[Traits.MW]),
        ],
        traits=[Traits.ASTARTES, Traits.WALKER, Traits.RIENFORCED_ARMOUR],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Saturnine Dreadnought b",
        5,
        1,
        UnitType.ARMORED_VEHICLE,
        speed=15,
        armour=4,
        cc=4,
        ff=4,
        weapons=[
            RangedWeapon(30, name="Disintegrator Cannons", ap=3),
            RangedWeapon(15, name="Graviton Pulverisers", ap=2),
            RangedWeapon(15, name="Graviton Pulverisers", ap=2),
        ],
        traits=[Traits.ASTARTES, Traits.WALKER, Traits.RIENFORCED_ARMOUR],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Tarantula, Twin Lascannon",
        3,
        2,
        UnitType.LIGHT_VEHICLE,
        speed=0,
        armour=6,
        cc=6,
        ff=6,
        weapons=[TwinLinkedLasCannon()],
        traits=[Traits.SCOUT],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Tarantula, Hyperios air-defence missile launcher",
        3,
        2,
        UnitType.LIGHT_VEHICLE,
        speed=0,
        armour=6,
        cc=6,
        ff=6,
        weapons=[RangedWeapon(30, name="Hyperios Missiles", aa=4)],
        traits=[Traits.SCOUT],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Rapier, Laser Destroyer Array",
        5,
        1,
        UnitType.INFANTRY,
        speed=10,
        armour=4,
        cc=6,
        ff=5,
        weapons=[RangedWeapon(45, name="Laser Destroyer Array", ap=6, at=4)],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Rapier, Quad Launcher",
        5,
        1,
        UnitType.INFANTRY,
        speed=10,
        armour=4,
        cc=6,
        ff=5,
        weapons=[
            RangedWeapon(
                45,
                name="Quad Launcher",
                ap=4,
                at=6,
                traits=[Traits.INDIRECT],
            )
        ],
    )
)

# Araknae: Orias heavy frag missiles

# Araknae: quad accelerator autocannons

# Araknae: twin punisher cannons

legiones_astartes.add_unit(
    Unit(
        "Sabre Strike Tank with Anvilus Autocannon",
        5,
        1,
        UnitType.ARMORED_VEHICLE,
        speed=35,
        armour=5,
        cc=6,
        ff=5,
        weapons=[
            RangedWeapon(
                20, name="Anvilus Autocannon", ap=4, at=5, traits=[Traits.FIXED_FORWARD]
            ),
            RangedWeapon(
                30, name="Sabre Missiles", at=4, traits=[Traits.FIXED_FORWARD]
            ),
        ],
        traits=[Traits.ASTARTES],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Sabre Strike Tank with Neutron Blaster",
        5,
        1,
        UnitType.ARMORED_VEHICLE,
        speed=35,
        armour=5,
        cc=6,
        ff=5,
        weapons=[
            RangedWeapon(
                20,
                name="Neutron Blaster",
                ap=5,
                at=5,
                traits=[Traits.FIXED_FORWARD, Traits.DISRUPT],
            ),
            RangedWeapon(
                30, name="Sabre Missiles", at=4, traits=[Traits.FIXED_FORWARD]
            ),
        ],
        traits=[Traits.ASTARTES],
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
            RangedWeapon(
                45, name="Laser Destroyer", at=3, ap=6, traits=[Traits.FIXED_FORWARD]
            ),
            RangedWeapon(
                45, name="Laser Destroyer", at=3, ap=6, traits=[Traits.FIXED_FORWARD]
            ),
            TwinLinkedLasCannon(aa=5, traits=[Traits.FIXED_FORWARD]),
            TwinHeavyBolter(traits=[Traits.FIXED_FORWARD]),
            TwinHeavyBolter(traits=[Traits.FIXED_FORWARD]),
            TwinHeavyBolter(traits=[Traits.LEFT]),
            TwinHeavyBolter(traits=[Traits.RIGHT]),
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
        "Deredeo Dreadnoughts with Anvilus Autocannon Battery",
        5,
        1,
        UnitType.ARMORED_VEHICLE,
        speed=15,
        armour=3,
        cc=5,
        ff=3,
        weapons=[
            TwinHeavyBolter(),
            RangedWeapon(45, name="Aiolos Missile Launcher", ap=5, at=5, aa=5),
            RangedWeapon(45, name="Anvilus Autocannon Battery", ap=5, at=4),
            RangedWeapon(45, name="Anvilus Autocannon Battery", ap=5, at=4),
        ],
        traits=[Traits.ASTARTES, Traits.WALKER, Traits.INVULNERABLE_SAVE],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Deredeo Dreadnoughts with Hellfire Plasma Cannonade",
        5,
        1,
        UnitType.ARMORED_VEHICLE,
        speed=15,
        armour=3,
        cc=5,
        ff=3,
        weapons=[
            TwinHeavyBolter(),
            RangedWeapon(45, name="Aiolos Missile Launcher", ap=5, at=5, aa=5),
            RangedWeapon(
                45,
                name="Hellfire Plasma Cannonade",
                ap=4,
                at=4,
                traits=[Traits.SLOW_FIRING],
            ),
            RangedWeapon(
                45,
                name="Hellfire Plasma Cannonade",
                ap=4,
                at=4,
                traits=[Traits.SLOW_FIRING],
            ),
        ],
        traits=[Traits.ASTARTES, Traits.WALKER, Traits.INVULNERABLE_SAVE],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Leviathan Siege Dreadnoughts with Cyclonic Melta Lance",
        5,
        1,
        UnitType.ARMORED_VEHICLE,
        speed=15,
        armour=4,
        cc=4,
        ff=4,
        weapons=[
            AssaultWeapon([Traits.EXTRA_ATTACK_1, Traits.MW], name="Siege Claw"),
            RangedWeapon(15, name="Cyclonic Melta Lance", at=3, mw=5),
        ],
        traits=[Traits.ASTARTES, Traits.WALKER, Traits.RIENFORCED_ARMOUR],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Leviathan Siege Dreadnoughts with Leviathan Storm Cannon",
        5,
        1,
        UnitType.ARMORED_VEHICLE,
        speed=15,
        armour=4,
        cc=4,
        ff=4,
        weapons=[
            AssaultWeapon([Traits.EXTRA_ATTACK_1, Traits.MW], name="Siege Claw"),
            RangedWeapon(15, name="Leviathan Storm Cannon", ap=4, at=4),
        ],
        traits=[Traits.ASTARTES, Traits.WALKER, Traits.RIENFORCED_ARMOUR],
    )
)

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
    )
)

# This unit does not exist in the Legions Imperialis range
# legiones_astartes.add_unit(
#     Unit(
#         "Vindicator Laser Destroyer",
#         5,
#         1,
#         UnitType.ARMORED_VEHICLE,
#         speed=25,
#         armour=4,
#         cc=6,
#         ff=5,
#         weapons=[
#             RangedWeapon(60, name="Laser Destroyer Array", ap=6, at=3),
#         ],
#         traits=[Traits.ASTARTES, Traits.WALKER],
#     )
# )

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
        weapons=[
            RangedWeapon(
                45,
                name="Vengeance & Castellan Missiles",
                bp=1,
                traits=[Traits.IGNORE_COVER, Traits.INDIRECT],
            )
        ],
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
            RangedWeapon(
                45, name="Scorpius Multi Launcher", ap=6, at=5, traits=[Traits.INDIRECT]
            ),
            RangedWeapon(
                45, name="Scorpius Multi Launcher", ap=6, at=5, traits=[Traits.INDIRECT]
            ),
        ],
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
            RangedWeapon(
                60, name="Neutron Laser Array", at=3, mw=5, traits=[Traits.DISRUPT]
            ),
            RangedWeapon(
                60, name="Neutron Laser Array", at=3, mw=5, traits=[Traits.DISRUPT]
            ),
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
        damage_capacity=2,
        traits=[Traits.ASTARTES, Traits.RIENFORCED_ARMOUR, Traits.THICK_REAR_ARMOUR],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Fellblade Super Heavy Tank",
        5,
        1,
        UnitType.WAR_ENGINE,
        speed=20,
        armour=4,
        cc=5,
        ff=5,
        weapons=[
            RangedWeapon(
                name="Fellblade Cannon",
                range=75,
                ap=2,
                at=2,
                traits=[Traits.MW, Traits.TITAN_KILLER_1],
            ),
            QuadLasCannon(),
            QuadLasCannon(),
            TwinHeavyBolter(traits=[Traits.FIXED_FORWARD]),
            DemolisherCannon(traits=[Traits.FIXED_FORWARD]),
        ],
        damage_capacity=4,
        traits=[Traits.ASTARTES, Traits.RIENFORCED_ARMOUR, Traits.THICK_REAR_ARMOUR],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Glaive Super Heavy Tank",
        5,
        1,
        UnitType.WAR_ENGINE,
        speed=20,
        armour=4,
        cc=5,
        ff=5,
        weapons=[
            RangedWeapon(
                name="Volkite Carronade",
                range=75,
                ap=3,
                at=5,
                traits=[Traits.DISRUPT, Traits.IGNORE_COVER],
            ),
            RangedWeapon(
                name="Volkite Carronade",
                range=75,
                ap=3,
                at=5,
                traits=[Traits.DISRUPT, Traits.IGNORE_COVER],
            ),
            RangedWeapon(
                name="Volkite Carronade",
                range=75,
                ap=3,
                at=5,
                traits=[Traits.DISRUPT, Traits.IGNORE_COVER],
            ),
            RangedWeapon(
                name="Volkite Carronade",
                range=75,
                ap=3,
                at=5,
                traits=[Traits.DISRUPT, Traits.IGNORE_COVER],
            ),
            QuadLasCannon(),
            QuadLasCannon(),
            TwinHeavyBolter(traits=[Traits.FIXED_FORWARD]),
        ],
        damage_capacity=4,
        traits=[Traits.ASTARTES, Traits.RIENFORCED_ARMOUR, Traits.THICK_REAR_ARMOUR],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Falchion Super Heavy Tank Destroyer",
        5,
        1,
        UnitType.WAR_ENGINE,
        speed=20,
        armour=4,
        cc=5,
        ff=5,
        weapons=[
            RangedWeapon(
                name="Twin Linked Volcano Cannon",
                range=90,
                ap=2,
                at=2,
                traits=[Traits.MW, Traits.TITAN_KILLER_D3, Traits.FIXED_FORWARD],
            ),
            QuadLasCannon(),
            QuadLasCannon(),
        ],
        damage_capacity=4,
        traits=[Traits.ASTARTES, Traits.RIENFORCED_ARMOUR, Traits.THICK_REAR_ARMOUR],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Ascalon Super Heavy Tank",
        5,
        1,
        UnitType.WAR_ENGINE,
        speed=20,
        armour=4,
        cc=5,
        ff=5,
        weapons=[
            Multiplier(
                4,
                RangedWeapon(
                    name="Inferno gun",
                    range=30,
                    ap=2,
                    at=6,
                    traits=[Traits.FIXED_FORWARD, Traits.FIXED_FORWARD],
                ),
            ),
            QuadLasCannon(),
            QuadLasCannon(),
        ],
        damage_capacity=4,
        traits=[Traits.ASTARTES, Traits.RIENFORCED_ARMOUR, Traits.THICK_REAR_ARMOUR],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Land Speeder with Plasma Cannon and Heavy Bolter",
        5,
        1,
        UnitType.LIGHT_VEHICLE,
        speed=35,
        armour=5,
        cc=6,
        ff=5,
        weapons=[RangedWeapon(30, name="Plasma Cannon", ap=5, at=5), HeavyBolter()],
        traits=[Traits.ASTARTES, Traits.SKIMMER, Traits.SCOUT],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Land Speeder with Flamer and Multi-melta",
        5,
        1,
        UnitType.LIGHT_VEHICLE,
        speed=35,
        armour=5,
        cc=6,
        ff=5,
        weapons=[
            RangedWeapon(15, name="Multi-melta", mw=5),
            SmallArms([Traits.MW], name="Multi-melta"),
        ],
        traits=[Traits.ASTARTES, Traits.SKIMMER, Traits.SCOUT],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Javelin Attack Speeder with Cyclone Missile Launcher",
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
        traits=[Traits.ASTARTES, Traits.SKIMMER, Traits.SCOUT],
    )
)

legiones_astartes.add_unit(
    Unit(
        "Javelin Attack Speeder with Lascannons",
        5,
        1,
        UnitType.LIGHT_VEHICLE,
        35,
        armour=4,
        cc=6,
        ff=5,
        weapons=[TwinLinkedLasCannon(), HeavyBolter()],
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
    )
)

legiones_astartes.add_unit(
    Unit(
        "Scimitar Jetbike",
        5,
        1,
        UnitType.INFANTRY,
        35,
        armour=4,
        cc=4,
        ff=4,
        weapons=[SmallArms()],
        traits=[Traits.ASTARTES, Traits.MOUNTED, Traits.SKIMMER, Traits.SCOUT],
    )
)
