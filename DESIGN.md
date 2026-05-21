# Epic Armageddon Machine Spirit — Design Brief

> **Audience:** This document is written for a designer who has no access to the
> application. It describes every screen/view, interactive element, data state,
> and validation feedback that a visual design must cover.

---

## 1. What the app is

**Epic Armageddon Machine Spirit** is a point-cost prediction tool for the
tabletop miniatures game *Epic Armageddon*. It takes an army's unit profiles
(stats, weapons, special rules) and uses a Gaussian Process Regression (GPR)
machine-learning model to output a recommended point cost per unit, together
with an uncertainty measure and a confidence quality rating.

The current application is a **command-line interface (CLI)** tool invoked as
`eaup`. A future visual design should translate these commands and outputs into
screens and interactions.

---

## 2. Supported armies

Two armies are currently supported. Each has a unique **slug** (URL/identifier)
and a display name.

| Slug                | Display Name              |
|---------------------|---------------------------|
| `legiones-astartes` | Legiones Astartes         |
| `solar-auxilia`     | Solar Auxilia             |

---

## 3. Routes / Screens

The application has three top-level functional areas, each mapping to a
potential screen or page in a visual design.

### 3.1 Predict — `/predict`

**Purpose:** Run the prediction model for one or more armies and display the
recommended point costs.

**Inputs / Controls:**
- **Army selector** — multi-select list of available armies, or a
  "Select all armies" toggle.
- **Output directory** — optional text field (defaults to `output/`).
- **Seed** — optional number field for reproducibility (defaults to `42`).
- **Verbose toggle** — checkbox / toggle switch that enables detailed logging
  output.

**Actions:**
- **Predict** button — triggers the pipeline; shows a loading/progress
  indicator while the model trains and predicts.

**Output view (results page):**  
After a successful run, two tables are shown per army:

#### 3.1.1 Predicted Cost Table

Columns: `Name` · `Predicted Cost` · `Uncertainty` · `Quality` · `Spread`

| Field          | Description |
|----------------|-------------|
| Name           | Unit display name (e.g. "Tactical Squad") |
| Predicted Cost | Rounded point cost. For units with weapon choices this is a **range**, e.g. `35 – 50`. |
| Uncertainty    | ± points (e.g. `±12.0`) — how confident the model is |
| Quality        | Categorical confidence label — see §6 |
| Spread         | Only shown for units with weapon choices. Percentage spread between cheapest and most expensive variant. A ⚠ warning icon is shown when spread > 15 %. |

Below the table, two summary statistics are shown:
- **Average Score** (0–100, higher = more confident)
- **Average Uncertainty** (points)

#### 3.1.2 Unit Stats Table

Columns: `Name` · `Type` · `Speed` · `Armour` · `CC` · `FF` · `Weapons` ·
`Range` · `Firepower` · `Notes`

This table lists every unit's raw game statistics so the viewer can cross-check
the model inputs.

---

### 3.2 Validate — `/validate`

**Purpose:** Show how accurate the model is by running leave-one-out
cross-validation on the training data.

**Inputs / Controls:**
- **Verbose toggle** — same as predict screen.
- **Run Validation** button.

**Output view:**
Two numeric results displayed after the run completes:
- **MAE** — Mean Absolute Error in points (e.g. `MAE: 8.42 pts`)
- **Avg Absolute Error** — Average absolute error in points

No tables; this is a summary view only.

---

### 3.3 Stats — `/stats`

**Purpose:** Display the raw unit-profile statistics table for one army,
without running the prediction model.

**Inputs / Controls:**
- **Army selector** — single-select dropdown of available armies.
- **Output directory** — optional text field.
- **Generate Stats** button.

**Output view:**
The same **Unit Stats Table** described in §3.1.2, but for the selected army
only.

---

## 4. Menus / Navigation

### 4.1 Primary navigation

A persistent top-level navigation bar (or sidebar) with three items:

1. **Predict** — leads to `/predict`
2. **Validate** — leads to `/validate`
3. **Stats** — leads to `/stats`

