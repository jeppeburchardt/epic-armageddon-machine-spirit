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
    TwinHeavyBolter,
    LasCannon,
    TwinLinkedLasCannon,
    VanquisherBattleCannon,
    BattleCannon,
    DemolisherCannon,
    AutoCannon,
    TwinAutoCannon,
)

solar_auxilia = Army(name="Solar Auxilia")

solar_auxilia.add_unit(
    Unit(
        "Infantry Section",
        3,
        2,
        UnitType.INFANTRY,
        speed=15,
        armour=5,
        cc=6,
        ff=5,
        weapons=[SmallArms(name="Las-rifles")],
    )
)

solar_auxilia.add_unit(
    Unit(
        "Infantry with flamers",
        3,
        2,
        UnitType.INFANTRY,
        speed=15,
        armour=5,
        cc=6,
        ff=4,
        weapons=[RangedWeapon(15, name="Flamers", ap=5, traits=[Traits.IGNORE_COVER])],
    )
)

solar_auxilia.add_unit(
    Unit(
        "Veletaris Storm Section",
        3,
        2,
        UnitType.INFANTRY,
        speed=15,
        armour=5,
        cc=4,
        ff=6,
        weapons=[AssaultWeapon([Traits.MW], name="Power Axes")],
    )
)

solar_auxilia.add_unit(
    Unit(
        "Ogryn Charonite Squad",
        3,
        2,
        UnitType.INFANTRY,
        speed=15,
        armour=3,
        cc=3,
        ff=5,
        weapons=[
            AssaultWeapon([Traits.EXTRA_ATTACK_1, Traits.MW], name="Charonite Claws")
        ],
    )
)

solar_auxilia.add_unit(
    Unit(
        "Tactical Command Unit",
        3,
        2,
        UnitType.INFANTRY,
        speed=15,
        armour=5,
        cc=6,
        ff=5,
        weapons=[RangedWeapon(15, ap=4, at=5, name="Plasma Guns"), SmallArms()],
        traits=[Traits.COMMANDER],
    )
)

solar_auxilia.add_unit(
    Unit(
        "Legate Command Unit",
        3,
        2,
        UnitType.INFANTRY,
        speed=15,
        armour=5,
        cc=5,
        ff=4,
        weapons=[
            RangedWeapon(15, ap=4, at=5, name="Volkite Chargers"),
            SmallArms([Traits.MW, Traits.EXTRA_ATTACK_1], name="Archaeotech Pistol"),
        ],
        traits=[Traits.SUPREME_COMMANDER],
    )
)

solar_auxilia.add_unit(
    Unit(
        "Rapier Mole Mortar",
        3,
        2,
        UnitType.INFANTRY,
        speed=10,
        armour=6,
        cc=6,
        ff=6,
        weapons=[
            RangedWeapon(
                30, name="Mole Mortar", bp=1, traits=[Traits.DISRUPT, Traits.INDIRECT]
            )
        ],
    )
)

solar_auxilia.add_unit(
    Unit(
        "Rapier Laser Destroyer",
        3,
        2,
        UnitType.INFANTRY,
        speed=10,
        armour=6,
        cc=6,
        ff=6,
        weapons=[RangedWeapon(45, name="Laser Destroyer", ap=6, at=4)],
    )
)

