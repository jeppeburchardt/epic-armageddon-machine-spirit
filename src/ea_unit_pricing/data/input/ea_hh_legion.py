from ea_unit_pricing.domain import (
    AircraftSpeed,
    Army,
    AssaultWeapon,
    Detachment,
    DetachmentUnit,
    MultipleChoiceWeapon,
    Multiplier,
    RangedWeapon,
    SmallArms,
    Traits,
    Unit,
    UnitType,
    UpgradeAdd,
    UpgradeCharacter,
    UpgradeReplace,
)

from .ea_hh_weapons import (
    AutoCannon,
    DemolisherCannon,
    HeavyBolter,
    LasCannon,
    QuadLasCannon,
    TwinAutoCannon,
    TwinHeavyBolter,
    TwinLinkedLasCannon,
)

legiones_astartes = Army("legiones-astartes", "Legiones Astartes")

praetor = Unit(
    name="Praetor",
    type=UnitType.CHARACTER,
    traits=[Traits.SUPREME_COMMANDER, Traits.INVULNERABLE_SAVE],
    weapons=[AssaultWeapon(traits=[Traits.EXTRA_ATTACK_1, Traits.MW])],
    single_unit_cost=100,
    fixed_cost=True,
    strategy_rating=5,
    initiative=1,
)
legiones_astartes.add_unit(praetor)

centurion = Unit(
    name="Centurion",
    type=UnitType.CHARACTER,
    traits=[Traits.COMMANDER, Traits.INVULNERABLE_SAVE, Traits.LEADER],
    weapons=[AssaultWeapon(traits=[Traits.EXTRA_ATTACK_1, Traits.MW])],
    single_unit_cost=50,
    fixed_cost=True,
    strategy_rating=5,
    initiative=1,
)
legiones_astartes.add_unit(praetor)

tactical_squad_unit = Unit(
    "Tactical Legionnaires Squad",
    5,
    1,
    UnitType.INFANTRY,
    15,
    4,
    4,
    4,
    34,
    [SmallArms(name="Bolters")],
    [Traits.KNOW_NO_FEAR],
    transport_cost=1,
    transport_type="Marine",
)
legiones_astartes.add_unit(tactical_squad_unit)

assault_squad_unit = Unit(
    "Assault Squad",
    strategy_rating=5,
    initiative=1,
    type=UnitType.INFANTRY,
    speed=30,
    armour=4,
    cc=3,
    ff=5,
    weapons=[AssaultWeapon(name="Bolt Pistols and Chainswords")],
    traits=[Traits.KNOW_NO_FEAR, Traits.JUMP_PACKS],
    transport_cost=1,
    transport_type="Jumppack",
)
legiones_astartes.add_unit(assault_squad_unit)

heavy_support_squad_unit = Unit(
    "Heavy Support Squad",
    strategy_rating=5,
    initiative=1,
    type=UnitType.INFANTRY,
    speed=15,
    armour=4,
    cc=5,
    ff=3,
    weapons=[
        SmallArms(name="Bolters"),
        RangedWeapon(45, name="Missile Launchers", at=5, ap=4, aa=6),
    ],
    traits=[Traits.KNOW_NO_FEAR],
    transport_cost=1,
    transport_type="Marine",
)
legiones_astartes.add_unit(heavy_support_squad_unit)

tactical_support_squad_unit = Unit(
    "Tactical Support Squad",
    strategy_rating=5,
    initiative=1,
    type=UnitType.INFANTRY,
    speed=15,
    armour=4,
    cc=4,
    ff=4,
    weapons=[
        SmallArms(name="Plasma Guns", traits=[Traits.IGNORE_COVER, Traits.EXTRA_ATTACK_1]),
        RangedWeapon(20, name="Plasma Guns", ap=5, at=5, traits=[Traits.IGNORE_COVER]),
    ],
    traits=[Traits.KNOW_NO_FEAR],
    transport_cost=1,
    transport_type="Marine",
)
legiones_astartes.add_unit(tactical_support_squad_unit)

terminator_squad_unit = Unit(
    "Terminator Squad",
    strategy_rating=5,
    initiative=1,
    type=UnitType.INFANTRY,
    speed=15,
    armour=4,
    cc=3,
    ff=3,
    weapons=[
        AssaultWeapon(traits=[Traits.EXTRA_ATTACK_1, Traits.MW], name="Power Fists"),
        SmallArms(name="Storm Bolters"),
    ],
    traits=[Traits.KNOW_NO_FEAR, Traits.REINFORCED_ARMOUR],
    transport_cost=2,
    transport_type="Terminator",
)
legiones_astartes.add_unit(terminator_squad_unit)

