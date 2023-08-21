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
	. venv/bin/activate


.PHONY: venv
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
	python manage.py run --host=0.0.0.0


.PHONY:
build:
	docker build -t $(DOCKER_USER)/$(APP_NAME):$(TAG) .