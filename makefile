FORCE:

prod: tests github

github: FORCE
	- git commit -a
	git push origin master

lint: FORCE
	flake8 medical_record_management_project/

dev_env: FORCE
	pip install -r requirements.txt

test: FORCE
	python medical_record_management_project/manage.py test

coverage: FORCE
	coverage run medical_record_management_project/manage.py test
	coverage report -m

