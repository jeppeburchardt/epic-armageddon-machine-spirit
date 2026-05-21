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
            assert generated_data == golden_data, f"JSON mismatch: {golden_file.name}"
        else:
            assert generated.read_text() == golden_file.read_text(), (
                f"Markdown mismatch: {golden_file.name}"
            )
