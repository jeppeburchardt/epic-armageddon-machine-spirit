import json

from models.units import Army
from models.result import Result

from out.army_file import kebab


def build_prices_json_file(army_results: list[tuple[Army, list[Result]]]):
    output = {}
    for army, results in army_results:
        key = kebab(army.name)
        output[key] = {
            result.unit.name: {
                "cost": int(round(result.predicted_cost)),
                "uncertainty": int(round(result.uncertainty)),
            }
            for result in results
        }
    with open("prices.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)
