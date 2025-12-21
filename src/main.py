from data import ea_40k_units, ea_hh_units
from gpr.trainer import GPRTrainer
from gpr.mapping.map2 import map2
from tabulate import tabulate


trainer = GPRTrainer(mapper=map2)
trainer.train(ea_40k_units)
# trainer.validate()

print(
    tabulate(
        [trainer.predict(u) for u in ea_hh_units],
        headers=["Name", "Original Cost", "Predicted Cost", "Uncertainty", "Quality", "Score"],
        tablefmt="github",
    )
)