saturnine_terminator_squad_plasma_bombards_unit = Unit(
    "Saturnine Terminator Squad (Plasma Bombards)",
    strategy_rating=5,
    initiative=1,
    type=UnitType.INFANTRY,
    speed=15,
    armour=3,
    cc=3,
    ff=3,
    weapons=[
        AssaultWeapon(traits=[Traits.EXTRA_ATTACK_1, Traits.MW], name="Disruption Fists"),
        RangedWeapon(name="Plasma Bombards", range=20, at=4),
    ],
    traits=[Traits.KNOW_NO_FEAR, Traits.REINFORCED_ARMOUR, Traits.TELEPORT],
)
legiones_astartes.add_unit(saturnine_terminator_squad_plasma_bombards_unit)

saturnine_terminator_squad_twin_heavy_disintegrators_unit = Unit(
    "Saturnine Terminator Squad (Twin Heavy Disintegrators)",
    strategy_rating=5,
    initiative=1,
    type=UnitType.INFANTRY,
    speed=15,
    armour=3,
    cc=3,
    ff=3,
    weapons=[
        AssaultWeapon(traits=[Traits.EXTRA_ATTACK_1, Traits.MW], name="Disruption Fists"),
        RangedWeapon(name="Twin Heavy Disintegrators", range=20, ap=4),
    ],
    traits=[Traits.KNOW_NO_FEAR, Traits.REINFORCED_ARMOUR, Traits.TELEPORT],
)
legiones_astartes.add_unit(saturnine_terminator_squad_twin_heavy_disintegrators_unit)

saturnine_dreadnought_a_unit = Unit(
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
    traits=[Traits.KNOW_NO_FEAR, Traits.WALKER, Traits.REINFORCED_ARMOUR],
)
legiones_astartes.add_unit(saturnine_dreadnought_a_unit)

saturnine_dreadnought_b_unit = Unit(
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
    traits=[Traits.KNOW_NO_FEAR, Traits.WALKER, Traits.REINFORCED_ARMOUR],
)
legiones_astartes.add_unit(saturnine_dreadnought_b_unit)

tarantula_unit = Unit(
    "Tarantula",
    3,
    2,
    UnitType.LIGHT_VEHICLE,
    speed=0,
    armour=6,
    cc=6,
    ff=6,
    weapons=[
        MultipleChoiceWeapon(
            [
                TwinLinkedLasCannon(),
                RangedWeapon(30, name="Hyperios Missiles", aa=4),
            ]
        ),
    ],
    traits=[Traits.SCOUT],
)
legiones_astartes.add_unit(tarantula_unit)

rapier_unit = Unit(
    "Rapier",
    5,
    1,
    UnitType.INFANTRY,
    speed=10,
    armour=4,
    cc=6,
    ff=5,
    weapons=[
        MultipleChoiceWeapon(
            [
                RangedWeapon(45, name="Laser Destroyer Array", ap=6, at=4),
                RangedWeapon(
                    45,
                    name="Quad Launcher",
                    ap=4,
                    at=6,
                    traits=[Traits.INDIRECT],
                ),
            ]
        )
    ],
)
legiones_astartes.add_unit(rapier_unit)

# Araknae: Orias heavy frag missiles

# Araknae: quad accelerator autocannons

# Araknae: twin punisher cannons

sabre_strike_tank_unit = Unit(
    "Sabre Strike Tank",
    5,
    1,
    UnitType.ARMORED_VEHICLE,
    speed=35,
    armour=5,
    cc=6,
    ff=5,
    weapons=[
        MultipleChoiceWeapon(
            [
                RangedWeapon(
                    20,
                    name="Anvilus Autocannon",
                    ap=4,
                    at=5,
                    traits=[Traits.FIXED_FORWARD],
                ),
                RangedWeapon(
                    20,
                    name="Neutron Blaster",
                    ap=5,
                    at=5,
                    traits=[Traits.FIXED_FORWARD, Traits.DISRUPT],
                ),
            ]
        ),
        RangedWeapon(30, name="Sabre Missiles", at=4, traits=[Traits.FIXED_FORWARD]),
    ],
    traits=[Traits.KNOW_NO_FEAR],
)
legiones_astartes.add_unit(sabre_strike_tank_unit)

