from data.models import RangedWeapon, SmallArms, Traits, UnitType, Unit, AssaultWeapon
from .ea_hh_weapons import (
    HeavyBolter,
    TwinHeavyBolter,
    LasCannon,
    TwinLinkedLasCannon,
    VanquisherBattleCannon,
    BattleCannon,
    DemolisherCannon,
    AutoCannon,
)

infantry = Unit(
    "Infantry Section",
    3,
    2,
    UnitType.INFANTRY,
    speed=15,
    armour=5,
    cc=6,
    ff=5,
    weapons=[SmallArms()],
    single_unit_cost=100 / 7,
)

infantry_flamers = Unit(
    "Infantry with flamers",
    3,
    2,
    UnitType.INFANTRY,
    speed=15,
    armour=5,
    cc=6,
    ff=4,
    weapons=[RangedWeapon(15, ap=5, traits=[Traits.IGNORE_COVER])],
    single_unit_cost=75 / 4,
)

veletaris = Unit(
    "Veletaris Storm Section",
    3,
    2,
    UnitType.INFANTRY,
    speed=15,
    armour=5,
    cc=4,
    ff=6,
    weapons=[AssaultWeapon([Traits.MW])],
    single_unit_cost=75 / 4,
)

ogryn_charonite_squad = Unit(
    "Ogryn Charonite Squad",
    3,
    2,
    UnitType.INFANTRY,
    speed=15,
    armour=3,
    cc=3,
    ff=5,
    weapons=[AssaultWeapon([Traits.EXTRA_ATTACK_1, Traits.MW])],
    single_unit_cost=75 / 2,
)

tactical_command = Unit(
    "Tactical Command Unit",
    3,
    2,
    UnitType.INFANTRY,
    speed=15,
    armour=5,
    cc=6,
    ff=5,
    weapons=[RangedWeapon(15, ap=4, at=5), SmallArms()],
    traits=[Traits.COMMANDER],
    single_unit_cost=50,
)

legate_command = Unit(
    "Legate Command Unit",
    3,
    2,
    UnitType.INFANTRY,
    speed=15,
    armour=5,
    cc=5,
    ff=4,
    weapons=[
        RangedWeapon(15, ap=4, at=5),
        SmallArms([Traits.MW, Traits.EXTRA_ATTACK_1]),
    ],
    traits=[Traits.SUPREME_COMMANDER],
    single_unit_cost=150,
)

rapier_mole_mortar = Unit(
    "Rapier Mole Mortar",
    3,
    2,
    UnitType.INFANTRY,
    speed=10,
    armour=6,
    cc=6,
    ff=6,
    weapons=[RangedWeapon(30, bp=1, traits=[Traits.DISRUPT, Traits.INDIRECT])],
    single_unit_cost=25,
)

rapier_laser_destroyer = Unit(
    "Rapier Laser Destroyer",
    3,
    2,
    UnitType.INFANTRY,
    speed=10,
    armour=6,
    cc=6,
    ff=6,
    weapons=[RangedWeapon(45, ap=6, at=4)],
    single_unit_cost=25,
)

rapier_light_artillery = Unit(
    "Rapier Light Artillery",
    3,
    2,
    UnitType.INFANTRY,
    speed=10,
    armour=6,
    cc=6,
    ff=6,
    weapons=[RangedWeapon(45, ap=4, at=6, traits=[Traits.INDIRECT])],
    single_unit_cost=25,
)

sentinel = Unit(
    "Aethon Heavy Sentinel",
    3,
    2,
    UnitType.LIGHT_VEHICLE,
    speed=20,
    armour=5,
    cc=6,
    ff=5,
    weapons=[RangedWeapon(30, ap=5, at=6), RangedWeapon(45, at=5, ap=3)],
    traits=[Traits.SCOUT, Traits.WALKER],
    single_unit_cost=0,
)

tarantula_las = Unit(
    "Tarantula, Twin Lascannon",
    3,
    2,
    UnitType.LIGHT_VEHICLE,
    speed=0,
    armour=6,
    cc=6,
    ff=5,
    weapons=[TwinLinkedLasCannon()],
    traits=[Traits.SCOUT, Traits.TELEPORT],
    single_unit_cost=25,
)

tarantula_hyp = Unit(
    "Tarantula, Hyperios air-defence missile launcher",
    3,
    2,
    UnitType.LIGHT_VEHICLE,
    speed=0,
    armour=6,
    cc=6,
    ff=5,
    weapons=[RangedWeapon(30, aa=4)],
    traits=[Traits.SCOUT, Traits.TELEPORT],
    single_unit_cost=25,
)

# Cyclops

