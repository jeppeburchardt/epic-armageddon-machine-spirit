"""Markdown army file serializer."""

from __future__ import annotations

from pathlib import Path
from re import sub

from ea_unit_pricing.domain.army import Army
from ea_unit_pricing.domain.result import MultipleChoiceResult, Result
from ea_unit_pricing.serialization.markdown_table import get_markdown_prediction_table
from ea_unit_pricing.serialization.unit_stats_table import get_markdown_unit_table

__all__ = ["build_army_markdown_file", "kebab"]


def kebab(s: str) -> str:
    """Convert a string to kebab-case."""
    return "-".join(
        sub(
            r"(\s|_|-)+",
            " ",
            sub(
                r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+",
                lambda mo: " " + mo.group(0).lower(),
                s,
            ),
        ).split()
    )


def build_army_markdown_file(
    army: Army,
    result: list[Result | MultipleChoiceResult],
    output_dir: Path = Path("."),
) -> Path:
    """Write a markdown army file and return the path written."""
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"{kebab(army.name)}.md"
    with path.open("w", encoding="utf-8") as f:
        f.write(f"# {army.name}\n\n")
        f.write("## Predicted unit cost:\n\n")
        f.write(f"{get_markdown_prediction_table(result, army)}\n\n")
        f.write("## Unit stats:\n\n")
        f.write(f"{get_markdown_unit_table(army)}\n\n")
    return path