sicaran_battle_tank_unit = Unit(
    "Sicaran Battle Tank",
    5,
    1,
    UnitType.ARMORED_VEHICLE,
    speed=35,
    armour=5,
    cc=6,
    ff=4,
    weapons=[
        MultipleChoiceWeapon(
            [
                Multiplier(2, RangedWeapon(name="Accelerator Cannon", range=45, at=5, ap=4)),
                Multiplier(2, RangedWeapon(name="Omega Plasma Array", range=45, at=3)),
                Multiplier(4, RangedWeapon(name="Punisher Cannon", range=30, at=5, ap=5)),
                Multiplier(
                    2,
                    RangedWeapon(
                        45,
                        name="Arcus Missile Launcher",
                        ap=6,
                        at=5,
                        traits=[Traits.INDIRECT],
                    ),
                ),
            ],
            name="Turret",
        ),
        MultipleChoiceWeapon(
            [
                Multiplier(2, LasCannon(traits=[Traits.FIXED_FORWARD])),
                Multiplier(2, HeavyBolter(traits=[Traits.FIXED_FORWARD])),
            ],
            name="Sponsons",
        ),
        HeavyBolter(traits=[Traits.FIXED_FORWARD]),
    ],
    traits=[Traits.KNOW_NO_FEAR, Traits.REINFORCED_ARMOUR],
)
legiones_astartes.add_unit(sicaran_battle_tank_unit)

predator_unit = Unit(
    "Predator",
    5,
    1,
    UnitType.ARMORED_VEHICLE,
    30,
    4,
    6,
    5,
    240 / 4,
    [
        MultipleChoiceWeapon(
            [
                RangedWeapon(45, 5, 5, name="Predator Auto Cannon"),
                TwinLinkedLasCannon(),
            ],
            name="Turret",
        ),
        MultipleChoiceWeapon(
            [
                Multiplier(
                    2,
                    HeavyBolter(traits=[Traits.FIXED_FORWARD], stat_modifiers={"ff": -2}),
                ),
                Multiplier(2, LasCannon(traits=[Traits.FIXED_FORWARD])),
            ],
            name="Sponsons",
        ),
    ],
    [Traits.KNOW_NO_FEAR],
)
legiones_astartes.add_unit(predator_unit)

land_raider_unit = Unit(
    "Land Raider",
    5,
    1,
    UnitType.ARMORED_VEHICLE,
    speed=25,
    armour=4,
    cc=6,
    ff=4,
    weapons=[Multiplier(2, TwinLinkedLasCannon(traits=[Traits.FIXED_FORWARD]))],
    traits=[
        Traits.KNOW_NO_FEAR,
        Traits.REINFORCED_ARMOUR,
        Traits.THICK_REAR_ARMOUR,
    ],
    transport_capacity=2,
    transport_capabilities=["Marine", "Terminator"],
)
legiones_astartes.add_unit(land_raider_unit)

rhino_unit = Unit(
    "Rhino",
    5,
    1,
    type=UnitType.ARMORED_VEHICLE,
    speed=25,
    armour=5,
    cc=6,
    ff=6,
    weapons=[SmallArms(name="Bolters")],
    transport_capacity=2,
    transport_capabilities=["Marine"],
)
legiones_astartes.add_unit(rhino_unit)

spartan_assault_tank_unit = Unit(
    "Spartan Assault Tank",
    5,
    1,
    UnitType.WAR_ENGINE,
    speed=25,
    armour=4,
    cc=6,
    ff=5,
    weapons=[
        Multiplier(
            2,
            QuadLasCannon(traits=[Traits.FIXED_FORWARD]),
        ),
        TwinHeavyBolter(traits=[Traits.FIXED_FORWARD]),
    ],
    traits=[
        Traits.KNOW_NO_FEAR,
        Traits.REINFORCED_ARMOUR,
        Traits.THICK_REAR_ARMOUR,
    ],
    damage_capacity=2,
    transport_capacity=4,
    transport_capabilities=["Marine", "Terminator"],
)
legiones_astartes.add_unit(spartan_assault_tank_unit)

thunderhawk_gunship_unit = Unit(
    "Thunderhawk Gunship",
    5,
    1,
    UnitType.AIRCRAFT_WAR_ENGINE,
    200,
    4,
    6,
    4,
    250,
    [
        Multiplier(
            2,
            RangedWeapon(
                45,
                name="Laser Destroyer",
                at=3,
                ap=6,
                traits=[Traits.FIXED_FORWARD],
            ),
        ),
        TwinLinkedLasCannon(aa=5, traits=[Traits.FIXED_FORWARD]),
        Multiplier(2, TwinHeavyBolter(traits=[Traits.FIXED_FORWARD])),
        TwinHeavyBolter(traits=[Traits.LEFT]),
        TwinHeavyBolter(traits=[Traits.RIGHT]),
    ],
    [Traits.KNOW_NO_FEAR, Traits.PLANET_FALL, Traits.REINFORCED_ARMOUR],
    damage_capacity=2,
    aircraft_speed=AircraftSpeed.BOMBER,
    transport_capacity=8,
    transport_capabilities=["Marine", "Jumppack", "Terminator", "Dreadnought"],
)
legiones_astartes.add_unit(thunderhawk_gunship_unit)

