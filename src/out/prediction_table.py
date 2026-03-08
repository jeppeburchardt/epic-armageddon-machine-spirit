from models.result import Result, MultipleChoiceResult, quality_to_str
from tabulate import tabulate
from models.units import Army


def _spread_str(result: Result) -> str:
    if not isinstance(result, MultipleChoiceResult):
        return ""
    label = f"{result.spread:.0%}"
    if result.is_wide_spread:
        label += " ⚠"
    return label


def _resolved(r):
    """Return (predicted_cost, uncertainty, quality) aligned with the JSON output.

    For MultipleChoiceResult the JSON uses the minimum-cost variant as the
    base price, so we do the same here.
    """
    if isinstance(r, MultipleChoiceResult):
        min_r = min(r.all_results, key=lambda x: x.predicted_cost)
        return min_r.predicted_cost, min_r.uncertainty, min_r.quality
    return r.predicted_cost, r.uncertainty, r.quality


def get_markdown_prediction_table(results: list[Result], army: Army) -> str:
    def _row(r):
        cost, uncertainty, quality = _resolved(r)
        if isinstance(r, MultipleChoiceResult):
            max_cost = round(max(x.predicted_cost for x in r.all_results), 0)
            cost_str = f"{round(cost, 0):.0f} - {max_cost:.0f}"
        else:
            cost_str = f"{round(cost, 0):.0f}"
        return (
            r.unit.name,
            cost_str,
            f"±{round(uncertainty, 0)}",
            quality_to_str(quality),
            _spread_str(r),
        )

    md = tabulate(
        map(_row, results),
        headers=[
            "Name",
            "Predicted Cost",
            "Uncertainty",
            "Quality",
            "Spread",
        ],
        tablefmt="github",
    )
    avg_score = sum(p.score for p in results) / len(results) if results else 0
    avg_uncert = sum(p.uncertainty for p in results) / len(results) if results else 0
    md += (
        f"\n\nAverage Score: {avg_score:.2f}\nAverage Uncertainty: {avg_uncert:.2f}\n\n"
    )
    return md
