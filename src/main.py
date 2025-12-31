from data import ea_40k_units, ea_hh_units
from gpr.trainer import GPRTrainer
from gpr.mapping.map2 import map2
from tabulate import tabulate


trainer = GPRTrainer(mapper=map2)
trainer.train(ea_40k_units)

# validations = trainer.validate()
predictions = [trainer.predict(u) for u in ea_hh_units]

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

print(
    tabulate(
        predictions,
        headers=[
            "Name",
            "Original Cost",
            "Predicted Cost",
            "Uncertainty",
            "Quality",
            "Score",
        ],
        tablefmt="github",
    )
)
avg_score = sum(p[5] for p in predictions) / len(predictions) if predictions else 0
print(f"\nAverage Score: {avg_score:.2f}")
