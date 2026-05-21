"""JSON prices-file serializer."""

from __future__ import annotations

import json
from itertools import product as cartesian_product
from pathlib import Path

from ea_unit_pricing.domain.army import Army
from ea_unit_pricing.domain.enums import quality_to_str, trait_to_string, unit_type_to_string
from ea_unit_pricing.domain.result import MultipleChoiceResult, Result
from ea_unit_pricing.domain.weapons import (
    AssaultWeapon,
    MultipleChoiceWeapon,
    Multiplier,
    RangedWeapon,
    SmallArms,
)
from ea_unit_pricing.serialization.army_markdown import kebab
from ea_unit_pricing.serialization.rounding import rounded_cost, rounded_delta

__all__ = ["build_prices_json_file"]


def _firepower_dict(weapon: RangedWeapon) -> dict[str, object]:
    fp: dict[str, object] = {}
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


def weapon_to_dict(weapon: object) -> dict[str, object]:
    """Serialise any weapon type to a JSON-compatible dict."""
    if isinstance(weapon, Multiplier):
        result = weapon_to_dict(weapon.weapon)
        result["count"] = weapon.times
        return result
    if isinstance(weapon, RangedWeapon):
        d: dict[str, object] = {
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


def _unit_profile_dict(unit: object) -> dict[str, object]:
    profile: dict[str, object] = {
        "type": unit_type_to_string(unit.type),  # type: ignore[attr-defined]
        "speed": unit.unit_speed_to_string(),  # type: ignore[attr-defined]
        "armour": unit.armour,  # type: ignore[attr-defined]
        "cc": unit.cc,  # type: ignore[attr-defined]
        "ff": unit.ff,  # type: ignore[attr-defined]
        "traits": [trait_to_string(t) for t in unit.traits],  # type: ignore[attr-defined]
    }
    if unit.damage_capacity > 1:  # type: ignore[attr-defined]
        profile["damage_capacity"] = unit.damage_capacity  # type: ignore[attr-defined]
    if unit.void_shields > 0:  # type: ignore[attr-defined]
        profile["void_shields"] = unit.void_shields  # type: ignore[attr-defined]
    if unit.transport_capacity > 0:  # type: ignore[attr-defined]
        profile["transport_capacity"] = unit.transport_capacity  # type: ignore[attr-defined]
    return profile


def _weapons_for_choice_result(result: MultipleChoiceResult) -> list[object]:
    original_unit = result.original_unit
    all_results = result.all_results
    min_cost = min(r.predicted_cost for r in all_results)

    choice_positions = [
        i for i, w in enumerate(original_unit.weapons) if isinstance(w, MultipleChoiceWeapon)
    ]
    option_lists = [original_unit.weapons[i].options for i in choice_positions]  # type: ignore[union-attr]
    combos = list(cartesian_product(*option_lists))

    weapons: list[object] = []
    for i, w in enumerate(original_unit.weapons):
        if not isinstance(w, MultipleChoiceWeapon):
            weapons.append(weapon_to_dict(w))
        else:
            slot_idx = choice_positions.index(i)
            choice_list = []
            for option in w.options:
                matching = [j for j, combo in enumerate(combos) if combo[slot_idx] is option]
                avg_cost = (
                    sum(all_results[j].predicted_cost for j in matching) / len(matching)
                    if matching
                    else 0.0
                )
                delta = rounded_delta(min_cost, avg_cost)
                opt_dict = weapon_to_dict(option)
                opt_dict["cost_delta"] = delta
                choice_list.append(opt_dict)
            weapons.append({"name": w.name, "options": choice_list})
    return weapons


def build_prices_json_file(
    army_results: list[tuple[Army, list[Result | MultipleChoiceResult]]],
    output_dir: Path = Path("."),
) -> Path:
    """Write ``prices.json`` to *output_dir* and return the path."""
    output_dir.mkdir(parents=True, exist_ok=True)
    output: dict[str, object] = {}
    for army, results in army_results:
        key = kebab(army.name)
        army_output: dict[str, object] = {}
        for result in results:
            if isinstance(result, MultipleChoiceResult):
                min_result = min(result.all_results, key=lambda r: r.predicted_cost)
                entry: dict[str, object] = {
                    "cost": rounded_cost(result),
                    "uncertainty": int(round(min_result.uncertainty)),
                    "quality": quality_to_str(min_result.quality),
                    "unit_profile": _unit_profile_dict(result.original_unit),
                    "weapons": _weapons_for_choice_result(result),
                }
            else:
                entry = {
                    "cost": rounded_cost(result),
                    "uncertainty": int(round(result.uncertainty)),
                    "quality": quality_to_str(result.quality),
                    "unit_profile": _unit_profile_dict(result.unit),
                    "weapons": [weapon_to_dict(w) for w in result.unit.weapons],
                }
            army_output[result.unit.name] = entry
        output[key] = army_output

    path = output_dir / "prices.json"
    with path.open("w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    return path
