from models.units import Unit, UnitType


def unit_type(unit: Unit) -> list[float]:
    return [
        (1 if unit.type == UnitType.CHARACTER or unit.type == UnitType.INFANTRY else 0),
        (
            1
            if unit.type == UnitType.LIGHT_VEHICLE
            or unit.type == UnitType.ARMORED_VEHICLE
            else 0
        ),
        (
            1
            if unit.type == UnitType.WAR_ENGINE
            or unit.type == UnitType.AIRCRAFT_WAR_ENGINE
            else 0
        ),
        (
            1
            if unit.type == UnitType.AIRCRAFT
            or unit.type == UnitType.AIRCRAFT_WAR_ENGINE
            else 0
        ),
    ]
