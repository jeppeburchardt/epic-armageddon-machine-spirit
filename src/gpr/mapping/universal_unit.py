import numpy as np
from models.units import Unit

from .segments.stats import stats
from .segments.unit_type import unit_type
from .segments.fire_power import fire_power
from .segments.extra_damage import extra_damage
from .segments.trait_groups import trait_groups
from .segments.assault import assault
from .segments.range_bands import range_bands


def dice_test_to_score(dice_test: int) -> int:
    return (6 - dice_test) / 6


def universal_unit(unit: Unit) -> np.ndarray:
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
