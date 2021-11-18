FORCE:

prod: tests github

github: FORCE
	- git commit -a
	git push origin master

lint: FORCE
	flake8 medical_record_management_project/


env: FORCE
	pip install -r requirements.txt

dev_env: FORCE
	pip install -r requirements-dev.txt

db: FORCE
	cd $(PROJ_DIR); python manage.py makemigrations; python manage.py migrate

dev_env: FORCE
	pip install -r requirements.txt

setup_dev: dev_env db

test: FORCE
	python medical_record_management_project/manage.py test

coverage: FORCE
	coverage run medical_record_management_project/manage.py test
	coverage report -m

