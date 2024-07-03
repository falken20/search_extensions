
<div align="center">
<img src="search_extensions.png" alt="drawing" width="600"/>
<a href="https://richionline-portfolio.nw.r.appspot.com"><img src="https://richionline-portfolio.nw.r.appspot.com/static/assets/falken_logo.ico" width=40 alt="Personal Portfolio web"></a>


![Version](https://img.shields.io/badge/version-1.0.1-blue) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/rich/10.11.0)](https://www.python.org) 
![GitHub Top languaje](https://img.shields.io/github/languages/top/falken20/search_extensions) ![GitHub language count](https://img.shields.io/github/languages/count/falken20/search_extensions) ![Test coverage](https://img.shields.io/badge/test%20coverage-93%25-green)
[![Richi web](https://img.shields.io/badge/web-richionline-blue)](https://richionline-portfolio.nw.r.appspot.com) 
[![Twitter](https://img.shields.io/twitter/follow/richionline?style=social)](https://twitter.com/richionline)
</div>


# search_extensions
Script to find files in a directory tree and it has to fulfill that it has a determinate extension. The extension set is in a config file. You can configure two environment variables with the path (**PATH_DIR**) and extensions (**EXTENSIONS**) to search. If the variables doesn't exist, the script ask the user for the values.

---
##### Setup

```bash
pip install -r requirements.txt
```

##### Running the app

```bash
python ./src/search_extensions.py
```

##### Setup tests

```bash
pip install -r requirements-tests.txt
```

##### Running the tests with pytest and coverage

```bash
./scripts/coverage.sh
```
or
```bash
coverage run -m pytest -v && coverage html --omit=*/venv/*,*/test/*
```

##### Environment vars
```bash
ID_LOG=ROD->
LOG_LEVEL=INFO
# Application vars
PATH_DIR=/.../...
EXTENSIONS=mp3,jpg,png,wav,txt
```

##### Versions
- 1.0.1 Show path file in results
- 1.0.0 Basic Version