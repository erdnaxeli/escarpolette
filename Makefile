POETRY = poetry
BLACK = $(POETRY) run black

all:
	$(POETRY) run ./main.py	

lint:
	$(BLACK) .