fire_raptor_gunship_unit = Unit(
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
        Multiplier(2, RangedWeapon(30, name="Avenger Bolt Cannon", ap=3, at=5)),
        Multiplier(2, RangedWeapon(15, name="Tempest rockets", ap=4, aa=6)),
        MultipleChoiceWeapon(
            [
                Multiplier(2, TwinLinkedLasCannon()),
                Multiplier(2, TwinHeavyBolter()),
                Multiplier(2, TwinAutoCannon()),
            ]
        ),
    ],
    traits=[Traits.KNOW_NO_FEAR, Traits.REINFORCED_ARMOUR],
    aircraft_speed=AircraftSpeed.FIGHTER_BOMBER,
)
legiones_astartes.add_unit(fire_raptor_gunship_unit)

xiphon_interceptor_unit = Unit(
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
        Multiplier(2, RangedWeapon(30, name="Rotary Missile Launcher", at=4, aa=5)),
        LasCannon(),
    ],
    traits=[Traits.KNOW_NO_FEAR],
    aircraft_speed=AircraftSpeed.FIGHTER,
)
legiones_astartes.add_unit(xiphon_interceptor_unit)

storm_eagle_attack_ship_unit = Unit(
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
        Multiplier(2, RangedWeapon(45, at=4)),
        RangedWeapon(45, bp=1),
        RangedWeapon(30, ap=4, aa=5),
    ],
    traits=[Traits.KNOW_NO_FEAR, Traits.REINFORCED_ARMOUR, Traits.PLANET_FALL],
    transport_capacity=4,
    transport_capabilities=["Marine", "Jumppack", "Terminator"],
    damage_capacity=1,
    aircraft_speed=AircraftSpeed.FIGHTER_BOMBER,
)
legiones_astartes.add_unit(storm_eagle_attack_ship_unit)

contemptor_dreadnought_unit = Unit(
    "Contemptor Dreadnought",
    5,
    1,
    UnitType.ARMORED_VEHICLE,
    15,
    3,
    4,
    4,
    60,
    [
        AssaultWeapon(traits=[Traits.MW, Traits.EXTRA_ATTACK_1], name="Power Fist"),
        MultipleChoiceWeapon(
            [
                TwinLinkedLasCannon(),
                RangedWeapon(30, 5, 4, 0, name="Assault Cannon"),
            ],
        ),
    ],
    [Traits.KNOW_NO_FEAR, Traits.WALKER],
    transport_cost=2,
    transport_type="Dreadnought",
)
legiones_astartes.add_unit(contemptor_dreadnought_unit)

deredeo_dreadnought_unit = Unit(
    "Deredeo Dreadnought",
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
        MultipleChoiceWeapon(
            [
                Multiplier(
                    2,
                    RangedWeapon(45, name="Anvilus Autocannon Battery", ap=5, at=4),
                ),
                Multiplier(
                    2,
                    RangedWeapon(
                        45,
                        name="Hellfire Plasma Cannonade",
                        ap=4,
                        at=4,
                        traits=[Traits.SLOW_FIRING],
                    ),
                ),
            ]
        ),
    ],
    traits=[Traits.KNOW_NO_FEAR, Traits.WALKER, Traits.INVULNERABLE_SAVE],
    transport_cost=2,
    transport_type="Dreadnought",
)
legiones_astartes.add_unit(deredeo_dreadnought_unit)

leviathan_siege_dreadnought_unit = Unit(
    "Leviathan Siege Dreadnought",
    5,
    1,
    UnitType.ARMORED_VEHICLE,
    speed=15,
    armour=4,
    cc=4,
    ff=4,
    weapons=[
        AssaultWeapon(traits=[Traits.EXTRA_ATTACK_1, Traits.MW], name="Siege Claw"),
        MultipleChoiceWeapon(
            [
                RangedWeapon(20, name="Leviathan Storm Cannon", ap=4, at=4),
                RangedWeapon(20, name="Cyclonic Melta Lance", at=3, mw=5),
            ]
        ),
    ],
    traits=[Traits.KNOW_NO_FEAR, Traits.WALKER, Traits.REINFORCED_ARMOUR],
    transport_cost=2,
    transport_type="Dreadnought",
)
legiones_astartes.add_unit(leviathan_siege_dreadnought_unit)

vindicator_unit = Unit(
    "Vindicator",
    5,
    1,
    UnitType.ARMORED_VEHICLE,
    speed=25,
    armour=4,
    cc=6,
    ff=4,
    weapons=[DemolisherCannon()],
    traits=[Traits.KNOW_NO_FEAR, Traits.WALKER],
)
legiones_astartes.add_unit(vindicator_unit)

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
#         traits=[Traits.KNOW_NO_FEAR, Traits.WALKER],
#     )
# )

