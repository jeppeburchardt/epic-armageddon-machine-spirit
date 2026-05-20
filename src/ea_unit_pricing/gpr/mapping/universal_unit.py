"""Universal unit feature vector.

**IMPORTANT — frozen layout constraint:**
The order of segments in ``universal_unit()`` is baked into any trained model.
Do *not* change the concatenation order or add/remove segments without
retraining and regenerating the golden outputs.
"""

from __future__ import annotations

import numpy as np

from ea_unit_pricing.domain.unit import Unit
from ea_unit_pricing.gpr.mapping.segments.assault import assault
from ea_unit_pricing.gpr.mapping.segments.extra_damage import extra_damage
from ea_unit_pricing.gpr.mapping.segments.fire_power import fire_power
from ea_unit_pricing.gpr.mapping.segments.range_bands import range_bands
from ea_unit_pricing.gpr.mapping.segments.stats import stats
from ea_unit_pricing.gpr.mapping.segments.trait_groups import trait_groups
from ea_unit_pricing.gpr.mapping.segments.unit_type import unit_type

__all__ = ["dice_test_to_score", "universal_unit"]


def dice_test_to_score(dice_test: int) -> float:
    """Convert a D6 roll-or-more target to a normalised score (0–1).

    Lower dice targets (better stats) produce higher scores.
    """
    return (6 - dice_test) / 6


def universal_unit(unit: Unit) -> np.ndarray:
    """Return the feature vector for *unit* used by the GPR model.

    Segment order (frozen):
    1. stats        — 9 features
    2. unit_type    — 4 features (one-hot)
    3. range_bands  — 4 features
    4. fire_power   — 5 features
    5. extra_damage — 2 features
    6. trait_groups — 5 features
    7. assault      — 1 feature
    """
    vector = (
        stats(unit)
        + unit_type(unit)
        + range_bands(unit)
        + fire_power(unit)
        + extra_damage(unit)
        + trait_groups(unit)
        + assault(unit)
    )
    return np.array(vector)
