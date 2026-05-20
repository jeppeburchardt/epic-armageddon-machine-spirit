"""Data package — lazy loaders for training and input army data.

Use ``load_training_units()`` and ``load_input_armies()`` instead of
importing the raw module-level lists directly.  This keeps data loading
explicit and avoids import-time side effects.
"""

from __future__ import annotations

from ea_unit_pricing.domain.army import Army
from ea_unit_pricing.domain.unit import Unit

__all__ = ["load_input_armies", "load_training_units"]


def load_training_units() -> list[Unit]:
    """Return all training units from the Epic Armageddon 40K catalogues."""
    from ea_unit_pricing.data.training.ea_40k_astartes import ea_40k_astartes_units
    from ea_unit_pricing.data.training.ea_40k_dark_eldar import ea_40k_dark_eldar_units
    from ea_unit_pricing.data.training.ea_40k_eldar import ea_40k_eldar
    from ea_unit_pricing.data.training.ea_40k_feral_orks import ea_40k_feral_orks
    from ea_unit_pricing.data.training.ea_40k_imperial_navy import ea_40k_imperial_navy_units
    from ea_unit_pricing.data.training.ea_40k_minervan import minervan
    from ea_unit_pricing.data.training.ea_40k_ork_war_horde import ea_40k_ork_war_horde
    from ea_unit_pricing.data.training.ea_40k_steel_legion import ea_40k_steel_legion_units
    from ea_unit_pricing.data.training.ea_40k_tyranid import tyranids
    from ea_unit_pricing.data.training.epic_uk_squats import squats

    return (
        ea_40k_astartes_units
        + ea_40k_steel_legion_units
        + ea_40k_imperial_navy_units
        + ea_40k_feral_orks
        + ea_40k_ork_war_horde
        + ea_40k_eldar
        + ea_40k_dark_eldar_units
        + squats.get_sorted_units()
        + minervan.get_sorted_units()
        + tyranids.get_sorted_units()
    )


def load_input_armies() -> list[Army]:
    """Return armies whose costs are to be predicted."""
    from ea_unit_pricing.data.input.ea_hh_legion import legiones_astartes
    from ea_unit_pricing.data.input.ea_hh_solar_aux import solar_auxilia

    return [solar_auxilia, legiones_astartes]
