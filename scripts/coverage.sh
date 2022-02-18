#!/bin/sh

coverage run -m pytest -v && coverage report --omit="*/test/*,*/venv/*"

# Coverage report in html
# coverage run -m pytest -v && coverage html --omit="*/test/*,*/venv/*"

# With param -s for input
# coverage run -m pytest - v -s && coverage html --omit="*/test/*,*/venv/*"