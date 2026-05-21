"""Prediction pipeline — orchestrates GPR training and army prediction."""

from __future__ import annotations

import logging
from pathlib import Path

from ea_unit_pricing.domain.army import Army
from ea_unit_pricing.domain.result import MultipleChoiceResult, Result
from ea_unit_pricing.domain.unit import Unit
from ea_unit_pricing.gpr.mapping.universal_unit import universal_unit
from ea_unit_pricing.gpr.trainer import GPRTrainer
from ea_unit_pricing.serialization.army_json import build_prices_json_file
from ea_unit_pricing.serialization.army_list_json import build_army_json_files
from ea_unit_pricing.serialization.army_markdown import build_army_markdown_file

__all__ = ["predict_army", "predict_with_choices", "run_pipeline"]

logger = logging.getLogger(__name__)


def predict_with_choices(trainer: GPRTrainer, unit: Unit) -> Result | MultipleChoiceResult:
    """Predict cost for *unit*, expanding ``MultipleChoiceWeapon`` slots.

    Returns a plain ``Result`` when the unit has no choice weapons, or a
    ``MultipleChoiceResult`` wrapping predictions for every combination.
    """
    configs = unit.get_all_configurations()
    if len(configs) == 1:
        return trainer.predict(configs[0])
    results = [trainer.predict(c) for c in configs]
    return MultipleChoiceResult(unit, results)


def predict_army(
    trainer: GPRTrainer,
    army: Army,
    output_dir: Path = Path("."),
) -> tuple[Army, list[Result | MultipleChoiceResult]]:
    """Predict costs for all units in *army* and write a markdown file.

    Returns a ``(army, predictions)`` tuple suitable for passing to the JSON
    serializers.
    """
    predictions: list[Result | MultipleChoiceResult] = [
        predict_with_choices(trainer, u) for u in army.get_sorted_units()
    ]
    build_army_markdown_file(army, predictions, output_dir=output_dir)
    logger.info("Predicted %d units for %s", len(predictions), army.name)
    return army, predictions


def run_pipeline(
    armies: list[Army],
    training_units: list[Unit],
    output_dir: Path = Path("output"),
    random_state: int = 42,
) -> list[tuple[Army, list[Result | MultipleChoiceResult]]]:
    """Train a GPR model and predict costs for all *armies*.

    Args:
        armies: Armies to predict.
        training_units: Units with known costs used to fit the model.
        output_dir: Directory where output files are written.
        random_state: Seed for reproducible GPR results.

    Returns:
        List of ``(army, predictions)`` tuples.
    """
    trainer = GPRTrainer(mapper=universal_unit, random_state=random_state)
    logger.info("Training on %d units…", len(training_units))
    trainer.train(training_units)

    results = [predict_army(trainer, army, output_dir=output_dir) for army in armies]
    build_prices_json_file(results, output_dir=output_dir)
    build_army_json_files(results, output_dir=output_dir)
    return results
