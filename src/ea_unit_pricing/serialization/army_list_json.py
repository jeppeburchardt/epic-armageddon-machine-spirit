"""Army list JSON serializer."""

from __future__ import annotations

import json
from itertools import product as cartesian_product
from pathlib import Path

from ea_unit_pricing.domain.army import (
    Army,
    MaxGroupPercentage,
    MinGroupPercentage,
    Restriction,
    UpgradeAdd,
    UpgradeCharacter,
    UpgradeReplace,
)
from ea_unit_pricing.domain.enums import quality_to_str, trait_to_string, unit_type_to_string
from ea_unit_pricing.domain.result import MultipleChoiceResult, Result
from ea_unit_pricing.domain.weapons import (
    AssaultWeapon,
    MultipleChoiceWeapon,
    Multiplier,
    RangedWeapon,
    SmallArms,
)
from ea_unit_pricing.serialization.rounding import rounded_cost, rounded_delta

__all__ = ["build_army_json_files"]


def _firepower_str(weapon: RangedWeapon) -> str:
    fp: list[str] = []
    traits = list(map(trait_to_string, weapon.traits))
    if weapon.at > 0:
        fp.append(f"AT{weapon.at}+")
    if weapon.ap > 0:
        fp.append(f"AP{weapon.ap}+")
    if weapon.mw > 0:
        fp.append(f"MW{weapon.mw}+")
    if weapon.aa > 0:
        fp.append(f"AA{weapon.aa}+")
    if weapon.bp > 0:
        fp.append(f"{weapon.bp}BP")
    return " ".join([*fp, *traits])


def _weapon_to_dict(weapon: object) -> dict[str, object]:
    if isinstance(weapon, Multiplier):
        result = _weapon_to_dict(weapon.weapon)
        result["count"] = weapon.times
        return result
    if isinstance(weapon, RangedWeapon):
        d: dict[str, object] = {
            "weaponName": weapon.name,
            "type": "Ranged Weapon",
            "range": f"{weapon.range}cm",
            "firepower": _firepower_str(weapon),
        }
        if weapon.stat_modifiers:
            d["unitStatModifiers"] = weapon.stat_modifiers
        return d
    if isinstance(weapon, AssaultWeapon):
        return {
            "weaponName": weapon.name,
            "type": "Assault Weapons",
            "range": "(bc)",
            "firepower": " ".join(list(map(trait_to_string, weapon.traits))),
        }
    if isinstance(weapon, SmallArms):
        return {
            "weaponName": weapon.name,
            "type": "Small Arms",
            "range": "(15cm)",
            "firepower": " ".join(list(map(trait_to_string, weapon.traits))),
        }
    if isinstance(weapon, MultipleChoiceWeapon):
        return {
            "weaponName": str(weapon.name),
            "options": [_weapon_to_dict(o) for o in weapon.options],
        }
    return {"name": str(weapon)}


def _restriction_to_dict(restriction: Restriction) -> dict[str, object]:
    d: dict[str, object] = {"type": restriction.type, "group": restriction.group}
    if isinstance(restriction, MaxGroupPercentage):
        d["maxPercentage"] = restriction.maxPercentage
    if isinstance(restriction, MinGroupPercentage):
        d["minPercentage"] = restriction.minPercentage
    return d


def _dice_stat(v: int) -> str:
    if not v:
        return "-"
    return f"{v}+"


def _unit_profile_dict(unit: object) -> dict[str, object]:
    profile: dict[str, object] = {
        "type": unit_type_to_string(unit.type),  # type: ignore[attr-defined]
        "speed": unit.unit_speed_to_string(),  # type: ignore[attr-defined]
        "armour": _dice_stat(unit.armour),  # type: ignore[attr-defined]
        "cc": _dice_stat(unit.cc),  # type: ignore[attr-defined]
        "ff": _dice_stat(unit.ff),  # type: ignore[attr-defined]
        "traits": [trait_to_string(t) for t in unit.traits],  # type: ignore[attr-defined]
    }
    if unit.damage_capacity > 1:  # type: ignore[attr-defined]
        profile["damageCapacity"] = unit.damage_capacity  # type: ignore[attr-defined]
    if unit.void_shields > 0:  # type: ignore[attr-defined]
        profile["voidShields"] = unit.void_shields  # type: ignore[attr-defined]
    if unit.transport_capacity > 0:  # type: ignore[attr-defined]
        profile["transportation"] = {
            "capacity": unit.transport_capacity,  # type: ignore[attr-defined]
            "capabilities": unit.transport_capabilities,  # type: ignore[attr-defined]
        }
    if unit.transport_cost > 0:  # type: ignore[attr-defined]
        profile["transportation"] = {
            "cost": unit.transport_cost,  # type: ignore[attr-defined]
            "type": unit.transport_type,  # type: ignore[attr-defined]
        }
    return profile


