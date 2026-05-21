"""Army composition classes: Army, Detachment, Upgrades, and supporting types."""

from __future__ import annotations

from dataclasses import dataclass, field

from ea_unit_pricing.domain.unit import Unit

__all__ = [
    "Army",
    "Detachment",
    "DetachmentUnit",
    "SpecialRule",
    "Upgrade",
    "UpgradeAdd",
    "UpgradeCharacter",
    "UpgradeReplace",
]


@dataclass
class SpecialRule:
    """A named special rule with one or more descriptive paragraphs."""

    title: str
    paragraphs: list[str]


@dataclass
class DetachmentUnit:
    """A unit entry within a detachment, with count constraints."""

    unit: Unit
    count: int = 0
    max: int = 0
    min: int = 0

    def __post_init__(self) -> None:
        if self.max == 0:
            self.max = self.count
        if self.min == 0:
            self.min = self.count


@dataclass
class Detachment:
    """A formation template listing required units and available upgrades."""

    name: str
    group: str
    units: list[DetachmentUnit]
    available_upgrades: list[DetachmentUnit] = field(default_factory=list)

    def add_upgrade(self, upgrade: DetachmentUnit) -> None:
        self.available_upgrades.append(upgrade)

    # Legacy attribute name used in serialization code.
    @property
    def availableUpgrades(self) -> list[DetachmentUnit]:
        return self.available_upgrades


@dataclass
class Upgrade:
    """Base class for detachment upgrade entries."""

    name: str
    type: str  # "add" | "replace" | "character"
    transport_warning: bool = False

    # Legacy attribute name compatibility.
    @property
    def transportWarning(self) -> bool:
        return self.transport_warning


@dataclass
class UpgradeAdd(Upgrade):
    """An upgrade that adds extra units to a detachment."""

    adds: list[DetachmentUnit] = field(default_factory=list)
    max_total: int = 0

    def __init__(
        self,
        name: str,
        adds: list[DetachmentUnit] | None = None,
        max_total: int = 0,
        transport_warning: bool = False,
        # Legacy camelCase kwargs
        maxTotal: int = 0,
        transportWarning: bool = False,
    ) -> None:
        super().__init__(name, type="add", transport_warning=transport_warning or transportWarning)
        self.adds = adds if adds is not None else []
        self.max_total = max_total or maxTotal

    # Legacy attribute name.
    @property
    def maxTotal(self) -> int:
        return self.max_total


@dataclass
class UpgradeReplace(Upgrade):
    """An upgrade that replaces one unit type with another."""

    from_unit: Unit | None = None
    to_unit: Unit | None = None
    max: int = 0

    def __init__(self, name: str, from_unit: Unit, to_unit: Unit, max: int) -> None:
        super().__init__(name, type="replace")
        self.from_unit = from_unit
        self.to_unit = to_unit
        self.max = max

    # Legacy attribute names used in serialization.
    @property
    def fromUnit(self) -> Unit | None:
        return self.from_unit

    @property
    def toUnit(self) -> Unit | None:
        return self.to_unit


@dataclass
class UpgradeCharacter(Upgrade):
    """A character-type upgrade."""

    type: str = field(default="character", init=False)
    character_names: list[str] = field(default_factory=list)


class Army:
    """An army list containing units, detachment definitions, and upgrades.

    Not a dataclass because it is built incrementally via ``add_*`` methods.
    """

    def __init__(
        self,
        slug: str,
        name: str = "",
        strategy_rating: int = 1,
        special_rules: list[SpecialRule] | None = None,
        # Legacy camelCase kwarg accepted for backward compatibility.
        strategyRating: int | None = None,
        specialRules: list[SpecialRule] | None = None,
    ) -> None:
        self.slug = slug
        self.name = name
        self.strategyRating = strategyRating if strategyRating is not None else strategy_rating
        self.specialRules: list[SpecialRule] = (
            specialRules if specialRules is not None else (special_rules or [])
        )
        self.units: list[Unit] = []
        self.detachments: list[Detachment] = []
        self.upgrades: list[Upgrade] = []

    def add_unit(self, unit: Unit) -> None:
        self.units.append(unit)

    def add_detachment(self, detachment: Detachment) -> None:
        self.detachments.append(detachment)

    def add_upgrade(self, upgrade: Upgrade) -> None:
        self.upgrades.append(upgrade)

    def get_sorted_units(self) -> list[Unit]:
        """Return units sorted by UnitType value for consistent output ordering."""
        return sorted(self.units, key=lambda unit: unit.type.value)
