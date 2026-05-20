# The Epic Armageddon Machine Spirit

New unit points prediction for Epic Armageddon using machine learning

## What

The goal is to train a model on the existing units for [Epic Armagaddon](https://net-armageddon.org) found in the [Tournament Pack](https://tp.net-armageddon.org/) and use that model to predict the point cost of new units, with a good starting point, in order to skip time comsuming play testing.

## How

By converting unit profiles to vectors and feeding them to a Gaussian Process Regression (GPR) model, it is able to predict a point value and also an uncertainty measure of a new unit. GPR is preferred for at task like this, because it can produce pretty accurate prediction based on a small set of data points (hundreds), compared to neural nets that usually requires large data sets (thousands).

## Why

I want to adopt the new Legion Imperialis releases from Games Workshop into the Epic Armageddon ruleset (also by Games Workshop).

## Current state

By training on a small portion of Epic Armageddon 40K units, it can predict the point cost of new made up units, for instance the Legions Imperialis range.

Currently only army lists for Solar Auxilia and Legiones Astartes exist.

[Legiones Astartes](output/legiones-astartes.md)

[Solar Auxilia](output/solar-auxilia.md)

**Predicted Cost**
This is the current model's prediction

**Uncertainty**
How many points, + or - from the predicted cost the algorithm is uncertain

**Quality**

- Safe: Low uncertainty.
- Review: Uncertainty is not low or the uncertainty compared to the predicted cost is high.
- Experimental: High uncertainty.

## Installation

Requires Python 3.9 or later.

```bash
git clone https://github.com/your-org/ea-unit-pricing.git
cd ea-unit-pricing
pip install -e ".[dev]"
```

This installs the `eaup` command globally in your active environment.

## Usage

### Predict point costs

Generate markdown and JSON output for all armies:

```bash
eaup predict --all-armies
```

Predict a single army:

```bash
eaup predict --armies legiones-astartes
eaup predict --armies solar-auxilia
```

### Validate the training set

Run leave-one-out cross-validation on the training data and print mean absolute error:

```bash
eaup validate
```

### Unit stats table

Write a markdown stats table for an army to the output directory:

```bash
eaup stats legiones-astartes
eaup stats solar-auxilia --output-dir my-results
```

### Available army slugs

| Slug                | Army                              |
| ------------------- | --------------------------------- |
| `legiones-astartes` | Legiones Astartes (Space Marines) |
| `solar-auxilia`     | Solar Auxilia                     |

### Output files

By default, output is written to `./output/`. Each run produces:

| File          | Description                              |
| ------------- | ---------------------------------------- |
| `<army>.md`   | Human-readable points table              |
| `<army>.json` | Machine-readable results per unit        |
| `prices.json` | Combined prices for all predicted armies |

The output directory can also be set via the `EAUP_OUTPUT_DIR` environment variable:

```bash
EAUP_OUTPUT_DIR=my-results eaup predict --all
```

## Development

```bash
make install   # pip install -e ".[dev]"
make lint      # ruff check
make fmt       # ruff format
make type      # mypy --strict
make test      # pytest tests/
make cov       # pytest with coverage report
```