def _weapon_slots(result: MultipleChoiceResult) -> list[dict[str, object]]:
    original_unit = result.original_unit
    all_results = result.all_results
    min_cost = min(r.predicted_cost for r in all_results)

    choice_positions = [
        i for i, w in enumerate(original_unit.weapons) if isinstance(w, MultipleChoiceWeapon)
    ]
    option_lists = [original_unit.weapons[i].options for i in choice_positions]  # type: ignore[union-attr]
    combos = list(cartesian_product(*option_lists))

    weapon_slots: list[dict[str, object]] = []
    for i, w in enumerate(original_unit.weapons):
        if not isinstance(w, MultipleChoiceWeapon):
            weapon_slots.append({"kind": "fixed", **_weapon_to_dict(w)})
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
                opt_dict = _weapon_to_dict(option)
                opt_dict["additionalCost"] = delta
                choice_list.append(opt_dict)
            weapon_slots.append({"kind": "choice", "name": w.name, "choices": choice_list})
    return weapon_slots


def _result_to_dict(result: Result | MultipleChoiceResult) -> dict[str, object]:
    def _gpr_training_info(r: Result) -> dict[str, object]:
        return {
            "predictedMean": r.predicted_cost,
            "uncertainty": r.uncertainty,
            "score": r.score,
            "quality": quality_to_str(r.quality),
            "topNearestNeighbours": [
                {"name": name, "price": price, "distance": distance}
                for name, price, distance in r.nearest_neighbours
            ],
            "contributingPriceValues": r.training_price_values,
            "trainingSetSize": r.training_set_size,
            "modelKernel": r.model_kernel,
        }

    if isinstance(result, MultipleChoiceResult):
        return {
            "name": result.unit.name,
            "cost": rounded_cost(result),
            "weaponSlots": _weapon_slots(result),
            "gprTrainingInfo": _gpr_training_info(result.best_result),
            **_unit_profile_dict(result.original_unit),
        }
    return {
        "name": result.unit.name,
        "cost": rounded_cost(result),
        "uncertainty": round(result.uncertainty),
        "quality": quality_to_str(result.quality),
        "weaponSlots": [{"kind": "fixed", **_weapon_to_dict(w)} for w in result.unit.weapons],
        "gprTrainingInfo": _gpr_training_info(result),
        **_unit_profile_dict(result.unit),
    }


def build_army_json_files(
    army_results: list[tuple[Army, list[Result | MultipleChoiceResult]]],
    output_dir: Path = Path("."),
) -> list[Path]:
    """Write one ``<slug>.json`` per army in *army_results* and return the paths."""
    output_dir.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []
    for army, results in army_results:
        output: dict[str, object] = {
            "name": army.name,
            "slug": army.slug,
            "strategyRating": army.strategyRating,
            "specialRules": [],
            "restrictions": [_restriction_to_dict(r) for r in army.restrictions],
            "units": [],
            "detachments": [],
            "upgrades": [],
        }
        for detachment in army.detachments:
            units = [
                {"unitName": u.unit.name, "count": u.count, "min": u.min, "max": u.max}
                for u in detachment.units
            ]
            output["detachments"].append(  # type: ignore[attr-defined]
                {
                    "name": detachment.name,
                    "group": detachment.group,
                    "units": units,
                    "restrictions": [],
                    "availableUpgrades": [d.name for d in detachment.availableUpgrades],
                }
            )
        for upgrade in army.upgrades:
            up: dict[str, object] = {
                "name": upgrade.name,
                "type": upgrade.type,
                "transportWarning": upgrade.transportWarning,
            }
            if isinstance(upgrade, UpgradeAdd):
                if upgrade.maxTotal > 0:
                    up["maxTotal"] = upgrade.maxTotal
                up["adds"] = [{"unitName": u.unit.name} for u in upgrade.adds]
            if isinstance(upgrade, UpgradeReplace):
                up["replaces"] = {
                    "fromUnitName": upgrade.fromUnit.name if upgrade.fromUnit else "",
                    "toUnitName": upgrade.toUnit.name if upgrade.toUnit else "",
                    "max": upgrade.max,
                }
            if isinstance(upgrade, UpgradeCharacter):
                up["characterNames"] = upgrade.character_names
            output["upgrades"].append(up)  # type: ignore[attr-defined]
        for result in results:
            output["units"].append(_result_to_dict(result))  # type: ignore[attr-defined]

        path = output_dir / f"{army.slug}.json"
        with path.open("w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
        paths.append(path)
    return paths
