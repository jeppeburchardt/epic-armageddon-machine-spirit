---
description: "Use when adding or adjusting unit profiles, defining weapons, creating new army files, or extending the GPR pipeline in this EA unit pricing project. Covers Python conventions, unit/weapon construction patterns, stat semantics, and file organisation."
applyTo: "src/**/*.py"
---

# EA Unit Pricing — Project Conventions

## Python Style

- **Enforce type hints on all new and modified code**: function signatures, return types, and class attribute annotations.
- Use `list[X]` (lowercase, Python 3.9+ builtin generics), not `List[X]` from `typing`.
- Prefer `X | None` over `Optional[X]` for optional types.
- Keep imports explicit — never use `from module import *`.
- Organise imports: standard library first, then project-local modules.

### Type hint examples

```python
# Function signatures
def add_unit(self, unit: Unit) -> None: ...
def get_sorted_units(self) -> list[Unit]: ...

# Class attributes
class RangedWeapon:
    name: str
    range: int
    at: int
    ap: int
    traits: list[Traits]
```

---

## Dice Stat Semantics

All game stats that read as "roll X or more on a D6" use **lower = better**:

| Stat         | Meaning                                  | Best value |
| ------------ | ---------------------------------------- | ---------- |
| `initiative` | Order activation (lower acts first)      | `1`        |
| `armour`     | Hit threshold (lower = harder to damage) | `2`        |
| `cc`         | Close combat hit roll                    | `2`        |
| `ff`         | Firefight hit roll                       | `2`        |

`speed` is in centimetres and higher is better.  
`strategy_rating` is higher = better.  
`damage_capacity` and `void_shields` are higher = better.

---

## Unit Construction

Use **keyword arguments** for all parameters except `name` (which is positional first):

```python
legiones_astartes.add_unit(
    Unit(
        "Predator Squadron",
        strategy_rating=4,
        initiative=2,
        type=UnitType.ARMORED_VEHICLE,
        speed=30,
        armour=4,
        cc=6,
        ff=4,
        weapons=[
            BattleCannon(),
            MultipleChoiceWeapon([HeavyBolter(), LasCannon()]),
        ],
        traits=[Traits.REINFORCED_ARMOUR],
    )
)
```

### `single_unit_cost`

Always the **cost per model** (not per squad/formation):

```python
# If source lists 270pts for a 5-model squad:
single_unit_cost=270 / 5
```

Omit `single_unit_cost` on input (LI) units — it will be predicted by the model.

### Mandatory fields

`name`, `strategy_rating`, `initiative`, `type` are always required.  
All other fields default to `0` / empty — only set fields that differ from neutral defaults.

---

## Weapon Modelling

### Weapon classes at a glance

| Class                         | Use for                                                        |
| ----------------------------- | -------------------------------------------------------------- |
| `RangedWeapon`                | Any weapon with a range stat                                   |
| `AssaultWeapon`               | Base contact / melee weapons                                   |
| `SmallArms`                   | Generic short-range small arms (no meaningful firepower stats) |
| `Multiplier(n, weapon)`       | Multiple identical ranged weapons on one unit                  |
| `MultipleChoiceWeapon([...])` | Mutually exclusive weapon options in a slot                    |

### `RangedWeapon` parameters

```python
RangedWeapon(
    range,       # int, in centimetres
    at=0,        # Anti-Tank dice roll (lower = better, 0 = no AT)
    ap=0,        # Anti-Personnel dice roll
    aa=0,        # Anti-Aircraft dice roll
    bp=0,        # Barrage Points
    mw=0,        # Macro-Weapon dice roll
    traits=[],   # list[Traits]
    name="--",
)
```

### Weapon factory subclasses

Extract reusable weapons as subclasses of `RangedWeapon` and place them in `src/ea_unit_pricing/data/input/ea_hh_weapons.py`:

```python
class PlasmaCannon(RangedWeapon):
    def __init__(self, traits: list[Traits] | None = None) -> None:
        super().__init__(45, at=4, ap=4, name="Plasma Cannon", traits=traits or [])
```

Only define inline `RangedWeapon(...)` for weapons that are unique to a single unit.

### `Multiplier` — repeated identical weapons

```python
# Four lascannons
weapons=[Multiplier(4, LasCannon())]
```

### `MultipleChoiceWeapon` — optional / alternative weapon slots

```python
weapons=[
    HeavyBolter(),
    MultipleChoiceWeapon([LasCannon(), TwinLinkedLasCannon()]),
]
```

The unit is automatically expanded into one variant per combination via `Unit.get_all_configurations()`. Do **not** duplicate the `Unit` entry manually instead.

---

## Traits

