# CSV Normalizer for Truss
This is my solution to the project described at: https://github.com/trussworks/truss-interview/blob/master/CSV_README.md

# Installation
I used pyenv to manage my python version and Pipenv to manage dependencies.
```shell script
$ pipenv install
```

# Running
```shell script
$ pipenv shell
$ ./normalizer.py < sample.csv > output.csv
```

# Tests
I'm use pytest.
Tests are in the tests/ directory.
```shell script
$ pipenv install --dev
$ pipenv run pytest tests
```

# Assumptions
