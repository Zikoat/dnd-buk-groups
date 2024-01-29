.PHONY: test lint type-check format all

test:
	pytest

lint:
	pylint src

type-check:
	mypy src

format:
	black src

run-script:
	./src/main.py

all: format lint type-check test run-script