solar_auxilia.add_unit(
    Unit(
        "Rapier Quad Launcher",
        3,
        2,
        UnitType.INFANTRY,
        speed=10,
        armour=6,
        cc=6,
        ff=6,
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

solar_auxilia.add_unit(
    Unit(
        "Aethon Heavy Sentinel",
        3,
        2,
        UnitType.LIGHT_VEHICLE,
        speed=20,
        armour=5,
        cc=6,
        ff=5,
        weapons=[
            RangedWeapon(30, name="Multilaser", ap=5, at=6),
            RangedWeapon(45, name="Rockets", at=5, ap=3),
        ],
        traits=[Traits.SCOUT, Traits.WALKER],
    )
)

solar_auxilia.add_unit(
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

solar_auxilia.add_unit(
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

# Cyclops

solar_auxilia.add_unit(
    Unit(
        "Leman Russ (Battle cannon + H.B.)",
        3,
        2,
        UnitType.ARMORED_VEHICLE,
        speed=25,
        armour=4,
        cc=6,
        ff=4,
        weapons=[BattleCannon(), HeavyBolter()],
        traits=[Traits.RIENFORCED_ARMOUR],
    )
)
solar_auxilia.add_unit(
    Unit(
        "Leman Russ (Battle cannon + Las)",
        3,
        2,
        UnitType.ARMORED_VEHICLE,
        speed=25,
        armour=4,
        cc=6,
        ff=5,
        weapons=[VanquisherBattleCannon(), LasCannon()],
        traits=[Traits.RIENFORCED_ARMOUR],
    )
)
solar_auxilia.add_unit(
    Unit(
        "Leman Russ (Vanquisher + H.B.)",
        3,
        2,
        UnitType.ARMORED_VEHICLE,
        speed=25,
        armour=4,
        cc=6,
        ff=4,
        weapons=[VanquisherBattleCannon(), HeavyBolter()],
        traits=[Traits.RIENFORCED_ARMOUR],
    )
)
solar_auxilia.add_unit(
    Unit(
        "Leman Russ (Vanquisher + Las)",
        3,
        2,
        UnitType.ARMORED_VEHICLE,
        speed=25,
        armour=4,
        cc=6,
        ff=5,
        weapons=[VanquisherBattleCannon(), LasCannon()],
        traits=[Traits.RIENFORCED_ARMOUR],
    )
)
solar_auxilia.add_unit(
    Unit(
        "Leman Russ (Annihilator)",
        3,
        2,
        UnitType.ARMORED_VEHICLE,
        speed=25,
        armour=4,
        cc=6,
        ff=5,
        weapons=[LasCannon(), TwinLinkedLasCannon()],
        traits=[Traits.RIENFORCED_ARMOUR],
    )
)
solar_auxilia.add_unit(
    Unit(
        "Leman Russ (Demolisher)",
        3,
        2,
        UnitType.ARMORED_VEHICLE,
        speed=25,
        armour=4,
        cc=6,
        ff=5,
        weapons=[
            DemolisherCannon(),
            LasCannon(),
        ],
        traits=[Traits.RIENFORCED_ARMOUR],
    )
)
solar_auxilia.add_unit(
    Unit(
        "Leman Russ (Executioner)",
        3,
        2,
        UnitType.ARMORED_VEHICLE,
        speed=25,
        armour=4,
        cc=6,
        ff=4,
        weapons=[
            RangedWeapon(
                30, name="Plasma Cannon", ap=4, at=4, traits=[Traits.SLOW_FIRING]
            ),
            LasCannon(),
        ],
        traits=[Traits.RIENFORCED_ARMOUR],
    )
)
solar_auxilia.add_unit(
    Unit(
        "Leman Russ (Exterminator)",
        3,
        2,
        UnitType.ARMORED_VEHICLE,
        speed=25,
        armour=4,
        cc=6,
        ff=4,
        weapons=[
            TwinAutoCannon(),
            LasCannon(),
        ],
        traits=[Traits.RIENFORCED_ARMOUR],
    )
)

solar_auxilia.add_unit(
    Unit(
        "Malcador (battle cannon, demolisher, las.spon.)",
        3,
        2,
        UnitType.ARMORED_VEHICLE,
        speed=15,
        armour=4,
        cc=6,
        ff=5,
        weapons=[
            BattleCannon(),
            DemolisherCannon(),
            LasCannon(),
            LasCannon(),
        ],
        traits=[Traits.RIENFORCED_ARMOUR, Traits.THICK_REAR_ARMOUR],
    )
)

solar_auxilia.add_unit(
    Unit(
        "Malcador (vanquisher, demiólisher, h.b.spon.)",
        3,
        2,
        UnitType.ARMORED_VEHICLE,
        speed=15,
        armour=4,
        cc=6,
        ff=4,
        weapons=[
            VanquisherBattleCannon(),
            DemolisherCannon(),
            HeavyBolter(),
            HeavyBolter(),
        ],
        traits=[Traits.RIENFORCED_ARMOUR, Traits.THICK_REAR_ARMOUR],
    )
)

solar_auxilia.add_unit(
    Unit(
        "Malcador (las cannons)",
        3,
        2,
        UnitType.ARMORED_VEHICLE,
        speed=15,
        armour=4,
        cc=6,
        ff=5,
        weapons=[
            TwinLinkedLasCannon(),
            LasCannon(),
            LasCannon(),
            LasCannon(),
        ],
        traits=[Traits.RIENFORCED_ARMOUR, Traits.THICK_REAR_ARMOUR],
    )
)

solar_auxilia.add_unit(
    Unit(
        "Dracosan with las cannon",
        3,
        2,
        UnitType.ARMORED_VEHICLE,
        speed=20,
        armour=4,
        cc=6,
        ff=5,
        weapons=[
            TwinLinkedLasCannon(),
        ],
        traits=[Traits.RIENFORCED_ARMOUR],
        transport_capacity=5,
    )
)
solar_auxilia.add_unit(
    Unit(
        "Dracosan with demolisher",
        3,
        2,
        UnitType.ARMORED_VEHICLE,
        speed=20,
        armour=4,
        cc=6,
        ff=4,
        weapons=[
            DemolisherCannon(),
        ],
        traits=[Traits.RIENFORCED_ARMOUR],
        transport_capacity=2,
    )
)

solar_auxilia.add_unit(
    Unit(
        "Medusa",
        3,
        2,
        UnitType.ARMORED_VEHICLE,
        speed=20,
        armour=5,
        cc=6,
        ff=5,
        weapons=[
            RangedWeapon(
                30, name="Medusa Siege Cannon", mw=4, traits=[Traits.IGNORE_COVER]
            ),
            HeavyBolter(),
        ],
    )
)

solar_auxilia.add_unit(
    Unit(
        "Basilisk",
        3,
        2,
        UnitType.ARMORED_VEHICLE,
        speed=20,
        armour=5,
        cc=6,
        ff=5,
        weapons=[
            RangedWeapon(120, name="Earthshaker Cannon", ap=4, at=4),
            HeavyBolter(),
        ],
    )
)
solar_auxilia.add_unit(
    Unit(
        "Basilisk (Barrage)",
        3,
        2,
        UnitType.ARMORED_VEHICLE,
        speed=20,
        armour=5,
        cc=6,
        ff=5,
        weapons=[
            RangedWeapon(
                120, name="Earthshaker Cannon", bp=1, traits=[Traits.IGNORE_COVER]
            ),
            HeavyBolter(),
        ],
    )
)

solar_auxilia.add_unit(
    Unit(
        "Arvus Lighter",
        3,
        2,
        UnitType.ARMORED_VEHICLE,
        speed=30,
        armour=5,
        cc=0,
        ff=6,
        weapons=[SmallArms(name="Multi-Laser")],
        traits=[Traits.SKIMMER, Traits.PLANETFALL],
        transport_capacity=2,
    )
)

solar_auxilia.add_unit(
    Unit(
        "Malcador Infernus",
        3,
        2,
        UnitType.ARMORED_VEHICLE,
        speed=20,
        armour=4,
        cc=6,
        ff=3,
        weapons=[
            RangedWeapon(30, name="Infernus Cannon", ap=3),
            AutoCannon(),
            AutoCannon(),
        ],
        traits=[Traits.RIENFORCED_ARMOUR, Traits.THICK_REAR_ARMOUR],
    )
)

solar_auxilia.add_unit(
    Unit(
        "Malcador Valdor",
        3,
        2,
        UnitType.ARMORED_VEHICLE,
        speed=20,
        armour=4,
        cc=6,
        ff=5,
        weapons=[
            RangedWeapon(45, name="Neutron Beam Laser", mw=3, traits=[Traits.DISRUPT]),
            AutoCannon(),
        ],
        traits=[Traits.RIENFORCED_ARMOUR, Traits.THICK_REAR_ARMOUR],
    )
)

solar_auxilia.add_unit(
    Unit(
        "Shadowsword",
        3,
        2,
        UnitType.WAR_ENGINE,
        speed=15,
        armour=4,
        cc=6,
        ff=6,
        weapons=[
            RangedWeapon(
                90, name="Volcano Cannon", mw=2, traits=[Traits.TITAN_KILLER_D3]
            ),
            TwinHeavyBolter(),
            HeavyBolter(),
            HeavyBolter(),
            LasCannon(),
            LasCannon(),
        ],
        damage_capacity=3,
        traits=[Traits.RIENFORCED_ARMOUR],
    )
)

solar_auxilia.add_unit(
    Unit(
        "Stromblade",
        3,
        2,
        UnitType.WAR_ENGINE,
        speed=15,
        armour=4,
        cc=6,
        ff=6,
        weapons=[
            RangedWeapon(45, name="Plasma Blastgun", mw=2, traits=[Traits.SLOW_FIRING]),
            TwinHeavyBolter(),
            HeavyBolter(),
            HeavyBolter(),
            LasCannon(),
            LasCannon(),
        ],
        damage_capacity=3,
        traits=[Traits.RIENFORCED_ARMOUR],
    )
)

solar_auxilia.add_unit(
    Unit(
        "Stormsword",
        3,
        2,
        UnitType.WAR_ENGINE,
        speed=15,
        armour=4,
        cc=6,
        ff=6,
        weapons=[
            RangedWeapon(
                30,
                name="Stormsword Siege Cannon",
                bp=3,
                traits=[Traits.DISRUPT, Traits.IGNORE_COVER],
            ),
            TwinHeavyBolter(),
            HeavyBolter(),
            HeavyBolter(),
            LasCannon(),
            LasCannon(),
        ],
        damage_capacity=3,
        traits=[Traits.RIENFORCED_ARMOUR],
    )
)

solar_auxilia.add_unit(
    Unit(
        "Baneblade",
        3,
        2,
        UnitType.WAR_ENGINE,
        speed=15,
        armour=4,
        cc=6,
        ff=4,
        weapons=[
            RangedWeapon(75, name="Baneblade Cannon", ap=3, at=3),
            TwinHeavyBolter(),
            TwinHeavyBolter(),
            TwinHeavyBolter(),
            AutoCannon(),
            LasCannon(),
            LasCannon(),
            DemolisherCannon(),
        ],
        damage_capacity=3,
        traits=[Traits.RIENFORCED_ARMOUR],
    )
)

solar_auxilia.add_unit(
    Unit(
        "Stormhammer",
        3,
        2,
        UnitType.WAR_ENGINE,
        speed=15,
        armour=4,
        cc=6,
        ff=4,
        weapons=[
            RangedWeapon(60, name="Stormhammer Cannon", ap=3, at=3),
            HeavyBolter(),
            HeavyBolter(),
            HeavyBolter(),
            HeavyBolter(),
            HeavyBolter(),
            HeavyBolter(),
            LasCannon(),
            RangedWeapon(75, name="Twin-linked Battle Cannon", ap=3, at=4),
        ],
        damage_capacity=3,
        traits=[Traits.RIENFORCED_ARMOUR],
    )
)

solar_auxilia.add_unit(
    Unit(
        "Avenger Strike Fighter",
        3,
        2,
        UnitType.AIRCRAFT,
        speed=200,
        armour=5,
        ff=0,
        cc=0,
        weapons=[
            RangedWeapon(30, name="Avenger Cannon", ap=4, at=2),
            RangedWeapon(30, name="Avenger Cannon", ap=4, at=2),
            LasCannon(),
            LasCannon(),
            RangedWeapon(30, name="Heavy Stubber", aa=6, traits=[Traits.REAR]),
        ],
    )
)

solar_auxilia.add_unit(
    Unit(
        "Thunderbolt",
        3,
        2,
        UnitType.AIRCRAFT,
        speed=200,
        armour=6,
        cc=0,
        ff=0,
        weapons=[
            RangedWeapon(30, name="Multi-laser", at=6, ap=5, aa=5, traits=[Traits.FxF]),
            RangedWeapon(30, name="Rockets", at=4, traits=[Traits.FxF]),
            RangedWeapon(15, name="Storm Bolters", aa=5, ap=4, traits=[Traits.FxF]),
        ],
    )
)

solar_auxilia.add_unit(
    Unit(
        "Lightning Fighter",
        3,
        2,
        UnitType.AIRCRAFT,
        speed=200,
        armour=6,
        ff=0,
        cc=0,
        weapons=[
            RangedWeapon(
                30,
                name="Kraken Heavy Missiles",
                at=4,
                traits=[Traits.SINGLE_SHOT, Traits.FxF],
            ),
            LasCannon(aa=5),
            LasCannon(aa=5),
            AutoCannon(aa=5),
            AutoCannon(aa=5),
        ],
    )
)

solar_auxilia.add_unit(
    Unit(
        "Marauder Bomber",
        3,
        2,
        UnitType.AIRCRAFT,
        200,
        armour=4,
        cc=0,
        ff=0,
        weapons=[
            TwinLinkedLasCannon(aa=4),
            RangedWeapon(15, name="Bomb Rack", bp=3),
            TwinHeavyBolter(aa=5),
        ],
    )
)
