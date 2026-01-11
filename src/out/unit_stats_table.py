from data.models import Unit
from tabulate import tabulate


def format_unit_with_weapons(unit: Unit):
    table = []
    if unit.weapons:
        table.append(
            unit.to_list() + unit.weapons[0].to_list() + [unit.traits_to_str()]
        )
        for weapon in unit.weapons[1:]:
            table.append([""] * len(unit.to_list()) + weapon.to_list())
    else:
        table.append(unit.to_list() + [""])
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
