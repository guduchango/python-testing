# python-testing
python testing example

# Doc Testing Python
https://docs.python.org/3/library/unittest.html

# Run test
python3.12 -m unittest discover -v -s tests

# Run suites
PYTHONPATH=. python3.12 tests/suites.py

# run tests
```
python3.12 -m unittest discover -v -s tests
```

# Coverage
```
coverage run --source src -m unitest
coverage report
coverage html
```


# Bugs
```bash
# this comand not run if not change folder tests to other unique name
coverage run --source ./src_tests -m unittest
