"""Markdown prediction table serializer."""

from __future__ import annotations

from tabulate import tabulate

from ea_unit_pricing.domain.enums import quality_to_str
from ea_unit_pricing.domain.result import MultipleChoiceResult, Result
from ea_unit_pricing.serialization.rounding import rounded_choice_costs, rounded_cost

__all__ = ["get_markdown_prediction_table"]


def _spread_str(result: Result | MultipleChoiceResult) -> str:
    if not isinstance(result, MultipleChoiceResult):
        return ""
    label = f"{result.spread:.0%}"
    if result.is_wide_spread:
        label += " ⚠"
    return label


def _resolved(r: Result | MultipleChoiceResult) -> tuple[float, float, object]:
    """Return (predicted_cost, uncertainty, quality) aligned with the JSON output."""
    if isinstance(r, MultipleChoiceResult):
        min_r = min(r.all_results, key=lambda x: x.predicted_cost)
        return min_r.predicted_cost, min_r.uncertainty, min_r.quality
    return r.predicted_cost, r.uncertainty, r.quality


def get_markdown_prediction_table(
    results: list[Result | MultipleChoiceResult],
    army: object,
) -> str:
    """Return a GitHub-flavoured markdown table of predicted costs."""

    def _row(r: Result | MultipleChoiceResult) -> tuple[str, str, str, str, str]:
        cost, uncertainty, quality = _resolved(r)
        if isinstance(r, MultipleChoiceResult):
            rounded_min_cost, rounded_max_cost = rounded_choice_costs(r)
            cost_str = f"{rounded_min_cost} - {rounded_max_cost}"
        else:
            cost_str = str(rounded_cost(r))
        return (
            r.unit.name,
            cost_str,
            f"±{round(uncertainty, 0)}",
            quality_to_str(quality),  # type: ignore[arg-type]
            _spread_str(r),
        )

    md = tabulate(
        map(_row, results),
        headers=["Name", "Predicted Cost", "Uncertainty", "Quality", "Spread"],
        tablefmt="github",
    )
    avg_score = sum(p.score for p in results) / len(results) if results else 0
    avg_uncert = sum(p.uncertainty for p in results) / len(results) if results else 0
    md += f"\n\nAverage Score: {avg_score:.2f}\nAverage Uncertainty: {avg_uncert:.2f}\n\n"
    return md
