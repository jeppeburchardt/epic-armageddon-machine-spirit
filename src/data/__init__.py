from .training.ea_40k_astartes import ea_40k_astartes_units
from .training.ea_40k_steel_legion import ea_40k_steel_legion_units
from .training.ea_40k_imperial_navy import ea_40k_imperial_navy_units
from .training.ea_40k_feral_orks import ea_40k_feral_orks
from .training.ea_40k_eldar import ea_40k_eldar
from .training.ea_40k_ork_war_horde import ea_40k_ork_war_horde
from .training.epic_uk_squats import squats
from .training.ea_40k_minervan import minervan

from .input.ea_hh_legion import legiones_astartes
from .input.ea_hh_solar_aux import solar_auxilia

ea_40k_units = (
    ea_40k_astartes_units
    + ea_40k_steel_legion_units
    + ea_40k_imperial_navy_units
    + ea_40k_feral_orks
    + ea_40k_ork_war_horde
    + ea_40k_eldar
    + squats.get_sorted_units()
    + minervan.get_sorted_units()
)
