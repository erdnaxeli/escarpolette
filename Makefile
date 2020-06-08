POETRY = poetry
BLACK = $(POETRY) run black
MYPY = $(POETRY) run mypy
PYTEST = $(POETRY) run pytest
RADON = $(POETRY) run radon

APP_HOST ?= 127.0.0.1
APP_PORT ?= 5000

export FLASK_APP = escarpolette
export FLASK_ENV ?= development

init:
	$(POETRY) install

db-upgrade:
	$(FLASK) db upgrade

format:
	$(BLACK) $(FLASK_APP) tests

format-ci:
	$(BLACK) --check $(FLASK_APP) tests

complexity:
	$(RADON) cc --total-average -nB -s escarpolette

run:
	$(POETRY) run python -m escarpolette --dev

build:
	$(MYPY) escarpolette

tests:
	$(PYTEST) tests/

.PHONY: init db-upgrade fromat complexity run build tests