leman_russ_bh = Unit(
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
    single_unit_cost=350 / 6,
)
leman_russ_bl = Unit(
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
    single_unit_cost=350 / 6,
)
leman_russ_vh = Unit(
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
    single_unit_cost=350 / 6,
)
leman_russ_vl = Unit(
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
    single_unit_cost=350 / 6,
)
leman_russ_annihilator = Unit(
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
    single_unit_cost=350 / 6,
)
leman_russ_demolisher = Unit(
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
    single_unit_cost=350 / 6,
)
leman_russ_executioner = Unit(
    "Leman Russ (Executioner)",
    3,
    2,
    UnitType.ARMORED_VEHICLE,
    speed=25,
    armour=4,
    cc=6,
    ff=4,
    weapons=[
        RangedWeapon(30, ap=4, at=4, traits=[]),  # TODO: fleshbane
        LasCannon(),
    ],
    traits=[Traits.RIENFORCED_ARMOUR],
    single_unit_cost=350 / 6,
)
leman_russ_exterminator = Unit(
    "Leman Russ (Exterminator)",
    3,
    2,
    UnitType.ARMORED_VEHICLE,
    speed=25,
    armour=4,
    cc=6,
    ff=4,
    weapons=[
        RangedWeapon(45, ap=4, at=5, traits=[]),  # TODO: fleshbane
        LasCannon(),
    ],
    traits=[Traits.RIENFORCED_ARMOUR],
    single_unit_cost=350 / 6,
)

malcador_a = Unit(
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
    single_unit_cost=100,
)

malcador_b = Unit(
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
    single_unit_cost=100,
)

malcador_c = Unit(
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
    single_unit_cost=70,
)

dracosan_las = Unit(
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
    single_unit_cost=0,
    transport_capacity=5,
)
dracosan_demo = Unit(
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
    single_unit_cost=0,
    transport_capacity=2,
)

medusa = Unit(
    "Medusa",
    3,
    2,
    UnitType.ARMORED_VEHICLE,
    speed=20,
    armour=5,
    cc=6,
    ff=5,
    weapons=[
        RangedWeapon(30, mw=4, traits=[Traits.IGNORE_COVER]),
        SmallArms([Traits.MW, Traits.IGNORE_COVER]),
        HeavyBolter(),
    ],
    single_unit_cost=83,
)

basilisk = Unit(
    "Basilisk",
    3,
    2,
    UnitType.ARMORED_VEHICLE,
    speed=20,
    armour=5,
    cc=6,
    ff=5,
    weapons=[
        RangedWeapon(120, ap=4, at=4),
        HeavyBolter(),
    ],
    single_unit_cost=83,
)
basilisk_or = Unit(
    "Basilisk (Barrage)",
    3,
    2,
    UnitType.ARMORED_VEHICLE,
    speed=20,
    armour=5,
    cc=6,
    ff=5,
    weapons=[
        RangedWeapon(120, bp=1, traits=[Traits.IGNORE_COVER]),
        HeavyBolter(),
    ],
    single_unit_cost=83,
)

arvus = Unit(
    "Arvus Lighter",
    3,
    2,
    UnitType.ARMORED_VEHICLE,
    speed=30,
    armour=5,
    cc=0,
    ff=6,
    weapons=[SmallArms()],
    traits=[Traits.SKIMMER, Traits.PLANETFALL],
    transport_capacity=2,
    single_unit_cost=25,
)

malcador_infernus = Unit(
    "Malcador Infernus",
    3,
    2,
    UnitType.ARMORED_VEHICLE,
    speed=20,
    armour=4,
    cc=6,
    ff=3,
    weapons=[RangedWeapon(30, ap=3), AutoCannon(), AutoCannon()],
    traits=[Traits.RIENFORCED_ARMOUR, Traits.THICK_REAR_ARMOUR],
    single_unit_cost=70,
)

malcador_valdor = Unit(
    "Malcador Valdor",
    3,
    2,
    UnitType.ARMORED_VEHICLE,
    speed=20,
    armour=4,
    cc=6,
    ff=5,
    weapons=[RangedWeapon(45, mw=3, traits=[Traits.DISRUPT]), AutoCannon()],
    traits=[Traits.RIENFORCED_ARMOUR, Traits.THICK_REAR_ARMOUR],
    single_unit_cost=83,
)

shadowsword = Unit(
    "Shadowsword",
    3,
    2,
    UnitType.WAR_ENGINE,
    speed=15,
    armour=4,
    cc=6,
    ff=6,
    weapons=[
        RangedWeapon(90, mw=2, traits=[Traits.TITAN_KILLER_D3]),
        TwinHeavyBolter(),
        HeavyBolter(),
        HeavyBolter(),
        LasCannon(),
        LasCannon(),
    ],
    damage_capacity=3,
    traits=[Traits.RIENFORCED_ARMOUR],
    single_unit_cost=200,
)

