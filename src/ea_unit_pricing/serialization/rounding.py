"""Tiered point-rounding policy for predicted costs."""

from __future__ import annotations

import math

from ea_unit_pricing.domain.result import MultipleChoiceResult, Result

__all__ = [
    "round_points",
    "rounded_choice_costs",
    "rounded_cost",
    "rounded_delta",
    "rounding_step",
]


def rounding_step(cost: float) -> int:
    """Return the rounding granularity for a given cost value."""
    if cost < 100:
        return 5
    if cost < 200:
        return 10
    return 25


def round_points(cost: float) -> int:
    """Round *cost* to the nearest tier step (5 / 10 / 25 depending on magnitude)."""
    step = rounding_step(cost)
    return int(math.floor((cost / step) + 0.5) * step)


def _resolved_base_result(result: Result | MultipleChoiceResult) -> Result:
    if isinstance(result, MultipleChoiceResult):
        return min(result.all_results, key=lambda item: item.predicted_cost)
    return result


def rounded_cost(result: Result | MultipleChoiceResult) -> int:
    """Return the rounded base cost for *result*."""
    return round_points(_resolved_base_result(result).predicted_cost)


def rounded_choice_costs(result: MultipleChoiceResult) -> tuple[int, int]:
    """Return (min_rounded_cost, max_rounded_cost) for all variants."""
    min_result = min(result.all_results, key=lambda item: item.predicted_cost)
    max_result = max(result.all_results, key=lambda item: item.predicted_cost)
    return round_points(min_result.predicted_cost), round_points(max_result.predicted_cost)


def rounded_delta(base_cost: float, option_cost: float) -> int:
    """Return the rounded cost difference between two variants."""
    return round_points(option_cost) - round_points(base_cost)
