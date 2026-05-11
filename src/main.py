from data import ea_40k_units, legiones_astartes, solar_auxilia
from gpr.trainer import GPRTrainer
from gpr.split_trainer import GPRSplitTrainer
from models.units import Army, Unit, UnitType
from models.result import MultipleChoiceResult
from gpr.mapping.universal_unit import universal_unit

# from out.unit_stats_table import get_markdown_unit_table
from out.prediction_table import get_markdown_prediction_table
from out.army_file import build_army_markdown_file
from out.army_json import build_prices_json_file
from out.army_list_json import build_army_json_files


def predict_with_choices(trainer: GPRTrainer, unit: Unit):
    """Predict cost for a unit, expanding MultipleChoiceWeapon slots.

    If the unit has no MultipleChoiceWeapon, a plain Result is returned.
    Otherwise a MultipleChoiceResult is returned containing predictions for
    every weapon-option combination; the highest predicted cost is canonical.
    """
    configs = unit.get_all_configurations()
    if len(configs) == 1:
        return trainer.predict(configs[0])
    results = [trainer.predict(c) for c in configs]
    return MultipleChoiceResult(unit, results)


def predict_army(trainer: GPRTrainer, army: Army):
    predictions = [predict_with_choices(trainer, u) for u in army.get_sorted_units()]
    build_army_markdown_file(army, predictions)

    print(get_markdown_prediction_table(predictions, army))
    # print(get_markdown_unit_table(army))
    return (army, predictions)


def training_set(unit: Unit) -> str:
    mapping = {
        UnitType.CHARACTER: "CHR",
        UnitType.INFANTRY: "INF",
        UnitType.LIGHT_VEHICLE: "V",
        UnitType.ARMORED_VEHICLE: "V",
        UnitType.AIRCRAFT: "AC",
        UnitType.AIRCRAFT_WAR_ENGINE: "AC",
        UnitType.WAR_ENGINE: "WE",
    }
    return mapping.get(unit.type, "OTHER")


# trainer = GPRSplitTrainer(mapper=universal_unit, splitter=training_set)
trainer = GPRTrainer(mapper=universal_unit)
trainer.train(ea_40k_units)
# trainer.validate()


results = [
    predict_army(trainer, solar_auxilia),
    predict_army(trainer, legiones_astartes),
]
build_prices_json_file(results)
build_army_json_files(results)
