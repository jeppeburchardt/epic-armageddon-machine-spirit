"""Vector layout snapshot test — guards the frozen feature-vector constraint.

For representative units, verifies that ``universal_unit()`` produces
the exact same ``np.ndarray`` shape and values as when the golden outputs
were generated.  Any change to segment order or dimensions will fail here.
"""

from __future__ import annotations

import numpy as np
import pytest

from ea_unit_pricing.domain import RangedWeapon, Traits, Unit, UnitType
from ea_unit_pricing.gpr.mapping.universal_unit import universal_unit


def test_vector_length() -> None:
    """Feature vector must always have exactly 30 elements."""
    unit = Unit("X", 5, 1, UnitType.INFANTRY, speed=15, armour=4, cc=4, ff=4)
    v = universal_unit(unit)
    assert v.shape == (30,), f"Expected 30 features, got {v.shape}"


@pytest.mark.parametrize(
    "unit, expected_vector",
    [
        (
            # Bare infantry — no weapons, no traits, all stats 0
            Unit("Bare", 5, 1, UnitType.INFANTRY),
            np.array(
                [
                    # stats (9): SR, ini, speed, armour, ff, cc, DC, VS, TC
                    # armour=0, ff=0, cc=0 → dice_test_to_score(0) = 1.0
                    5,
                    5 / 6,
                    0,
                    1.0,
                    1.0,
                    1.0,
                    1,
                    0,
                    0,
                    # unit_type (4): inf/char, vehicle, WE, aircraft
                    1,
                    0,
                    0,
                    0,
                    # range_bands (4)
                    0,
                    0,
                    0,
                    0,
                    # fire_power (5)
                    0,
                    0,
                    0,
                    0,
                    0,
                    # extra_damage (2)
                    0,
                    0,
                    # trait_groups (5)
                    0,
                    0,
                    0,
                    0,
                    0,
                    # assault (1)
                    0,
                ],
                dtype=float,
            ),
        ),
    ],
)
def test_vector_values(unit: Unit, expected_vector: np.ndarray) -> None:
    v = universal_unit(unit)
    np.testing.assert_allclose(v, expected_vector, rtol=1e-6)


def test_vector_ranged_weapon_at() -> None:
    """AT weapon at 45cm should increment the mid-range band and AT firepower."""
    unit = Unit(
        "Armed",
        5,
        1,
        UnitType.INFANTRY,
        weapons=[RangedWeapon(45, at=5, name="Lascannon")],
    )
    v = universal_unit(unit)
    # range_bands[2] = 30 < range < 50
    assert v[15] == 1, "Should have 1 weapon in 30-50cm band"
    # fire_power[0] = AT score
    assert v[17] == pytest.approx((6 - 5) / 6)


def test_vector_know_no_fear_trait() -> None:
    unit = Unit(
        "KNF",
        5,
        1,
        UnitType.INFANTRY,
        traits=[Traits.KNOW_NO_FEAR],
    )
    v = universal_unit(unit)
    # trait_groups layout: [ranged_traits, mobility, survivability, know_no_fear, walker]
    # indices 24-28; KNOW_NO_FEAR is at trait_groups[3] = index 27
    assert v[27] == 1
