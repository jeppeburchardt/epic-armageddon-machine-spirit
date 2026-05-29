from __future__ import annotations

import unittest

from ea_unit_pricing.domain import MultipleChoiceWeapon, RangedWeapon, Unit, UnitType
from ea_unit_pricing.domain.result import MultipleChoiceResult, Result
from ea_unit_pricing.serialization.army_json import _weapons_for_choice_result
from ea_unit_pricing.serialization.army_list_json import _result_to_dict
from ea_unit_pricing.serialization.rounding import round_points


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

        army_json = _result_to_dict(results)
        self.assertEqual(army_json["cost"], 100)
        self.assertEqual(army_json["weaponSlots"][1]["choices"][0]["additionalCost"], 0)
        self.assertEqual(army_json["weaponSlots"][1]["choices"][1]["additionalCost"], 0)

    def test_result_to_dict_includes_gpr_training_info(self) -> None:
        result = Result(
            make_unit("Scout"),
            predicted_cost=101,
            uncertainty=9,
            nearest_neighbours=[("Tac", 100.0, 0.2), ("Assault", 105.0, 0.4)],
            training_price_values=[100.0, 105.0, 110.0],
            model_kernel="RBF(...)",
            training_set_size=3,
        )

        payload = _result_to_dict(result)
        gpr_info = payload["gprTrainingInfo"]
        self.assertEqual(gpr_info["predictedMean"], 101)
        self.assertEqual(gpr_info["trainingSetSize"], 3)
        self.assertEqual(len(gpr_info["topNearestNeighbours"]), 2)
        self.assertEqual(gpr_info["contributingPriceValues"], [100.0, 105.0, 110.0])

    def test_choice_result_to_dict_includes_gpr_training_info(self) -> None:
        option_a = RangedWeapon(30, name="Option A")
        option_b = RangedWeapon(45, name="Option B")
        unit = make_unit(
            "Chooser",
            weapons=[MultipleChoiceWeapon([option_a, option_b], name="Turret")],
        )
        results = MultipleChoiceResult(
            unit,
            [
                Result(
                    make_unit("Chooser [A]"),
                    predicted_cost=108,
                    uncertainty=4,
                    nearest_neighbours=[("Tac", 100.0, 0.3)],
                    training_price_values=[100.0, 110.0],
                    model_kernel="RBF(...)",
                    training_set_size=2,
                ),
                Result(make_unit("Chooser [B]"), predicted_cost=102, uncertainty=4),
            ],
        )

        payload = _result_to_dict(results)
        gpr_info = payload["gprTrainingInfo"]
        self.assertEqual(gpr_info["predictedMean"], 108)
        self.assertEqual(gpr_info["trainingSetSize"], 2)
        self.assertEqual(gpr_info["topNearestNeighbours"][0]["name"], "Tac")


if __name__ == "__main__":
    unittest.main()
