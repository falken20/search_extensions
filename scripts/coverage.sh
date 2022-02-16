#!/bin/sh

coverage run -m pytest -v && coverage html

# With param -s for input
# coverage run -m pytest - v -s && coverage html