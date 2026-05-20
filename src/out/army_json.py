import json
from itertools import product as cartesian_product

from models.units import (
    Army,
    RangedWeapon,
    AssaultWeapon,
    SmallArms,
    Multiplier,
    MultipleChoiceWeapon,
    trait_to_string,
    unit_type_to_string,
)
from models.result import Result, MultipleChoiceResult, quality_to_str

from out.army_file import kebab
from out.rounding import rounded_cost, rounded_delta


def _firepower_dict(weapon: RangedWeapon) -> dict:
    fp = {}
    if weapon.at > 0:
        fp["at"] = f"{weapon.at}+"
    if weapon.ap > 0:
        fp["ap"] = f"{weapon.ap}+"
    if weapon.mw > 0:
        fp["mw"] = f"{weapon.mw}+"
    if weapon.aa > 0:
        fp["aa"] = f"{weapon.aa}+"
    if weapon.bp > 0:
        fp["bp"] = weapon.bp
    return fp


def weapon_to_dict(weapon) -> dict:
    if isinstance(weapon, Multiplier):
        d = weapon_to_dict(weapon.weapon)
        d["count"] = weapon.times
        return d
    if isinstance(weapon, RangedWeapon):
        d = {
            "name": weapon.name,
            "type": "Ranged Weapon",
            "range": weapon.range,
            "firepower": _firepower_dict(weapon),
            "traits": list(map(trait_to_string, weapon.traits)),
        }
        if weapon.stat_modifiers:
            d["unit_stat_modifiers"] = weapon.stat_modifiers
        return d
    if isinstance(weapon, AssaultWeapon):
        return {
            "name": weapon.name,
            "type": "Assault Weapons",
            "range": "(bc)",
            "traits": list(map(trait_to_string, weapon.traits)),
        }
    if isinstance(weapon, SmallArms):
        return {
            "name": weapon.name,
            "type": "Small Arms",
            "range": "(15cm)",
            "traits": list(map(trait_to_string, weapon.traits)),
        }
    if isinstance(weapon, MultipleChoiceWeapon):
        return {
            "name": str(weapon.name),
            "options": [weapon_to_dict(o) for o in weapon.options],
        }
    return {"name": str(weapon)}


def unit_profile_dict(unit) -> dict:
    profile = {
        "type": unit_type_to_string(unit.type),
        "speed": unit.unit_speed_to_string(),
        "armour": unit.armour,
        "cc": unit.cc,
        "ff": unit.ff,
        "traits": [trait_to_string(t) for t in unit.traits],
    }
    if unit.damage_capacity > 1:
        profile["damage_capacity"] = unit.damage_capacity
    if unit.void_shields > 0:
        profile["void_shields"] = unit.void_shields
    if unit.transport_capacity > 0:
        profile["transport_capacity"] = unit.transport_capacity
    return profile


def _weapons_for_choice_result(result: MultipleChoiceResult) -> list:
    original_unit = result.original_unit
    all_results = result.all_results
    min_cost = min(r.predicted_cost for r in all_results)

    choice_positions = [
        i
        for i, w in enumerate(original_unit.weapons)
        if isinstance(w, MultipleChoiceWeapon)
    ]
    option_lists = [original_unit.weapons[i].options for i in choice_positions]
    combos = list(cartesian_product(*option_lists))

    weapons = []
    for i, w in enumerate(original_unit.weapons):
        if not isinstance(w, MultipleChoiceWeapon):
            weapons.append(weapon_to_dict(w))
        else:
            slot_idx = choice_positions.index(i)
            choice_list = []
            for option in w.options:
                matching = [
                    j for j, combo in enumerate(combos) if combo[slot_idx] is option
                ]
                if matching:
                    avg_cost = sum(
                        all_results[j].predicted_cost for j in matching
                    ) / len(matching)
                    delta = rounded_delta(min_cost, avg_cost)
                else:
                    delta = 0
                opt_dict = weapon_to_dict(option)
                opt_dict["cost_delta"] = delta
                choice_list.append(opt_dict)
            weapons.append({"name": w.name, "options": choice_list})
    return weapons


def build_prices_json_file(army_results: list[tuple[Army, list[Result]]]):
    output = {}
    for army, results in army_results:
        key = kebab(army.name)
        army_output = {}
        for result in results:
            if isinstance(result, MultipleChoiceResult):
                min_result = min(result.all_results, key=lambda r: r.predicted_cost)
                entry = {
                    "cost": rounded_cost(result),
                    "uncertainty": int(round(min_result.uncertainty)),
                    "quality": quality_to_str(min_result.quality),
                    "unit_profile": unit_profile_dict(result.original_unit),
                    "weapons": _weapons_for_choice_result(result),
                }
            else:
                entry = {
                    "cost": rounded_cost(result),
                    "uncertainty": int(round(result.uncertainty)),
                    "quality": quality_to_str(result.quality),
                    "unit_profile": unit_profile_dict(result.unit),
                    "weapons": [weapon_to_dict(w) for w in result.unit.weapons],
                }
            army_output[result.unit.name] = entry
        output[key] = army_output
    with open("prices.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
