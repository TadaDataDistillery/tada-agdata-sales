default: all

test:
	coverage run -m unittest discover tests && coverage report

test-unit:
	coverage run -m unittest discover tests/unit && coverage report

check:
	pylint -E lambdas data_processing

style:
	pylint lambdas data_processing --fail-under 9

type:
	mypy lambdas data_processing

format:
	black lambdas data_processing tests && isort lambdas data_processing tests --profile black

all: format check style type test

build:
	docker build -t data_processing .