Always use the `Traits` enum — never raw strings:

```python
traits=[Traits.KNOW_NO_FEAR, Traits.JUMP_PACKS]
```

### Adding a new trait

1. Add an entry to `Traits(Enum)` in `src/ea_unit_pricing/domain/enums.py` with the next sequential integer value.
2. Add a human-readable mapping in `trait_to_string()` in the same file.
3. Determine which GPR segment it belongs to (see table below) and add a case to the relevant `src/ea_unit_pricing/gpr/mapping/segments/*.py` file.

| Trait category                                        | Segment file                     |
| ----------------------------------------------------- | -------------------------------- |
| Weapon special rules (Indirect, Lance, MW…)           | `trait_groups.py`                |
| Mobility (Jump Packs, Scout, Skimmer, Tunneler…)      | `trait_groups.py`                |
| Survivability (Reinforced Armour, Invulnerable Save…) | `trait_groups.py`                |
| Leadership (Know No Fear, Fearless, Inspiring…)       | `trait_groups.py`                |
| Walker                                                | `trait_groups.py`                |
| Titan Killer multiplier                               | `extra_damage.py`                |
| Assault extra attacks                                 | `extra_damage.py` / `assault.py` |

---

## Army Construction

Always use `army.add_unit(unit)` — never append directly to `army.units`:

```python
solar_auxilia = Army("Solar Auxilia")
solar_auxilia.add_unit(Unit(...))
```

## Development Setup

Install the package in editable mode (requires Python 3.9+):

```bash
pip install -e ".[dev]"
```

Run the prediction pipeline:

```bash
eaup predict --all-armies --output-dir output
```

Run tests:

```bash
pytest tests/
```

---

## File Organisation

| File location                                       | Contents                                                                                         |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `src/ea_unit_pricing/domain/enums.py`               | `UnitType`, `AircraftSpeed`, `Traits`, `Quality`, string converters                              |
| `src/ea_unit_pricing/domain/weapons.py`             | `RangedWeapon`, `AssaultWeapon`, `SmallArms`, `Multiplier`, `MultipleChoiceWeapon` (dataclasses) |
| `src/ea_unit_pricing/domain/unit.py`                | `Unit` dataclass, `expand_choices()`                                                             |
| `src/ea_unit_pricing/domain/army.py`                | `Army`, `Detachment`, upgrade classes                                                            |
| `src/ea_unit_pricing/domain/result.py`              | `Result`, `MultipleChoiceResult`, `TrainingSetValidationResult`                                  |
| `src/ea_unit_pricing/data/input/ea_hh_legion.py`    | Legiones Astartes unit profiles (prediction input)                                               |
| `src/ea_unit_pricing/data/input/ea_hh_solar_aux.py` | Solar Auxilia unit profiles (prediction input)                                                   |
| `src/ea_unit_pricing/data/input/ea_hh_weapons.py`   | Shared weapon factory classes for LI armies                                                      |
| `src/ea_unit_pricing/data/training/ea_40k_*.py`     | Epic Armageddon 40K training data (known costs)                                                  |
| `src/ea_unit_pricing/gpr/mapping/segments/`         | One file per feature-vector segment (layout frozen)                                              |
| `src/ea_unit_pricing/pipeline/prediction.py`        | `run_pipeline()`, `predict_army()`, `predict_with_choices()`                                     |
| `src/ea_unit_pricing/serialization/`                | Output formatters (markdown, JSON)                                                               |
| `src/ea_unit_pricing/cli.py`                        | `eaup` CLI entry point                                                                           |
| `tests/golden/`                                     | Committed reference outputs (regression oracle)                                                  |

### ⚠ Frozen vector layout

**Never change the order of segments in `universal_unit.py`.**  
The GPR model's feature vector has 30 elements in a fixed order (stats → unit_type → range_bands → fire_power → extra_damage → trait_groups → assault). Changing segment order or dimensions requires retraining and regenerating golden outputs.

### Naming conventions

- Army data files: `ea_hh_<army>.py` (input) or `ea_40k_<army>.py` (training)
- Weapon factory classes: PascalCase matching the in-game name (`TwinLinkedLasCannon`)
- Trait enum members: `SCREAMING_SNAKE_CASE`
- Segment functions: `snake_case`, return `list[float]`

---

## GPR Pipeline Rules

- **Never change the order or count of segments** returned by `universal_unit()` without retraining the model — the vector layout must stay stable.
- Always call `unit.get_all_configurations()` before passing a unit into the trainer or predictor; never call `predict(unit)` directly on a unit with `MultipleChoiceWeapon` slots.
- When adding a new feature dimension, update the corresponding segment file and document the index offset.
