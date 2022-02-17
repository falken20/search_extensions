#!/bin/sh

coverage run -m pytest -v && coverage html --omit=*/venv/*,*/test/*

# With param -s for input
# coverage run -m pytest - v -s && coverage html --omit=*/venv/*,*/test/*