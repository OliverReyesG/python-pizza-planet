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


.PHONY: init-db
init-db: venv
	python manage.py db init
	python manage.py db migrate
	python manage.py db upgrade


.PHONY: populate-db
populate-db: venv
	python populate_db.py


setup: venv
	pip install -r requirements.txt


test: venv
	python manage.py test


run: venv
	python manage.py run