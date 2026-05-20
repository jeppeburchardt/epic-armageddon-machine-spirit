"""Tests for the Result and MultipleChoiceResult quality classification."""

from __future__ import annotations

import pytest

from ea_unit_pricing.domain import UnitType
from ea_unit_pricing.domain.enums import Quality
from ea_unit_pricing.domain.result import MultipleChoiceResult, Result
from ea_unit_pricing.domain.unit import Unit


def _unit() -> Unit:
    return Unit("X", 5, 1, UnitType.INFANTRY)


@pytest.mark.parametrize(
    "predicted_cost, uncertainty, expected_quality",
    [
        (100, 5, Quality.SAFE),  # uncertainty < 10
        (100, 8, Quality.SAFE),  # score 92 > 80
        # score=88 > 80 → SAFE even though uncertainty=12
        (100, 12, Quality.SAFE),
        # score=80 (NOT > 80), uncertainty=20 (NOT < 10), score > 70 → REVIEW
        (100, 20, Quality.REVIEW),
        # score=85 > 80 → SAFE
        (200, 30, Quality.SAFE),
        # score=50 NOT > 70, uncertainty=60 NOT < 15 → EXPERIMENTAL
        (100, 50, Quality.EXPERIMENTAL),
    ],
)
def test_result_quality(
    predicted_cost: float, uncertainty: float, expected_quality: Quality
) -> None:
    r = Result(_unit(), predicted_cost=predicted_cost, uncertainty=uncertainty)
    assert r.quality == expected_quality


def test_result_score_capped() -> None:
    r = Result(_unit(), predicted_cost=100, uncertainty=5)
    assert 0 <= r.score <= 100


def test_multiple_choice_result_best_is_max() -> None:
    results = [
        Result(_unit(), predicted_cost=80, uncertainty=5),
        Result(_unit(), predicted_cost=120, uncertainty=5),
    ]
    mcr = MultipleChoiceResult(_unit(), results)
    assert mcr.best_result.predicted_cost == 120


def test_multiple_choice_result_spread() -> None:
    results = [
        Result(_unit(), predicted_cost=100, uncertainty=5),
        Result(_unit(), predicted_cost=120, uncertainty=5),
    ]
    mcr = MultipleChoiceResult(_unit(), results)
    assert mcr.spread == pytest.approx(20 / 120)


def test_multiple_choice_result_wide_spread() -> None:
    results = [
        Result(_unit(), predicted_cost=100, uncertainty=5),
        Result(_unit(), predicted_cost=200, uncertainty=5),
    ]
    mcr = MultipleChoiceResult(_unit(), results)
    assert mcr.is_wide_spread


def test_multiple_choice_result_narrow_spread() -> None:
    results = [
        Result(_unit(), predicted_cost=100, uncertainty=5),
        Result(_unit(), predicted_cost=105, uncertainty=5),
    ]
    mcr = MultipleChoiceResult(_unit(), results)
    assert not mcr.is_wide_spread
