from data.models import RangedWeapon, SmallArms, Traits, UnitType, Unit, AssaultWeapon
from .ea_hh_weapons import (
    HeavyBolter,
    LasCannon,
    TwinLinkedLasCannon,
    VanquisherBattleCannon,
    BattleCannon,
    DemolisherCannon,
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


ea_hh_solar_aux = [
    infantry,
    infantry_flamers,
    veletaris,
    ogryn_charonite_squad,
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
]
