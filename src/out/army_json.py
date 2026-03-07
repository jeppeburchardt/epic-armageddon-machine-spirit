import json

from models.units import Army
from models.result import Result, quality_to_str

from out.army_file import kebab


def build_prices_json_file(army_results: list[tuple[Army, list[Result]]]):
    output = {}
    for army, results in army_results:
        key = kebab(army.name)
        output[key] = {
            result.unit.name: {
                "cost": int(round(result.predicted_cost)),
                "uncertainty": int(round(result.uncertainty)),
                "quality": quality_to_str(result.quality),
            }
            for result in results
        }
    with open("prices.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)
