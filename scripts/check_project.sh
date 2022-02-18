#!/bin/sh

# Linter checks
# stop the build if there are Python syntax errors or undefined names
flake8 src test --count --select=E9,F63,F7,F82 --show-source --statistics
# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
flake8 src test --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

# Unit test and coverage
coverage run -m pytest -v && coverage report --omit="*/test/*,*/venv/*"

# Coverage report in html
# coverage run -m pytest -v && coverage html --omit="*/test/*,*/venv/*"

# With param -s for input
# coverage run -m pytest - v -s && coverage html --omit="*/test/*,*/venv/*"