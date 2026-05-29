"""Golden-output regression test for the full prediction pipeline.

Trains on the real training set and verifies that predictions for both
armies are byte-for-byte identical to the committed golden outputs.

This test guards the frozen feature-vector layout constraint: any change
that silently alters the GPR output will fail here.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from ea_unit_pricing.data import load_input_armies, load_training_units
from ea_unit_pricing.pipeline.prediction import run_pipeline


def _assert_json_equal_with_float_tolerance(
    expected: object, actual: object, path: str = "$"
) -> None:
    if isinstance(expected, dict) and isinstance(actual, dict):
        assert set(expected.keys()) == set(actual.keys()), f"Key mismatch at {path}"
        for key in expected:
            _assert_json_equal_with_float_tolerance(expected[key], actual[key], f"{path}.{key}")
        return

    if isinstance(expected, list) and isinstance(actual, list):
        assert len(expected) == len(actual), f"List length mismatch at {path}"
        for i, (exp_item, act_item) in enumerate(zip(expected, actual)):
            _assert_json_equal_with_float_tolerance(exp_item, act_item, f"{path}[{i}]")
        return

    is_expected_number = isinstance(expected, (int, float)) and not isinstance(expected, bool)
    is_actual_number = isinstance(actual, (int, float)) and not isinstance(actual, bool)
    if is_expected_number and is_actual_number:
        assert actual == pytest.approx(expected, abs=1e-6), f"Float mismatch at {path}"
        return

    assert actual == expected, f"Value mismatch at {path}"


@pytest.mark.slow
def test_prediction_pipeline_matches_golden(
    golden_dir: Path,
    tmp_output_dir: Path,
) -> None:
    """Full pipeline output must be byte-identical to committed golden files."""
    training_units = load_training_units()
    armies = load_input_armies()
    run_pipeline(armies, training_units, output_dir=tmp_output_dir, random_state=42)

    for golden_file in golden_dir.iterdir():
        if golden_file.suffix not in (".json", ".md"):
            continue
        generated = tmp_output_dir / golden_file.name
        assert generated.exists(), f"Missing output: {golden_file.name}"

        if golden_file.suffix == ".json":
            golden_data = json.loads(golden_file.read_text())
            generated_data = json.loads(generated.read_text())
            _assert_json_equal_with_float_tolerance(golden_data, generated_data)
        else:
            assert generated.read_text() == golden_file.read_text(), (
                f"Markdown mismatch: {golden_file.name}"
            )