stormblade = Unit(
    "Stromblade",
    3,
    2,
    UnitType.WAR_ENGINE,
    speed=15,
    armour=4,
    cc=6,
    ff=6,
    weapons=[
        RangedWeapon(45, mw=2, traits=[Traits.SLOW_FIRING]),
        TwinHeavyBolter(),
        HeavyBolter(),
        HeavyBolter(),
        LasCannon(),
        LasCannon(),
    ],
    damage_capacity=3,
    traits=[Traits.RIENFORCED_ARMOUR],
    single_unit_cost=200,
)

stormsword = Unit(
    "Stormsword",
    3,
    2,
    UnitType.WAR_ENGINE,
    speed=15,
    armour=4,
    cc=6,
    ff=6,
    weapons=[
        RangedWeapon(30, bp=3, traits=[Traits.DISRUPT, Traits.IGNORE_COVER]),
        TwinHeavyBolter(),
        HeavyBolter(),
        HeavyBolter(),
        LasCannon(),
        LasCannon(),
    ],
    damage_capacity=3,
    traits=[Traits.RIENFORCED_ARMOUR],
    single_unit_cost=200,
)

baneblade = Unit(
    "Baneblade",
    3,
    2,
    UnitType.WAR_ENGINE,
    speed=15,
    armour=4,
    cc=6,
    ff=4,
    weapons=[
        RangedWeapon(75, ap=3, at=3),
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
    single_unit_cost=200,
)

stromhammer = Unit(
    "Stormhammer",
    3,
    2,
    UnitType.WAR_ENGINE,
    speed=15,
    armour=4,
    cc=6,
    ff=4,
    weapons=[
        RangedWeapon(60, ap=3, at=3),
        HeavyBolter(),
        HeavyBolter(),
        HeavyBolter(),
        HeavyBolter(),
        HeavyBolter(),
        HeavyBolter(),
        LasCannon(),
        RangedWeapon(75, ap=3, at=4),
    ],
    damage_capacity=3,
    traits=[Traits.RIENFORCED_ARMOUR],
    single_unit_cost=200,
)

avenger = Unit(
    "Avenger Strike Fighter",
    3,
    2,
    UnitType.AIRCRAFT,
    speed=200,
    armour=5,
    ff=0,
    cc=0,
    weapons=[
        RangedWeapon(30, ap=4, at=2),
        RangedWeapon(30, ap=4, at=2),
        LasCannon(),
        LasCannon(),
        RangedWeapon(30, aa=6, traits=[Traits.REAR]),
    ],
    single_unit_cost=125,
)

thunderbolt = Unit(
    "Thunderbolt",
    3,
    2,
    UnitType.AIRCRAFT,
    speed=200,
    armour=6,
    cc=0,
    ff=0,
    weapons=[
        RangedWeapon(30, at=6, ap=5, aa=5, traits=[Traits.FxF]),
        RangedWeapon(30, at=4, traits=[Traits.FxF]),
        RangedWeapon(15, aa=5, ap=4, traits=[Traits.FxF]),
    ],
    single_unit_cost=112,
)

lightning = Unit(
    "Lightning Fighter",
    3,
    2,
    UnitType.AIRCRAFT,
    speed=200,
    armour=6,
    ff=0,
    cc=0,
    weapons=[
        RangedWeapon(30, at=4, traits=[Traits.SINGLE_SHOT, Traits.FxF]),
        LasCannon(aa=5),
        LasCannon(aa=5),
        AutoCannon(aa=5),
        AutoCannon(aa=5),
    ],
    single_unit_cost=112,
)

# Marauder Bomber
marauder = Unit(
    "Marauder Bomber",
    3,
    2,
    UnitType.AIRCRAFT,
    200,
    armour=4,
    cc=0,
    ff=0,
    weapons=[TwinLinkedLasCannon(aa=4), RangedWeapon(15, bp=3), RangedWeapon(30, aa=5)],
    single_unit_cost=125,
)

# Marauder Destroyer


ea_hh_solar_aux = [
    infantry,
    infantry_flamers,
    veletaris,
    ogryn_charonite_squad,
    tactical_command,
    legate_command,
    rapier_mole_mortar,
    rapier_laser_destroyer,
    rapier_light_artillery,
    sentinel,
    tarantula_las,
    tarantula_hyp,
    leman_russ_bl,
    leman_russ_bh,
    leman_russ_vl,
    leman_russ_vh,
    leman_russ_annihilator,
    leman_russ_demolisher,
    leman_russ_exterminator,
    leman_russ_executioner,
    malcador_a,
    malcador_b,
    malcador_c,
    dracosan_las,
    dracosan_demo,
    medusa,
    basilisk,
    basilisk_or,
    arvus,
    malcador_infernus,
    malcador_valdor,
    shadowsword,
    stormblade,
    stormsword,
    baneblade,
    stromhammer,
    avenger,
    thunderbolt,
    marauder,
]
