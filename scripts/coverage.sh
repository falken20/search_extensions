#!/bin/sh

coverage run --source . -m pytest && coverage report --omit=tests/*.py && coverage html -o coverage-reports/coverage.html