legion_whirlwind_unit = Unit(
    "Legion Whirlwind",
    5,
    1,
    UnitType.ARMORED_VEHICLE,
    speed=30,
    armour=5,
    cc=6,
    ff=5,
    weapons=[
        MultipleChoiceWeapon(
            [
                Multiplier(
                    2,
                    RangedWeapon(
                        45,
                        name="Scorpius Multi Launcher",
                        ap=6,
                        at=5,
                        traits=[Traits.INDIRECT],
                    ),
                ),
                RangedWeapon(
                    45,
                    name="Vengeance & Castellan Missiles",
                    bp=1,
                    traits=[Traits.IGNORE_COVER, Traits.INDIRECT],
                ),
            ]
        )
    ],
    traits=[Traits.KNOW_NO_FEAR],
)
legiones_astartes.add_unit(legion_whirlwind_unit)

mastodon_armored_transport_unit = Unit(
    "Mastodon Armored Transport",
    5,
    1,
    UnitType.WAR_ENGINE,
    speed=20,
    armour=4,
    cc=5,
    ff=4,
    damage_capacity=4,
    void_shields=2,
    transport_capacity=8,
    transport_capabilities=["Marine", "Jumppack", "Terminator", "Dreadnought"],
    weapons=[
        SmallArms([Traits.EXTRA_ATTACK_1, Traits.MW]),
        MultipleChoiceWeapon(
            [
                Multiplier(2, LasCannon()),
                Multiplier(2, HeavyBolter()),
            ],
            name="Sponson Weapons",
        ),
        Multiplier(
            2,
            RangedWeapon(
                15,
                name="Sponson Mounted heavy flamers",
                ap=4,
                traits=[Traits.IGNORE_COVER],
            ),
        ),
        Multiplier(2, RangedWeapon(30, ap=4, at=4, aa=5, name="Skyreaper battery")),
    ],
    traits=[Traits.KNOW_NO_FEAR, Traits.REINFORCED_ARMOUR],
)
legiones_astartes.add_unit(mastodon_armored_transport_unit)

typhon_siege_tank_unit = Unit(
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
        Multiplier(2, HeavyBolter()),
    ],
    damage_capacity=2,
    traits=[Traits.KNOW_NO_FEAR, Traits.REINFORCED_ARMOUR],
)
legiones_astartes.add_unit(typhon_siege_tank_unit)

cerberus_heavy_tank_destroyer_unit = Unit(
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
        Multiplier(
            2,
            RangedWeapon(60, name="Neutron Laser Array", at=3, mw=5, traits=[Traits.DISRUPT]),
        ),
        Multiplier(2, HeavyBolter()),
    ],
    damage_capacity=2,
    traits=[Traits.KNOW_NO_FEAR, Traits.REINFORCED_ARMOUR],
)
legiones_astartes.add_unit(cerberus_heavy_tank_destroyer_unit)

kratos_battle_tank_unit = Unit(
    "Kratos Battle Tank",
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
        MultipleChoiceWeapon(
            [
                Multiplier(
                    2,
                    HeavyBolter(traits=[Traits.FIXED_FORWARD], stat_modifiers={"ff": -1}),
                ),
                Multiplier(2, LasCannon(traits=[Traits.FIXED_FORWARD])),
                Multiplier(2, AutoCannon(traits=[Traits.FIXED_FORWARD])),
            ],
            name="Sponsons",
        ),
        MultipleChoiceWeapon(
            [
                Multiplier(
                    2,
                    HeavyBolter(traits=[Traits.FIXED_FORWARD], stat_modifiers={"ff": -1}),
                ),
                Multiplier(2, LasCannon(traits=[Traits.FIXED_FORWARD])),
                Multiplier(2, AutoCannon(traits=[Traits.FIXED_FORWARD])),
            ],
            name="Hull Weapons",
        ),
    ],
    damage_capacity=2,
    traits=[
        Traits.KNOW_NO_FEAR,
        Traits.REINFORCED_ARMOUR,
        Traits.THICK_REAR_ARMOUR,
    ],
)
legiones_astartes.add_unit(kratos_battle_tank_unit)


fellblade_super_heavy_tank_unit = Unit(
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
        Multiplier(
            2,
            QuadLasCannon(traits=[Traits.FIXED_FORWARD]),
        ),
        TwinHeavyBolter(traits=[Traits.FIXED_FORWARD]),
        DemolisherCannon(traits=[Traits.FIXED_FORWARD]),
    ],
    damage_capacity=4,
    traits=[
        Traits.KNOW_NO_FEAR,
        Traits.REINFORCED_ARMOUR,
        Traits.THICK_REAR_ARMOUR,
    ],
)
legiones_astartes.add_unit(fellblade_super_heavy_tank_unit)

