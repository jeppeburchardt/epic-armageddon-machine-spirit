"""Unit domain model.

Provides the ``Unit`` dataclass and the ``expand_choices()`` helper that
expands ``MultipleChoiceWeapon`` slots into one ``Unit`` per option combo.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from itertools import product as cartesian_product

from ea_unit_pricing.domain.enums import (
    AircraftSpeed,
    Traits,
    UnitType,
    aircraft_speed_to_string,
    trait_to_string,
    unit_type_to_string,
)
from ea_unit_pricing.domain.weapons import (
    AssaultWeapon,
    MultipleChoiceWeapon,
    Multiplier,
    RangedWeapon,
    SmallArms,
)

__all__ = ["Unit", "expand_choices"]


@dataclass
class Unit:
    """A single game model with stats, weapons, traits, and an optional cost.

    Stat conventions (dice-test semantics):
    * ``initiative``, ``armour``, ``cc``, ``ff`` — roll *X or more* on D6;
      **lower value = better** (e.g. armour 3 is better than armour 5).
    * ``speed`` — centimetres; higher = faster.
    * ``strategy_rating``, ``damage_capacity``, ``void_shields`` —
      higher = better.

    Use ``single_unit_cost = 0`` (the default) for prediction targets;
    set it on training units to the actual published cost per model.
    """

    name: str
    strategy_rating: int
    initiative: int
    type: UnitType
    speed: int = 0
    armour: int = 0
    cc: int = 0
    ff: int = 0
    single_unit_cost: float = 0
    weapons: list[RangedWeapon | AssaultWeapon | SmallArms | Multiplier | MultipleChoiceWeapon] = (
        field(default_factory=list)
    )
    traits: list[Traits] = field(default_factory=list)
    transport_capacity: int = 0
    transport_capabilities: list[str] = field(default_factory=list)
    transport_type: str = ""
    transport_cost: int = 0
    damage_capacity: int = 1
    void_shields: int = 0
    aircraft_speed: AircraftSpeed = AircraftSpeed.NONE
    fixed_cost: bool = False

    # ------------------------------------------------------------------
    # Display helpers
    # ------------------------------------------------------------------

    def to_list(self) -> list[str | int]:
        """Return a short display row for tabulate (name, type, speed, armour, cc, ff)."""
        return [
            self.name,
            unit_type_to_string(self.type),
            self.unit_speed_to_string(),
            self.armour,
            self.cc,
            self.ff,
        ]

    def traits_to_str(self) -> str:
        """Return a comma-separated string of traits and special attributes."""
        parts: list[str] = []
        if self.type == UnitType.WAR_ENGINE:
            parts.append(f"DC{self.damage_capacity}")
        if self.void_shields:
            parts.append(f"Void Shields ({self.void_shields})")
        return ", ".join(list(map(trait_to_string, self.traits)) + parts)

    def unit_speed_to_string(self) -> str:
        """Return a human-readable speed string."""
        if self.type in (UnitType.AIRCRAFT, UnitType.AIRCRAFT_WAR_ENGINE):
            return aircraft_speed_to_string(self.aircraft_speed)
        return f"{self.speed}cm"

    # ------------------------------------------------------------------
    # Weapon access
    # ------------------------------------------------------------------

    def get_all_ranged_weapons(
        self,
    ) -> list[RangedWeapon | AssaultWeapon | SmallArms]:
        """Return all concrete (non-choice) weapons, expanding Multipliers."""
        result: list[RangedWeapon | AssaultWeapon | SmallArms] = []
        for w in self.weapons:
            if isinstance(w, Multiplier):
                result.extend([w.weapon] * w.times)
            elif isinstance(w, MultipleChoiceWeapon):
                pass  # resolved via get_all_configurations() / expand_choices()
            else:
                result.append(w)
        return result

    # ------------------------------------------------------------------
    # Configuration expansion
    # ------------------------------------------------------------------

    def get_all_configurations(self) -> list[Unit]:
        """Return one Unit per weapon-option combination.

        Delegates to the module-level ``expand_choices()`` function.
        If the unit has no ``MultipleChoiceWeapon`` slots, returns ``[self]``.
        """
        return expand_choices(self)


def expand_choices(unit: Unit) -> list[Unit]:
    """Expand a unit's ``MultipleChoiceWeapon`` slots into concrete variants.

    Each ``MultipleChoiceWeapon`` in the unit's weapon list is replaced by
    every possible option via Cartesian product.  The resulting ``Unit``
    copies receive a bracketed suffix on the name indicating the chosen
    weapons.

    If the unit has no ``MultipleChoiceWeapon`` slots, ``[unit]`` is returned
    unchanged.
    """
    choice_positions = [
        i for i, w in enumerate(unit.weapons) if isinstance(w, MultipleChoiceWeapon)
    ]
    if not choice_positions:
        return [unit]

    option_lists = [unit.weapons[i].options for i in choice_positions]  # type: ignore[union-attr]
    configs: list[Unit] = []
    for combo in cartesian_product(*option_lists):
        new_weapons = list(unit.weapons)
        stat_delta: dict[str, int] = {}
        for pos, chosen in zip(choice_positions, combo):
            new_weapons[pos] = chosen
            for key, delta in getattr(chosen, "stat_modifiers", {}).items():
                stat_delta[key] = stat_delta.get(key, 0) + delta
        label = " | ".join(w.name for w in combo)
        variant = Unit(
            f"{unit.name} [{label}]",
            unit.strategy_rating,
            unit.initiative,
            unit.type,
            speed=unit.speed,
            armour=unit.armour,
            cc=unit.cc + stat_delta.get("cc", 0),
            ff=unit.ff + stat_delta.get("ff", 0),
            single_unit_cost=unit.single_unit_cost,
            weapons=new_weapons,
            traits=unit.traits,
            transport_capacity=unit.transport_capacity,
            damage_capacity=unit.damage_capacity,
            void_shields=unit.void_shields,
            aircraft_speed=unit.aircraft_speed,
        )
        configs.append(variant)
    return configs
