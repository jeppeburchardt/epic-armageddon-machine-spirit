"""Domain package — re-exports all public domain types for convenient importing."""

from ea_unit_pricing.domain.army import (
    Army,
    Detachment,
    DetachmentUnit,
    SpecialRule,
    Upgrade,
    UpgradeAdd,
    UpgradeCharacter,
    UpgradeReplace,
)
from ea_unit_pricing.domain.enums import (
    AircraftSpeed,
    Quality,
    Traits,
    UnitType,
    aircraft_speed_to_string,
    quality_to_str,
    trait_to_string,
    unit_type_to_string,
)
from ea_unit_pricing.domain.result import (
    MultipleChoiceResult,
    Result,
    TrainingSetValidationResult,
)
from ea_unit_pricing.domain.unit import Unit, expand_choices
from ea_unit_pricing.domain.weapons import (
    AssaultWeapon,
    MultipleChoiceWeapon,
    Multiplier,
    RangedWeapon,
    SmallArms,
)

__all__ = [
    # army
    "Army",
    "Detachment",
    "DetachmentUnit",
    "SpecialRule",
    "Upgrade",
    "UpgradeAdd",
    "UpgradeCharacter",
    "UpgradeReplace",
    # enums
    "AircraftSpeed",
    "Quality",
    "Traits",
    "UnitType",
    "aircraft_speed_to_string",
    "quality_to_str",
    "trait_to_string",
    "unit_type_to_string",
    # result
    "MultipleChoiceResult",
    "Result",
    "TrainingSetValidationResult",
    # unit
    "Unit",
    "expand_choices",
    # weapons
    "AssaultWeapon",
    "MultipleChoiceWeapon",
    "Multiplier",
    "RangedWeapon",
    "SmallArms",
]
