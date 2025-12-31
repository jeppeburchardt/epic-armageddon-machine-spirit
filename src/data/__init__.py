from .ea_40k_astartes import ea_40k_astartes_units
from .ea_40k_steel_legion import ea_40k_steel_legion_units
from .ea_40k_imperial_navy import ea_40k_imperial_navy_units
from .ea_40k_feral_orks import ea_40k_feral_orks
from .ea_40k_eldar import ea_40k_eldar
from .ea_40k_ork_war_horde import ea_40k_ork_war_horde

from .ea_hh_legion import ea_hh_legion_units
from .ea_hh_solar_aux import ea_hh_solar_aux

ea_40k_units = (
    ea_40k_astartes_units
    + ea_40k_steel_legion_units
    + ea_40k_imperial_navy_units
    + ea_40k_feral_orks
    + ea_40k_ork_war_horde
    + ea_40k_eldar
)
ea_hh_units = ea_hh_legion_units + ea_hh_solar_aux
