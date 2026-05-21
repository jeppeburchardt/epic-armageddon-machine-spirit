"""Unit stats table serializer (markdown)."""

from __future__ import annotations

from tabulate import tabulate

from ea_unit_pricing.domain.unit import Unit
from ea_unit_pricing.domain.weapons import MultipleChoiceWeapon

__all__ = ["get_markdown_unit_table"]


def _format_stat_modifiers(modifiers: dict[str, int]) -> str:
    parts = []
    for stat, delta in modifiers.items():
        sign = "+" if delta >= 0 else ""
        parts.append(f"{stat.upper()}{sign}{delta}")
    return ", ".join(parts)


def _format_unit_with_weapons(unit: Unit) -> list[list[str | int]]:
    table: list[list[str | int]] = []
    if not unit.weapons:
        table.append([*unit.to_list(), ""])  # type: ignore[arg-type]
        return table

    first_row = True
    for weapon in unit.weapons:
        if isinstance(weapon, MultipleChoiceWeapon):
            for i, option in enumerate(weapon.options):
                weapon_row = option.to_list()
                if i > 0:
                    weapon_row = [f"(or) {weapon_row[0]}", *weapon_row[1:]]
                modifier_str = _format_stat_modifiers(getattr(option, "stat_modifiers", {}))
                if first_row:
                    notes = ", ".join(filter(None, [unit.traits_to_str(), modifier_str]))
                    table.append(unit.to_list() + weapon_row + [notes])  # type: ignore[operator]
                    first_row = False
                else:
                    table.append([""] * len(unit.to_list()) + weapon_row + [modifier_str])  # type: ignore[operator]
        else:
            weapon_row = weapon.to_list()
            modifier_str = _format_stat_modifiers(getattr(weapon, "stat_modifiers", {}))
            if first_row:
                notes = ", ".join(filter(None, [unit.traits_to_str(), modifier_str]))
                table.append(unit.to_list() + weapon_row + [notes])  # type: ignore[operator]
                first_row = False
            else:
                table.append([""] * len(unit.to_list()) + weapon_row + [modifier_str])  # type: ignore[operator]
    return table


def get_markdown_unit_table(army: object) -> str:
    """Return a GitHub-flavoured markdown table of unit stats for *army*."""
    rows: list[list[str | int]] = []
    for u in army.units:  # type: ignore[attr-defined]
        rows.extend(_format_unit_with_weapons(u))
    return tabulate(
        rows,
        headers=[
            "Name",
            "Type",
            "Speed",
            "Armour",
            "CC",
            "FF",
            "Weapons",
            "Range",
            "Firepower",
            "Notes",
        ],
        tablefmt="github",
    )
