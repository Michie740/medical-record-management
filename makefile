FORCE:

prod: tests github

github: FORCE
	- git commit -a
	git push origin master

tests: lint unit

unit: FORCE
	python3 -m unittest source.db

lint: FORCE
	flake8 *.py

dev_env: FORCE
	pip install -r requirements.txt

docs: FORCE
	cd source; make docs
