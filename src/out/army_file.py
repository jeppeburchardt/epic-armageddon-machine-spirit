from re import sub

from data.models import Army
from gpr.result import Result

from out.unit_stats_table import get_markdown_unit_table
from out.prediction_table import get_markdown_prediction_table


def kebab(s):
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


def build_army_markdown_file(army: Army, result: list[Result]):
    filename = f"{kebab(army.name)}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {army.name}\n\n")
        f.write("## Predicted unit cost:\n\n")
        f.write(f"{get_markdown_prediction_table(result, army)}\n\n")
        f.write("## Unit stats:\n\n")
        f.write(f"{get_markdown_unit_table(army)}\n\n")
