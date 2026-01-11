from data.models import (
    RangedWeapon,
    Traits,
    UnitType,
    Unit,
    Army,
)

minervan = Army("Minervan Tank Legion Forces")


minervan.add_unit(
    Unit(
        "Medusa",
        2,
        1,
        UnitType.ARMORED_VEHICLE,
        speed=20,
        armour=6,
        cc=6,
        ff=5,
        weapons=[
            RangedWeapon(30, mw=4, traits=[Traits.IGNORE_COVER]),
            RangedWeapon(30, ap=5),
        ],
        traits=[],
        single_unit_cost=50,
    )
)

minervan.add_unit(
    Unit(
        "Leman Russ Demolisher",
        2,
        2,
        UnitType.ARMORED_VEHICLE,
        speed=20,
        armour=4,
        cc=6,
        ff=3,
        weapons=[
            RangedWeapon(30, ap=3, at=4, traits=[Traits.IGNORE_COVER]),
            RangedWeapon(45, at=5),
        ],
        traits=[Traits.RIENFORCED_ARMOUR],
        single_unit_cost=68,
    )
)
