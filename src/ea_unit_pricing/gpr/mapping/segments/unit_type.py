from __future__ import annotations

from ea_unit_pricing.domain.enums import UnitType
from ea_unit_pricing.domain.unit import Unit


def unit_type(unit: Unit) -> list[float]:
    """Return 4 one-hot features encoding the broad unit-type category."""
    return [
        1 if unit.type in (UnitType.CHARACTER, UnitType.INFANTRY) else 0,
        1 if unit.type in (UnitType.LIGHT_VEHICLE, UnitType.ARMORED_VEHICLE) else 0,
        1 if unit.type in (UnitType.WAR_ENGINE, UnitType.AIRCRAFT_WAR_ENGINE) else 0,
        1 if unit.type in (UnitType.AIRCRAFT, UnitType.AIRCRAFT_WAR_ENGINE) else 0,
    ]