### 4.2 Army picker

Used on the Predict and Stats screens. Presents the following options:

- `Legiones Astartes`
- `Solar Auxilia`
- *(future armies would be added here)*

On the **Predict** screen the picker is a **multi-select** (or "All armies"
shortcut). On the **Stats** screen it is a **single-select** dropdown.

---

## 5. Dialogs / Feedback states

### 5.1 Loading / In-progress

Shown while the model is training and generating predictions. This can take
several seconds.

**Elements:**
- Spinner or progress bar
- Status text, e.g. "Training on 120 units…" → "Predicting Legiones
  Astartes…" → "Writing output files…"

### 5.2 Success confirmation

Shown after a successful run.

**Message pattern:**
> Output written to `output/`

Includes a link or button to view/download the generated files.

### 5.3 Error: No army selected (Predict screen)

Triggered when the user clicks **Predict** without selecting any army and
without enabling "All armies".

**Message:**
> Specify army slugs or enable "All armies".

**Presentation:** Inline form error beneath the army selector, or a toast
notification.

### 5.4 Error: Unknown army slug

Triggered if an invalid army identifier is submitted (e.g. via URL or API).

**Message:**
> Unknown army: `<slug>`. Available armies: `legiones-astartes`,
> `solar-auxilia`.

**Presentation:** Error banner at the top of the results area.

### 5.5 Error: Unknown army (Stats screen)

Same as §5.4, for the Stats screen.

**Message:**
> Unknown army `<slug>`. Available: `legiones-astartes`, `solar-auxilia`.

---

## 6. Quality / Validation states

Every predicted unit carries a **Quality** label derived from its uncertainty
score. This is the primary visual status indicator in the results table and
should use distinct colour coding.

| Quality Label | Condition | Suggested colour |
|---------------|-----------|-----------------|
| **Safe** | Score > 80 **or** uncertainty < 10 pts | Green |
| **Review** | Score > 70 **or** uncertainty < 15 pts | Amber / Yellow |
| **Experimental** | Everything else (high uncertainty) | Red |

**Score formula:** `score = round((1 − uncertainty / predicted_cost) × 100)`
(0–100; higher is better).

### 6.1 Spread warning (weapon-choice units)

