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


def _firepower_str(weapon: RangedWeapon) -> str:
    fp = []
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


def weapon_to_dict_army(weapon) -> dict:
    if isinstance(weapon, Multiplier):
        d = weapon_to_dict_army(weapon.weapon)
        d["count"] = weapon.times
        return d
    if isinstance(weapon, RangedWeapon):
        d = {
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
            "options": [weapon_to_dict_army(o) for o in weapon.options],
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


def dice_stat(v: int):
    if not v:
        return "-"
    return "{0}+".format(v)


def unit_profile_army_dict(unit) -> dict:
    profile = {
        "type": unit_type_to_string(unit.type),
        "speed": unit.unit_speed_to_string(),
        "armour": dice_stat(unit.armour),
        "cc": dice_stat(unit.cc),
        "ff": dice_stat(unit.ff),
        "traits": [trait_to_string(t) for t in unit.traits],
    }
    if unit.damage_capacity > 1:
        profile["damageCapacity"] = unit.damage_capacity
    if unit.void_shields > 0:
        profile["voidShields"] = unit.void_shields
    if unit.transport_capacity > 0:
        profile["transportation"] = {
            "capacity": unit.transport_capacity,
            "capabilities": unit.transport_capabilities,
        }
    if unit.transport_cost > 0:
        profile["transportation"] = {
            "cost": unit.transport_cost,
            "type": unit.transport_type,
        }
    return profile


def weapon_slots_army(result: MultipleChoiceResult) -> list:
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

    weaponSlots = []

    for i, w in enumerate(original_unit.weapons):
        if not isinstance(w, MultipleChoiceWeapon):
            weaponSlots.append({"kind": "fixed", **weapon_to_dict_army(w)})
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
                    delta = int(round(avg_cost - min_cost))
                else:
                    delta = 0
                opt_dict = weapon_to_dict_army(option)
                opt_dict["additionalCost"] = delta
                choice_list.append(opt_dict)
            weaponSlots.append(
                {"kind": "choice", "name": w.name, "choices": choice_list}
            )
    return weaponSlots


def result_to_army_json(result: Result):
    if isinstance(result, MultipleChoiceResult):
        min_result = min(result.all_results, key=lambda r: r.predicted_cost)
        entry = {
            "name": result.unit.name,
            "cost": int(round(min_result.predicted_cost)),
            # "uncertainty": int(round(min_result.uncertainty)),
            # "quality": quality_to_str(min_result.quality),
            "weaponSlots": weapon_slots_army(result),
            **unit_profile_army_dict(result.original_unit),
        }
    else:
        entry = {
            "name": result.unit.name,
            "cost": int(round(result.predicted_cost)),
            "uncertainty": int(round(result.uncertainty)),
            "quality": quality_to_str(result.quality),
            "weaponSlots": [
                {"kind": "fixed", **weapon_to_dict_army(w)} for w in result.unit.weapons
            ],
            **unit_profile_army_dict(result.unit),
        }
    return entry


def build_army_json_files(army_results: list[tuple[Army, list[Result]]]):
    for army, results in army_results:
        output = {
            "name": army.name,
            "slug": army.slug,
            "strategyRating": army.strategyRating,
            "specialRules": [],
            "restrictions": [],
            "units": [],
            "detachments": [],
            "upgrades": [],
        }
        for detachment in army.detachments:
            units = list(
                map(
                    lambda u: {
                        "unitName": u.unit.name,
                        "count": u.count,
                        "min": u.min,
                        "max": u.max,
                    },
                    detachment.units,
                )
            )
            output["detachments"].append(
                {
                    "name": detachment.name,
                    "group": detachment.group,
                    "units": units,
                    "restrictions": [],
                    "availableUpgrades": list(
                        map(lambda d: d.name, detachment.availableUpgrades)
                    ),
                }
            )
        for upgrade in army.upgrades:
            up = {
                "name": upgrade.name,
                "type": upgrade.type,
                "transportWarning": upgrade.transportWarning,
            }
            if upgrade.type == "add":
                if upgrade.maxTotal > 0:
                    up["maxTotal"] = upgrade.maxTotal
                up["adds"] = list(
                    map(
                        lambda u: {"unitName": u.unit.name},
                        upgrade.adds,
                    )
                )
            output["upgrades"].append(up)
        for result in results:
            output["units"].append(result_to_army_json(result))
        with open("{0}.json".format(army.slug), "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
