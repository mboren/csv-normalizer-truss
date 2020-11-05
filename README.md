# CSV Normalizer
This is my solution to the project described at: https://github.com/trussworks/truss-interview/blob/master/CSV_README.md

# Dependencies
- Python 3.9
- [pytz](https://pypi.org/project/pytz/) 2020.4

# Installation
I used [pyenv](https://github.com/pyenv/pyenv) to manage my Python version
and [Pipenv](https://pipenv.pypa.io/en/latest/) to manage dependencies.

There're a lot of ways to deal with python versions and dependencies though,
so if you don't want to install pyenv, you can probably just use any version
of python 3 and `pip install pytz`

I haven't tested with any versions other than 3.9, but I'm not doing anything
terribly exciting, so I don't think there'll be compatibility issues.

## Install Python 3.9
You should do this however you like. If you have python installed
with homebrew, there's a good chance you already have 3.9, and can skip this step.
```shell script
$ pyenv install 3.9.0
```

## Install dependencies
```shell script
$ pipenv sync
```

# Running
```shell script
$ pipenv shell
$ ./normalizer.py < sample.csv > output.csv
```

# Tests
I'm using pytest.
Tests are in the tests/ directory.

## Install test dependencies
```shell script
$ pipenv sync --dev
```

## run tests
```shell script
$ pipenv run pytest tests
```

# Assumptions
- I assumed that all characters in names (eg numbers) were fine, and did no validation on this column.
- Since the instructions only said to drop rows if a column was unparseable due to invalid UTF-8 characters,
  I'm not dropping rows with zip codes that are longer than 5 digits.
- I assumed Python's [str.upper](https://docs.python.org/3/library/stdtypes.html#str.upper) function is sufficient for
  capitalizing non-english characters.

# More stuff I'd do
- Make output line ending match input line endings. 
