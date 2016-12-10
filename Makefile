.PHONY: run
run:
	python2.7 src/game.py

.PHONY: test
test:
	PYTHONPATH=src py.test test -s

.PHONY: install
install:
	virtualenv venv
	venv/bin/pip install -r requirements.lock
	venv/bin/pip install -r test-requirements.lock

.PHONY: freeze
freeze: requirements.lock test-requirements.lock

requirements.lock: requirements.txt
	virtualenv run_venv
	run_venv/bin/pip install -r requirements.txt
	run_venv/bin/pip freeze > requirements.lock
	rm -rf run_venv

test-requirements.lock: test-requirements.txt
	virtualenv test_venv
	test_venv/bin/pip install -r test-requirements.txt
	test_venv/bin/pip freeze > test-requirements.lock
	rm -rf test_venv
