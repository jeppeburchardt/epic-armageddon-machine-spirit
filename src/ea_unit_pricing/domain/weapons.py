"""Weapon classes for ranged, assault, and special weapon slots.

All weapon classes are dataclasses — instances are effectively immutable
after construction.  Mutable defaults are eliminated via ``field(default_factory=...)``.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from ea_unit_pricing.domain.enums import Traits

__all__ = [
    "AssaultWeapon",
    "Multiplier",
    "MultipleChoiceWeapon",
    "RangedWeapon",
    "SmallArms",
]

# Type alias used throughout the codebase for any weapon slot.
AnyWeapon = "RangedWeapon | AssaultWeapon | SmallArms | Multiplier | MultipleChoiceWeapon"


@dataclass
class RangedWeapon:
    """A ranged weapon with firepower statistics.

    Dice stats use the *roll-X-or-more* convention: lower value = better.

    Args:
        range: Maximum effective range in centimetres.
        at: Anti-tank firepower (dice target number).
        ap: Anti-personnel firepower (dice target number).
        aa: Anti-aircraft firepower (dice target number).
        bp: Barrage points count.
        mw: Macro-weapon firepower (dice target number).
        name: Display name shown in tables and JSON output.
        traits: List of special rule traits.
        stat_modifiers: Additive deltas applied to the carrying unit's base
            stats when this weapon is selected (keys: ``"ff"``, ``"cc"``).
    """

    range: int
    at: int = 0
    ap: int = 0
    aa: int = 0
    bp: int = 0
    traits: list[Traits] = field(default_factory=list)
    mw: int = 0
    name: str = "--"
    stat_modifiers: dict[str, int] = field(default_factory=dict)

    def to_list(self) -> list[str | int]:
        """Return a display row suitable for tabulate."""
        parts: list[str] = []
        if self.at > 0:
            parts.append(f"AT{self.at}+")
        if self.ap > 0:
            parts.append(f"AP{self.ap}+")
        if self.mw > 0:
            parts.append(f"MW{self.mw}+")
        if self.aa > 0:
            parts.append(f"AA{self.aa}+")
        if self.bp > 0:
            parts.append(f"{self.bp}BP")
        from ea_unit_pricing.domain.enums import trait_to_string

        firepower = " ".join(parts)
        traits_str = ", ".join(map(trait_to_string, self.traits))
        if firepower and traits_str:
            firepower = f"{firepower}, {traits_str}"
        elif traits_str:
            firepower = traits_str
        return [self.name, self.range, firepower]


@dataclass
class AssaultWeapon:
    """A melee/assault weapon attached to a unit."""

    traits: list[Traits] = field(default_factory=list)
    name: str = "--"

    def to_list(self) -> list[str]:
        from ea_unit_pricing.domain.enums import trait_to_string

        return [self.name, "(base contact)", ", ".join(map(trait_to_string, self.traits))]


@dataclass
class SmallArms:
    """Generic small-arms profile (15cm, no specific firepower dice)."""

    traits: list[Traits] = field(default_factory=list)
    name: str = "Small Arms"

    def to_list(self) -> list[str]:
        from ea_unit_pricing.domain.enums import trait_to_string

        return [self.name, "(Small Arms)", ", ".join(map(trait_to_string, self.traits))]


@dataclass
class Multiplier:
    """Wraps a weapon and indicates it is present *times* times on the unit.

    Example: ``Multiplier(2, HeavyBolter())`` → two Heavy Bolters.
    """

    times: int
    weapon: RangedWeapon

    @property
    def name(self) -> str:
        return f"{self.times}X {self.weapon.name}"

    def to_list(self) -> list[str | int]:
        parts = list(self.weapon.to_list())
        parts[0] = f"{self.times}X {parts[0]}"
        return parts


@dataclass
class MultipleChoiceWeapon:
    """A weapon slot offering mutually exclusive alternatives.

    Use ``Unit.get_all_configurations()`` to expand the unit into one
    concrete ``Unit`` per option combination.

    Example::

        MultipleChoiceWeapon([HeavyBolter(), LasCannon()])
    """

    options: list[RangedWeapon | AssaultWeapon | SmallArms]
    name: str = ""
