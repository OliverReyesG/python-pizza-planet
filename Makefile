.ONESHELL:


.DEFAULT_GOAL := setup
.PHONY: venv


PYTHON = ./venv/bin/python
PIP = ./venv/bin/pip


venv/bin/activate: requirements.txt
	python -m venv venv
	chmod +x venv/bin/activate
	. venv/bin/activate


venv: venv/bin/activate
	. venv/bin/activate


setup: venv
	pip install -r requirements.txt

test: venv
	python manage.py test

run: venv
	python manage.py run