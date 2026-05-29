"""CLI entry point — ``eaup`` command."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated, Optional

import typer

from ea_unit_pricing.data import load_input_armies, load_training_units
from ea_unit_pricing.gpr.mapping.universal_unit import universal_unit
from ea_unit_pricing.gpr.trainer import GPRTrainer
from ea_unit_pricing.logging_setup import configure_logging
from ea_unit_pricing.pipeline.prediction import run_pipeline
from ea_unit_pricing.serialization.unit_stats_table import get_markdown_unit_table

app = typer.Typer(
    name="eaup",
    help="EA Unit Pricing — GPR-based point-cost predictor for Epic Armageddon.",
    no_args_is_help=True,
)

_ARMY_CHOICES = ["legiones-astartes", "solar-auxilia"]


@app.command()
def predict(
    armies: Annotated[
        Optional[list[str]],
        typer.Argument(help=f"Army slugs to predict: {', '.join(_ARMY_CHOICES)}"),
    ] = None,
    all_armies: Annotated[bool, typer.Option("--all", help="Predict all armies.")] = False,
    output_dir: Annotated[
        Path, typer.Option("--output-dir", "-o", help="Directory for output files.")
    ] = Path("output"),
    seed: Annotated[int, typer.Option("--seed", help="Random seed for reproducibility.")] = 42,
    verbose: Annotated[bool, typer.Option("--verbose", "-v", help="Enable debug logging.")] = False,
) -> None:
    """Predict point costs and write markdown + JSON output files."""
    configure_logging("DEBUG" if verbose else "INFO")

    training_units = load_training_units()

    if all_armies:
        targets = load_input_armies()
    else:
        if not armies:
            typer.echo("Specify army slugs or pass --all.", err=True)
            raise typer.Exit(code=1)
        all_input = {a.slug: a for a in load_input_armies()}
        missing = [slug for slug in armies if slug not in all_input]
        if missing:
            typer.echo(f"Unknown army slugs: {', '.join(missing)}", err=True)
            typer.echo(f"Available: {', '.join(all_input)}", err=True)
            raise typer.Exit(code=1)
        targets = [all_input[slug] for slug in armies]

    run_pipeline(targets, training_units, output_dir=output_dir, random_state=seed)
    typer.echo(f"Output written to {output_dir}/")


@app.command()
def validate(
    verbose: Annotated[bool, typer.Option("--verbose", "-v")] = False,
) -> None:
    """Run leave-one-out cross-validation on the training set."""
    configure_logging("DEBUG" if verbose else "INFO")

    training_units = load_training_units()
    trainer = GPRTrainer(mapper=universal_unit)
    trainer.train(training_units)
    result = trainer.validate()
    typer.echo(f"MAE: {result.get_mean_absolute_error():.2f} pts")
    typer.echo(f"Avg absolute error: {result.get_avg_absolute_error():.2f} pts")


@app.command()
def stats(
    army: Annotated[str, typer.Argument(help="Army slug.")],
    output_dir: Annotated[Path, typer.Option("--output-dir", "-o")] = Path("output"),
) -> None:
    """Write a unit stats markdown table for *army*."""
    configure_logging()

    all_armies = {a.slug: a for a in load_input_armies()}
    if army not in all_armies:
        typer.echo(f"Unknown army {army!r}. Available: {', '.join(all_armies)}", err=True)
        raise typer.Exit(code=1)

    output_dir.mkdir(parents=True, exist_ok=True)
    table = get_markdown_unit_table(all_armies[army])
    path = output_dir / f"{army}-stats.md"
    path.write_text(table, encoding="utf-8")
    typer.echo(f"Stats written to {path}")


if __name__ == "__main__":
    app()