glaive_super_heavy_tank_unit = Unit(
    "Glaive Super Heavy Tank",
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
                name="Volkite Carronade",
                range=75,
                ap=3,
                at=5,
                traits=[Traits.DISRUPT, Traits.IGNORE_COVER],
            ),
        ),
        Multiplier(
            2,
            QuadLasCannon(traits=[Traits.FIXED_FORWARD]),
        ),
        TwinHeavyBolter(traits=[Traits.FIXED_FORWARD]),
    ],
    damage_capacity=4,
    traits=[
        Traits.KNOW_NO_FEAR,
        Traits.REINFORCED_ARMOUR,
        Traits.THICK_REAR_ARMOUR,
    ],
)
legiones_astartes.add_unit(glaive_super_heavy_tank_unit)

falchion_super_heavy_tank_destroyer_unit = Unit(
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
        Multiplier(
            2,
            QuadLasCannon(traits=[Traits.FIXED_FORWARD]),
        ),
    ],
    damage_capacity=4,
    traits=[
        Traits.KNOW_NO_FEAR,
        Traits.REINFORCED_ARMOUR,
        Traits.THICK_REAR_ARMOUR,
    ],
)
legiones_astartes.add_unit(falchion_super_heavy_tank_destroyer_unit)

ascalon_super_heavy_tank_unit = Unit(
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
                traits=[Traits.FIXED_FORWARD],
            ),
        ),
        Multiplier(
            2,
            QuadLasCannon(traits=[Traits.FIXED_FORWARD]),
        ),
    ],
    damage_capacity=4,
    traits=[
        Traits.KNOW_NO_FEAR,
        Traits.REINFORCED_ARMOUR,
        Traits.THICK_REAR_ARMOUR,
    ],
)
legiones_astartes.add_unit(ascalon_super_heavy_tank_unit)

land_speeder_with_plasma_cannon_and_heavy_bolter_unit = Unit(
    "Land Speeder with Plasma Cannon and Heavy Bolter",
    5,
    1,
    UnitType.LIGHT_VEHICLE,
    speed=35,
    armour=5,
    cc=6,
    ff=5,
    weapons=[RangedWeapon(30, name="Plasma Cannon", ap=5, at=5), HeavyBolter()],
    traits=[Traits.KNOW_NO_FEAR, Traits.SKIMMER, Traits.SCOUT],
)
legiones_astartes.add_unit(land_speeder_with_plasma_cannon_and_heavy_bolter_unit)

land_speeder_with_flamer_and_multi_melta_unit = Unit(
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
    traits=[Traits.KNOW_NO_FEAR, Traits.SKIMMER, Traits.SCOUT],
)
legiones_astartes.add_unit(land_speeder_with_flamer_and_multi_melta_unit)

javelin_attack_speeder_unit = Unit(
    "Javelin Attack Speeder",
    5,
    1,
    UnitType.LIGHT_VEHICLE,
    speed=35,
    armour=4,
    cc=6,
    ff=5,
    weapons=[
        MultipleChoiceWeapon(
            [
                RangedWeapon(45, name="Cyclone Missile Launcher", ap=3, at=5),
                TwinLinkedLasCannon(),
            ],
        ),
        HeavyBolter(),
    ],
    traits=[Traits.KNOW_NO_FEAR, Traits.SKIMMER, Traits.SCOUT],
)
legiones_astartes.add_unit(javelin_attack_speeder_unit)

outrider_squad_unit = Unit(
    "Outrider squad",
    5,
    1,
    UnitType.INFANTRY,
    35,
    armour=4,
    cc=3,
    ff=5,
    weapons=[SmallArms(name="Bolters")],
    traits=[Traits.KNOW_NO_FEAR, Traits.MOUNTED, Traits.SCOUT],
)
legiones_astartes.add_unit(outrider_squad_unit)

scimitar_jetbike_unit = Unit(
    "Scimitar Jetbike",
    5,
    1,
    UnitType.INFANTRY,
    35,
    armour=4,
    cc=4,
    ff=4,
    weapons=[HeavyBolter()],
    traits=[Traits.KNOW_NO_FEAR, Traits.MOUNTED, Traits.SKIMMER, Traits.SCOUT],
)
legiones_astartes.add_unit(scimitar_jetbike_unit)

## Character upgrade
character_upgrade = UpgradeCharacter(
    name="Character", transport_warning=False, character_names=[praetor.name, centurion.name]
)
legiones_astartes.add_upgrade(character_upgrade)

## Transport upgrade
transportation_upgrade = UpgradeAdd(
    "Transport",
    transportWarning=True,
    adds=[
        DetachmentUnit(rhino_unit),
        DetachmentUnit(land_raider_unit),
        DetachmentUnit(spartan_assault_tank_unit),
        DetachmentUnit(mastodon_armored_transport_unit),
    ],
)
legiones_astartes.add_upgrade(transportation_upgrade)

