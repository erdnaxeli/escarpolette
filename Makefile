POETRY = poetry
BLACK = $(POETRY) run black
FLASK = $(POETRY) run flask
MYPY = $(POETRY) run mypy

export FLASK_APP = escarpolette
export FLASK_ENV = development

all:
	$(FLASK) run

lint:
	$(BLACK) $(FLASK_APP)

compile:
	$(MYPY) --ignore-missing-import escarpolette
