from data import ea_40k_units, legiones_astartes, solar_auxilia
from data.models import Army, Unit
from gpr.trainer import GPRTrainer
from gpr.mapping.map2 import map2
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


def print_army(army):
    print(f"### {army.name} unit stats")
    # Flatten the list of lists for tabulate
    rows = []
    for u in army.units:
        rows.extend(format_unit_with_weapons(u))
    print(
        tabulate(
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
    )


def predict_army(trainer, army: Army):
    predictions = [trainer.predict(u) for u in army.get_sorted_units()]
    print(f"## {army.name}")
    print(
        tabulate(
            predictions,
            headers=[
                "Name",
                "Predicted Cost",
                "Uncertainty",
                "Quality",
                "Score",
            ],
            tablefmt="github",
        )
    )
    avg_score = sum(p[4] for p in predictions) / len(predictions) if predictions else 0
    print(f"\nAverage Score: {avg_score:.2f}\n\n")


trainer = GPRTrainer(mapper=map2)
trainer.train(ea_40k_units)

# predict_army(trainer, legiones_astartes)

print_army(solar_auxilia)
predict_army(trainer, solar_auxilia)

print_army(legiones_astartes)
predict_army(trainer, legiones_astartes)


# validations = trainer.validate()
# predictions = [trainer.predict(u) for u in solar_auxilia.get_sorted_units()]

# print(
#     tabulate(
#         validations,
#         headers=[
#             "Name",
#             "Original Cost",
#             "Predicted Cost",
#             "Error",
#             "Uncertainty",
#             "Quality",
#             "Score",
#         ],
#         tablefmt="github",
#     )
# )