## Support tank upgrade
support_tank_upgrade = UpgradeAdd(
    "Support Tank",
    maxTotal=2,
    adds=[
        DetachmentUnit(predator_unit),
        DetachmentUnit(sicaran_battle_tank_unit),
        DetachmentUnit(vindicator_unit),
    ],
)
legiones_astartes.add_upgrade(support_tank_upgrade)

## Dreadnought upgrade
dreadnought_upgrade = UpgradeAdd(
    "Support Dreadnought",
    maxTotal=4,
    adds=[
        DetachmentUnit(contemptor_dreadnought_unit),
        DetachmentUnit(leviathan_siege_dreadnought_unit),
        DetachmentUnit(deredeo_dreadnought_unit),
    ],
)
legiones_astartes.add_upgrade(dreadnought_upgrade)

## Tactical detachment
tactical_squad_detachment = Detachment(
    name="Tactical Legionnaires Detachment",
    group="Line",
    units=[DetachmentUnit(unit=tactical_squad_unit, count=8)],
)
tactical_squad_detachment.add_upgrade(transportation_upgrade)
tactical_squad_detachment.add_upgrade(support_tank_upgrade)
tactical_squad_detachment.add_upgrade(dreadnought_upgrade)
tactical_squad_detachment.add_upgrade(character_upgrade)

tactical_support_replace_upgrade = UpgradeReplace(
    name="Tactical Support Squad",
    from_unit=tactical_squad_unit,
    to_unit=tactical_support_squad_unit,
    max=4,
)
legiones_astartes.add_upgrade(tactical_support_replace_upgrade)
tactical_squad_detachment.add_upgrade(tactical_support_replace_upgrade)

heavy_support_replace_upgrade = UpgradeReplace(
    name="Heavy Support Squad",
    from_unit=tactical_squad_unit,
    to_unit=heavy_support_squad_unit,
    max=4,
)
legiones_astartes.add_upgrade(heavy_support_replace_upgrade)
tactical_squad_detachment.add_upgrade(heavy_support_replace_upgrade)

rapier_upgrade = UpgradeAdd(
    "Rapier",
    adds=[DetachmentUnit(rapier_unit)],
    max_total=4,
)
legiones_astartes.add_upgrade(rapier_upgrade)
tactical_squad_detachment.add_upgrade(rapier_upgrade)

legiones_astartes.add_detachment(tactical_squad_detachment)

## Assualt detachment
assault_detachment = Detachment(
    name="Assault Marine Detachment",
    group="Line",
    units=[DetachmentUnit(unit=assault_squad_unit, count=8)],
)
assault_detachment.add_upgrade(transportation_upgrade)
assault_detachment.add_upgrade(character_upgrade)
legiones_astartes.add_detachment(assault_detachment)

## Terminator detachment
terminator_detachment = Detachment(
    name="Terminator Detachment",
    group="Line",
    units=[DetachmentUnit(unit=terminator_squad_unit, min=4, max=8, count=4)],
)
terminator_detachment.add_upgrade(transportation_upgrade)
terminator_detachment.add_upgrade(character_upgrade)
terminator_detachment.add_upgrade(dreadnought_upgrade)
legiones_astartes.add_detachment(terminator_detachment)

## Predator detachment
predator_detachment = Detachment(
    name="Predators Detachment",
    group="Support",
    units=[DetachmentUnit(unit=predator_unit, count=3, max=6)],
)
legiones_astartes.add_detachment(predator_detachment)

## Sicaran detachment
sicaran_detachment = Detachment(
    name="Sicarans Detachment",
    group="Support",
    units=[
        DetachmentUnit(sicaran_battle_tank_unit, count=2, max=4),
    ],
)

legiones_astartes.add_detachment(sicaran_detachment)

## Sabre Strike Tank detachment
sabre_strike_tank_detachment = Detachment(
    name="Sabre Strike Tank Detachment",
    group="Support",
    units=[DetachmentUnit(sabre_strike_tank_unit, count=4, min=4, max=8)],
)
legiones_astartes.add_detachment(sabre_strike_tank_detachment)

## Tarantula detachment
tarantula_detachment = Detachment(
    name="Tarantula Battery",
    group="Support",
    units=[DetachmentUnit(tarantula_unit, count=4, min=4, max=4)],
)
legiones_astartes.add_detachment(tarantula_detachment)

## Kratos detachment
kratos_detachment = Detachment(
    name="Kratos Detachment",
    group="Support",
    units=[DetachmentUnit(kratos_battle_tank_unit, count=2, max=4)],
)
legiones_astartes.add_detachment(kratos_detachment)

