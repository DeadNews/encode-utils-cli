.PHONY: all clean test checks

install-all: install pc-install

install:
	poetry install --sync

pc-install:
	pre-commit install

update-latest:
	poetry up --latest

checks: pc-run install lint test

pc-run:
	pre-commit run -a

lint:
	poetry run poe lint

test:
	poetry run poe test

docs-serve:
	poetry run mkdocs serve
