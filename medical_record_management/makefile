FORCE:

prod: tests github

github: FORCE
    - git add .
	- git commit -m "Auto-push from make command"
	git push origin master

unit: FORCE
	echo "Tests go here!"

lint: FORCE
	flake8 medical_record_management/*.py

dev_env: FORCE
	pip install -r $/../requirements.txt
