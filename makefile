FORCE:

prod: tests github

github: FORCE
	- git commit -a
	git push origin master

unit: FORCE
	echo "Tests go here!"

lint: FORCE
	flake8 medical_record_management/*.py

dev_env: FORCE
	pip install -r $/../requirements.txt
