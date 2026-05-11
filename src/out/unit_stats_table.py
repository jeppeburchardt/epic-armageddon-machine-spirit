from models.units import MultipleChoiceWeapon, Unit
from tabulate import tabulate


def format_stat_modifiers(modifiers: dict[str, int]) -> str:
    parts = []
    for stat, delta in modifiers.items():
        sign = "+" if delta >= 0 else ""
        parts.append(f"{stat.upper()}{sign}{delta}")
    return ", ".join(parts)


def format_unit_with_weapons(unit: Unit):
    table = []
    if not unit.weapons:
        table.append(unit.to_list() + [""])
        return table

    first_row = True
    for weapon in unit.weapons:
        if isinstance(weapon, MultipleChoiceWeapon):
            for i, option in enumerate(weapon.options):
                weapon_row = option.to_list()
                if i > 0:
                    weapon_row = [f"(or) {weapon_row[0]}"] + weapon_row[1:]
                modifier_str = format_stat_modifiers(
                    getattr(option, "stat_modifiers", {})
                )
                if first_row:
                    notes = ", ".join(
                        filter(None, [unit.traits_to_str(), modifier_str])
                    )
                    table.append(unit.to_list() + weapon_row + [notes])
                    first_row = False
                else:
                    table.append(
                        [""] * len(unit.to_list()) + weapon_row + [modifier_str]
                    )
        else:
            weapon_row = weapon.to_list()
            modifier_str = format_stat_modifiers(getattr(weapon, "stat_modifiers", {}))
            if first_row:
                notes = ", ".join(filter(None, [unit.traits_to_str(), modifier_str]))
                table.append(unit.to_list() + weapon_row + [notes])
                first_row = False
            else:
                table.append([""] * len(unit.to_list()) + weapon_row + [modifier_str])
    return table


def get_markdown_unit_table(army):
    # Flatten the list of lists for tabulate
    rows = []
    for u in army.units:
        rows.extend(format_unit_with_weapons(u))
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
