from gpr.result import Result, quality_to_str
from tabulate import tabulate
from data.models import Army


def get_markdown_prediction_table(results: list[Result], army: Army) -> str:
    md = tabulate(
        map(
            lambda r: (
                r.unit.name,
                round(r.predicted_cost, 0),
                f"±{round(r.uncertainty, 0)}",
                quality_to_str(r.quality),
            ),
            results,
        ),
        headers=[
            "Name",
            "Predicted Cost",
            "Uncertainty",
            "Quality",
        ],
        tablefmt="github",
    )
    avg_score = sum(p.score for p in results) / len(results) if results else 0
    avg_uncert = sum(p.uncertainty for p in results) / len(results) if results else 0
    md += (
        f"\n\nAverage Score: {avg_score:.2f}\nAverage Uncertainty: {avg_uncert:.2f}\n\n"
    )
    return md
