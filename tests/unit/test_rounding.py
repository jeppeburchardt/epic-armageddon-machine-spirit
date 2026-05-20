"""Unit tests for the tiered point-rounding policy."""

from __future__ import annotations

import pytest

from ea_unit_pricing.domain import UnitType
from ea_unit_pricing.domain.unit import Unit
from ea_unit_pricing.domain.result import MultipleChoiceResult, Result
from ea_unit_pricing.serialization.rounding import (
    round_points,
    rounded_choice_costs,
    rounded_cost,
    rounded_delta,
    rounding_step,
)


def _make_unit(name: str = "X") -> Unit:
    return Unit(name, strategy_rating=5, initiative=1, type=UnitType.INFANTRY)


def _make_result(cost: float, uncertainty: float = 5.0) -> Result:
    return Result(_make_unit(), predicted_cost=cost, uncertainty=uncertainty)


@pytest.mark.parametrize(
    "cost, expected_step",
    [
        (0, 5),
        (50, 5),
        (99, 5),
        (100, 10),
        (150, 10),
        (199, 10),
        (200, 25),
        (500, 25),
    ],
)
def test_rounding_step(cost: float, expected_step: int) -> None:
    assert rounding_step(cost) == expected_step


@pytest.mark.parametrize(
    "cost, expected_rounded",
    [
        (0, 0),
        (12, 10),
        (13, 15),
        (97, 95),
        (103, 100),
        (115, 120),
        (205, 200),
        # 212 rounds to nearest 25 = 200 (diff 12 vs diff 13)
        (212, 200),
        # 213 rounds to nearest 25 = 225 (diff 13 vs diff 12)
        (213, 225),
    ],
)
def test_round_points(cost: float, expected_rounded: int) -> None:
    assert round_points(cost) == expected_rounded


def test_rounded_cost_plain_result() -> None:
    result = _make_result(113.0)
    assert rounded_cost(result) == 110


def test_rounded_cost_choice_result_uses_min() -> None:
    unit = _make_unit("Multi")
    results = [_make_result(100.0), _make_result(130.0)]
    mcr = MultipleChoiceResult(unit, results)
    # rounded_cost uses the MIN variant (base cost)
    assert rounded_cost(mcr) == 100


def test_rounded_choice_costs() -> None:
    unit = _make_unit("Multi")
    results = [_make_result(88.0), _make_result(112.0)]
    mcr = MultipleChoiceResult(unit, results)
    min_c, max_c = rounded_choice_costs(mcr)
    assert min_c == 90
    assert max_c == 110


def test_rounded_delta() -> None:
    assert rounded_delta(100.0, 125.0) == 30
    assert rounded_delta(90.0, 90.0) == 0


def test_choice_surcharges_are_derived_from_rounded_totals() -> None:
    unit = _make_unit("Multi")
    min_cost, max_cost = 195.0, 210.0
    results = [_make_result(min_cost), _make_result(max_cost)]
    mcr = MultipleChoiceResult(unit, results)
    min_c, max_c = rounded_choice_costs(mcr)
    # 195 rounds to 200 (nearest 25 >= 200)
    assert min_c == 200
    # 210 rounds to 200 (|210-200|=10 < |210-225|=15)
    assert max_c == 200
