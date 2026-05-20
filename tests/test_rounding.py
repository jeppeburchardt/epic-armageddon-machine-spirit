from __future__ import annotations

import unittest

from models.result import MultipleChoiceResult, Result
from models.units import MultipleChoiceWeapon, RangedWeapon, Unit, UnitType
from out.army_json import _weapons_for_choice_result
from out.army_list_json import result_to_army_json
from out.rounding import round_points


def make_unit(name: str, weapons: list | None = None) -> Unit:
    return Unit(
        name,
        strategy_rating=1,
        initiative=1,
        type=UnitType.INFANTRY,
        weapons=weapons or [],
    )


class RoundingPolicyTests(unittest.TestCase):
    def test_round_points_uses_tiered_steps(self) -> None:
        self.assertEqual(round_points(99), 100)
        self.assertEqual(round_points(100), 100)
        self.assertEqual(round_points(149), 150)
        self.assertEqual(round_points(199), 200)
        self.assertEqual(round_points(200), 200)
        self.assertEqual(round_points(213), 225)

    def test_choice_surcharges_are_derived_from_rounded_totals(self) -> None:
        base_weapon = RangedWeapon(15, name="Base Gun")
        option_a = RangedWeapon(30, name="Option A")
        option_b = RangedWeapon(45, name="Option B")
        unit = make_unit(
            "Chooser",
            weapons=[
                base_weapon,
                MultipleChoiceWeapon([option_a, option_b], name="Turret"),
            ],
        )

        results = MultipleChoiceResult(
            unit,
            [
                Result(make_unit("Chooser [A]"), predicted_cost=98, uncertainty=4),
                Result(make_unit("Chooser [B]"), predicted_cost=102, uncertainty=4),
            ],
        )

        weapon_data = _weapons_for_choice_result(results)
        choices = weapon_data[1]["options"]

        self.assertEqual(choices[0]["cost_delta"], 0)
        self.assertEqual(choices[1]["cost_delta"], 0)

        army_json = result_to_army_json(results)
        self.assertEqual(army_json["cost"], 100)
        self.assertEqual(army_json["weaponSlots"][1]["choices"][0]["additionalCost"], 0)
        self.assertEqual(army_json["weaponSlots"][1]["choices"][1]["additionalCost"], 0)


if __name__ == "__main__":
    unittest.main()
