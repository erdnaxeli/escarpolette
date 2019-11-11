POETRY = poetry
BLACK = $(POETRY) run black
FLASK = $(POETRY) run flask
MYPY = $(POETRY) run mypy
RADON = $(POETRY) run radon

export FLASK_APP = escarpolette
export FLASK_ENV = development

init:
	$(POETRY) install

db-upgrade:
	$(FLASK) db upgrade

format:
	$(BLACK) $(FLASK_APP)

complexity:
	$(RADON) cc --total-average -nB -s escarpolette

run:
	$(FLASK) run

build:
	$(MYPY) --ignore-missing-import escarpolette
