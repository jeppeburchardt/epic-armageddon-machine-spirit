from models.units import MultipleChoiceWeapon, Unit
from tabulate import tabulate


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
                if first_row:
                    table.append(unit.to_list() + weapon_row + [unit.traits_to_str()])
                    first_row = False
                else:
                    table.append([""] * len(unit.to_list()) + weapon_row + [""])
        else:
            weapon_row = weapon.to_list()
            if first_row:
                table.append(unit.to_list() + weapon_row + [unit.traits_to_str()])
                first_row = False
            else:
                table.append([""] * len(unit.to_list()) + weapon_row + [""])
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
