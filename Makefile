SHELL := /bin/bash
MANAGE := ./manage.py

TEST_SETTINGS := test

.PHONY: all help deps static migrate restart update deploy

all: help

help:
	@echo "Usage:"
	@echo "  make deploy - pull and deploy the update"
	@echo "  make test - run automated tests"

deps:
	pipenv install

migrate:
	$(MANAGE) makemigrations
	$(MANAGE) migrate

test:
	$(MANAGE) test $(TEST_SETTINGS)
