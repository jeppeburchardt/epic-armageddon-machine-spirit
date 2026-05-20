from __future__ import annotations

import math

from models.result import MultipleChoiceResult, Result


def rounding_step(cost: float) -> int:
    if cost < 100:
        return 5
    if cost < 200:
        return 10
    return 25


def round_points(cost: float) -> int:
    step = rounding_step(cost)
    return int(math.floor((cost / step) + 0.5) * step)


def resolved_base_result(result: Result | MultipleChoiceResult) -> Result:
    if isinstance(result, MultipleChoiceResult):
        return min(result.all_results, key=lambda item: item.predicted_cost)
    return result


def rounded_cost(result: Result | MultipleChoiceResult) -> int:
    return round_points(resolved_base_result(result).predicted_cost)


def rounded_choice_costs(result: MultipleChoiceResult) -> tuple[int, int]:
    min_result = min(result.all_results, key=lambda item: item.predicted_cost)
    max_result = max(result.all_results, key=lambda item: item.predicted_cost)
    return round_points(min_result.predicted_cost), round_points(
        max_result.predicted_cost
    )


def rounded_delta(base_cost: float, option_cost: float) -> int:
    return round_points(option_cost) - round_points(base_cost)
