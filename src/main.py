from data import ea_40k_units, legiones_astartes, solar_auxilia
from gpr.trainer import GPRTrainer
from data.models import Army
from gpr.mapping.map2 import map2

# from out.unit_stats_table import get_markdown_unit_table
from out.prediction_table import get_markdown_prediction_table
from out.army_file import build_army_markdown_file


def predict_army(trainer: GPRTrainer, army: Army):
    predictions = [trainer.predict(u) for u in army.get_sorted_units()]
    build_army_markdown_file(army, predictions)

    print(get_markdown_prediction_table(predictions, army))
    # print(get_markdown_unit_table(army))


trainer = GPRTrainer(mapper=map2)
trainer.train(ea_40k_units)


predict_army(trainer, solar_auxilia)

predict_army(trainer, legiones_astartes)