Units that have mutually exclusive weapon options (e.g. "Heavy Bolters **or**
Las Cannons") generate a cost range. When the spread between cheapest and most
expensive variant exceeds **15 %**, a ⚠ warning is appended to the Spread
column. This should be visually distinct from the Quality badge.

---

## 7. Data model overview

The following concepts appear in tables and should have consistent visual
treatment.

### 7.1 Unit

| Field               | Type / Values | Notes |
|---------------------|---------------|-------|
| Name                | String        | Display name |
| Type                | Enum (see §7.2) | Short code shown in tables |
| Speed               | `Ncm` or aircraft class | e.g. `15cm`, `Fighter`, `Bomber` |
| Armour              | Integer 1–6   | Lower = better (roll ≥ N on D6) |
| CC (Close Combat)   | Integer 1–6   | Lower = better |
| FF (Firefight)      | Integer 1–6   | Lower = better |
| Strategy Rating     | Integer       | Higher = better |
| Initiative          | Integer       | Lower = better |
| Damage Capacity     | Integer ≥ 1   | War Engines only |
| Void Shields        | Integer ≥ 0   | Shown as "Void Shields (N)" |
| Transport Capacity  | Integer ≥ 0   | Optional |
| Traits              | List (see §7.4) | Comma-separated in Notes column |

### 7.2 Unit types

| Code  | Full name             |
|-------|-----------------------|
| CH    | Character             |
| INF   | Infantry              |
| LV    | Light Vehicle         |
| AV    | Armoured Vehicle      |
| AC    | Aircraft              |
| WE    | War Engine            |
| AC/WE | Aircraft War Engine   |

### 7.3 Weapons

Three base weapon categories, displayed in the stats table:

| Category       | Range display       | Firepower display |
|----------------|---------------------|--------------------|
| Ranged Weapon  | `Ncm`               | `AT4+`, `AP5+`, `AA6+`, `MW3+`, `NBP`, or combinations |
| Assault Weapon | `(base contact)`    | Any applicable traits |
| Small Arms     | `(Small Arms)`      | Any applicable traits |

**Multiplier:** A weapon may appear multiple times on a unit (e.g. `2× Heavy
Bolter`).

**Multiple Choice Weapon:** Some weapon slots offer mutually exclusive
alternatives (e.g. "Heavy Bolter **or** Las Cannon"). In the stats table these
are displayed on successive rows prefixed with `(or)`. In the prediction table
they produce a cost range with an optional ⚠ spread warning.

Weapon firepower abbreviations:

| Code | Meaning              |
|------|----------------------|
| AT   | Anti-Tank            |
| AP   | Anti-Personnel       |
| AA   | Anti-Aircraft        |
| MW   | Macro-Weapon         |
| BP   | Barrage Points       |

### 7.4 Unit traits (special rules)

These appear as comma-separated text in the Notes column of the stats table.
Example values:

> Know No Fear, Jump Packs, Scout, Infiltrator, Reinforced Armour, Skimmer,
> Teleport, Walker, Fearless, Inspiring, Leader, Commander, Supreme Commander,
> Expendable, Disrupt, First Strike, Slow Firing, Titan Killer (D3),
> Titan Killer (D6), Invulnerable Save, Mounted, Planet Fall, Tunneler,
> Indirect, Ignore Cover, Extra Attack +1/+2/+3, Single Shot, Lance,
> Macro-Weapon, Thick Rear Armour, FxF (Fixed Forward), Rear

---

## 8. Output files

After a predict run the following downloadable files are produced. A results
screen should offer links to each.

| File                       | Format   | Description |
|----------------------------|----------|-------------|
| `<army-slug>.md`           | Markdown | Human-readable prediction + stats tables |
| `<army-slug>.json`         | JSON     | Per-unit prediction data (cost, uncertainty, quality, profile, weapons) |
| `prices.json`              | JSON     | Combined prices for all predicted armies |
| `<army-slug>-stats.md`     | Markdown | Unit stats table only (from `stats` command) |

### 8.1 JSON entry structure (per unit in `prices.json`)

```json
{
  "cost": 35,
  "uncertainty": 8,
  "quality": "Safe",
  "unit_profile": {
    "type": "INF",
    "speed": "15cm",
    "armour": 4,
    "cc": 4,
    "ff": 4,
    "traits": ["Know No Fear"]
  },
  "weapons": [
    {
      "name": "Bolters",
      "type": "Small Arms",
      "range": "(15cm)",
      "traits": []
    }
  ]
}
```

For **weapon-choice units**, individual weapon options include a `cost_delta`
field showing the extra point cost relative to the cheapest option.

---

## 9. Cost rounding rules

Predicted costs are rounded to the nearest step based on magnitude. Designers
should be aware that all displayed costs follow this convention:

| Cost range  | Rounded to nearest |
|-------------|-------------------|
| < 100 pts   | 5 pts             |
| 100–199 pts | 10 pts            |
| ≥ 200 pts   | 25 pts            |

---

## 10. Summary of all user-visible states

| State                     | Location           | Trigger |
|---------------------------|--------------------|---------|
| Idle (no results yet)     | Predict / Stats    | Initial load |
| Loading / In progress     | Predict / Validate / Stats | After submit |
| Results — all Safe        | Predict results    | All quality = Safe |
| Results — mixed quality   | Predict results    | Mix of Safe / Review / Experimental |
| Spread warning ⚠          | Prediction table   | Spread > 15 % on choice unit |
| Success confirmation      | Any command        | Run completes |
| Error: no army selected   | Predict            | Submit with no army chosen |
| Error: unknown army       | Predict / Stats    | Invalid slug supplied |
| Validation result         | Validate results   | Run completes |
