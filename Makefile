.ONESHELL:


.DEFAULT_GOAL := setup

PYTHON = ./venv/bin/python
PIP = ./venv/bin/pip

DOCKER_USER= oliverreyes
APP_NAME = pizza-planet-backend
TAG = latest


venv/bin/activate: requirements.txt
	python -m venv venv
	chmod +x venv/bin/activate


.PHONY: venv
venv: venv/bin/activate
	. venv/bin/activate


.PHONY: init-db
init-db: venv
	$(PYTHON) manage.py db init
	$(PYTHON) manage.py db migrate
	$(PYTHON) manage.py db upgrade


.PHONY: populate-db
populate-db: venv
	$(PYTHON) populate_db.py


setup: venv
	$(PIP) install -r requirements.txt


test: venv
	$(PYTHON) manage.py test


run: venv
	$(PYTHON) manage.py run --host=0.0.0.0


submodule: ui
	git submodule update --init


.PHONY:
build:
	docker build -t $(DOCKER_USER)/$(APP_NAME):$(TAG) .