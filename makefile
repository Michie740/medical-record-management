PROJ_DIR = medical_record_management_project

FORCE:

prod: tests github

github: FORCE
	- git commit -a
	git push origin master

lint: FORCE
	flake8 $(PROJ_DIR)/

env: FORCE
	pip install -r requirements.txt

dev_env: FORCE
	pip install -r requirements-dev.txt

db: FORCE
	python $(PROJ_DIR)/manage.py makemigrations
	python $(PROJ_DIR)/manage.py migrate

setup_dev: dev_env db

test: FORCE
	python $(PROJ_DIR)/manage.py test

coverage: FORCE
	coverage run medical_record_management_project/manage.py test
	coverage report -m

run: FORCE
	python $(PROJ_DIR)/manage.py runserver
