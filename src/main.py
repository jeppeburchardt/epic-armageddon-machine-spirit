from data import ea_40k_units, legiones_astartes, solar_auxilia
from gpr.trainer import GPRTrainer
from gpr.split_trainer import GPRSplitTrainer
from models.units import Army, Unit, UnitType
from gpr.mapping.universal_unit import universal_unit

# from out.unit_stats_table import get_markdown_unit_table
from out.prediction_table import get_markdown_prediction_table
from out.army_file import build_army_markdown_file


def predict_army(trainer: GPRTrainer, army: Army):
    predictions = [
        trainer.predict(u)
        # for u in filter(
        #     lambda x: x.type == UnitType.AIRCRAFT
        #     or x.type == UnitType.AIRCRAFT_WAR_ENGINE,
        #     army.get_sorted_units(),
        # )
        for u in army.get_sorted_units()
    ]
    build_army_markdown_file(army, predictions)

    print(get_markdown_prediction_table(predictions, army))
    # print(get_markdown_unit_table(army))


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


predict_army(trainer, solar_auxilia)

predict_army(trainer, legiones_astartes)
