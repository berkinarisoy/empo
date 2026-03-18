.PHONY: setup test

setup:
	python -m venv .venv
	.venv/bin/pip install --upgrade pip setuptools wheel
	.venv/bin/pip install -r requirements.txt

test:
	.venv/bin/pytest tests/