.PHONY: install lint fmt type test run clean

install:
	pip install -e ".[dev]"

lint:
	ruff check src tests

fmt:
	ruff format src tests

type:
	mypy --strict src/ea_unit_pricing

test:
	pytest --tb=short

cov:
	pytest --cov=ea_unit_pricing --cov-report=term-missing --cov-fail-under=70

run:
	eaup predict --all

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -name "*.pyc" -delete
	rm -rf .mypy_cache .ruff_cache htmlcov .coverage coverage.xml output/