## Whirlwind
whirlwind_detachment = Detachment(
    name="Whirlwind Support Battery",
    group="Support",
    units=[
        DetachmentUnit(legion_whirlwind_unit, count=4),
    ],
)
legiones_astartes.add_detachment(whirlwind_detachment)

## Vindicator
vindicator_detachment = Detachment(
    name="Vindicator Support Battery",
    group="Support",
    units=[DetachmentUnit(vindicator_unit, count=4, min=4, max=4)],
)
legiones_astartes.add_detachment(vindicator_detachment)

## Landspeeders
land_speeder_detachment = Detachment(
    name="Landspeeder Detachment",
    group="Support",
    units=[DetachmentUnit(land_speeder_with_flamer_and_multi_melta_unit, count=4)],
)
land_speeder_plasma_upgrade = UpgradeReplace(
    name="Plasma Cannon and Heavy Bolter",
    from_unit=land_speeder_with_flamer_and_multi_melta_unit,
    to_unit=land_speeder_with_plasma_cannon_and_heavy_bolter_unit,
    max=4,
)
legiones_astartes.add_upgrade(land_speeder_plasma_upgrade)
land_speeder_detachment.add_upgrade(land_speeder_plasma_upgrade)
legiones_astartes.add_detachment(land_speeder_detachment)

## Scimitars
scimitar_jetbike_detachment = Detachment(
    name="Scimitar Detachment",
    group="Support",
    units=[DetachmentUnit(scimitar_jetbike_unit, count=6)],
)
legiones_astartes.add_detachment(scimitar_jetbike_detachment)

## Outriders
outrider_detachment = Detachment(
    name="Outrider Detachment",
    group="Support",
    units=[DetachmentUnit(outrider_squad_unit, count=4)],
)
legiones_astartes.add_detachment(outrider_detachment)

## Javelin
javelin_attack_speeder_detachmnet = Detachment(
    name="Javelin Detachment",
    group="Support",
    units=[DetachmentUnit(javelin_attack_speeder_unit, count=4)],
)
legiones_astartes.add_detachment(javelin_attack_speeder_detachmnet)

xiphon_interceptor_detachment = Detachment(
    name="Xiphon Interceptor Wing",
    group="Special",
    units=[DetachmentUnit(xiphon_interceptor_unit, count=3)],
)
legiones_astartes.add_detachment(xiphon_interceptor_detachment)

fire_raptor_gunship_detachment = Detachment(
    name="Fire Raptor Wing",
    group="Special",
    units=[DetachmentUnit(fire_raptor_gunship_unit, count=2)],
)
legiones_astartes.add_detachment(fire_raptor_gunship_detachment)

storm_eagle_detachment = Detachment(
    name="Storm Eagle Wing",
    group="Special",
    units=[DetachmentUnit(storm_eagle_attack_ship_unit, count=2)],
)
legiones_astartes.add_detachment(storm_eagle_detachment)

thunderhawk_gunship_detachment = Detachment(
    name="Thunderhawk Gunship Wing",
    group="Special",
    units=[DetachmentUnit(thunderhawk_gunship_unit, count=1, max=1, min=1)],
)
legiones_astartes.add_detachment(thunderhawk_gunship_detachment)

typhon_detachment = Detachment(
    name="Typhon Siege Tank Detachment",
    group="Special",
    units=[DetachmentUnit(typhon_siege_tank_unit, count=2, min=2, max=4)],
)
legiones_astartes.add_detachment(typhon_detachment)

cerberus_detachment = Detachment(
    name="Cerberus Heavy Tank Destroyer Detachment",
    group="Special",
    units=[DetachmentUnit(cerberus_heavy_tank_destroyer_unit, count=2, min=2, max=4)],
)
legiones_astartes.add_detachment(cerberus_detachment)

fellblade_detachment = Detachment(
    name="Fellblade Detachment",
    group="Special",
    units=[DetachmentUnit(fellblade_super_heavy_tank_unit, count=1, min=1, max=2)],
)
legiones_astartes.add_detachment(fellblade_detachment)

glaive_detachment = Detachment(
    name="Glaive Detachment",
    group="Special",
    units=[DetachmentUnit(glaive_super_heavy_tank_unit, count=1, min=1, max=2)],
)
legiones_astartes.add_detachment(glaive_detachment)

falchion_detachment = Detachment(
    name="Falchion Detachment",
    group="Special",
    units=[DetachmentUnit(falchion_super_heavy_tank_destroyer_unit, count=1, min=1, max=2)],
)
legiones_astartes.add_detachment(falchion_detachment)

ascalon_detachment = Detachment(
    name="Ascalon Detachment",
    group="Special",
    units=[DetachmentUnit(ascalon_super_heavy_tank_unit, count=1, min=1, max=2)],
)
legiones_astartes.add_detachment(ascalon_detachment)
