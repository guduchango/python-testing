# Python Testing with Unittest

This repository is designed to illustrate how to perform unit testing in Python using the `unittest` tool. The project is structured in evolutionary steps, represented in different Git branches: `step__1`, `step__2`, ..., up to `step__14`. Each branch shows a step toward the full implementation of tests, from the initial setup to the integration of tests and the generation of coverage reports.

## Project Structure

- **Branches**: Each branch contains a specific phase of the unit testing development. You can follow the progress of the implementation step by step starting from `step__1` to `step__14`.
- **Unit Tests**: The tests are organized within the `src_tests` folder.
- **Test Coverage**: The **Coverage** tool is used to measure the test coverage and generate detailed reports.

## Commands Used

Here are the main commands used in this project to run the tests and generate coverage reports:

1. **Run unit tests**:
   ```bash
   python3.12 -m unittest discover -v -s src_tests
   ```

2. **Run tests from a specific file:**:
   ```bash
   PYTHONPATH=. python3.12 src_tests/suites.py
   ```

3. **Generate coverage report:**:
   ```bash
   coverage run --source src -m unittest
   coverage report  
   coverage html
   ```

4. **Run unit tests**:
   ```bash
   coverage run --source ./src_tests -m unittest
   ```
## Purpose

The purpose of this project is to teach and demonstrate how to structure a testing project in Python, how to use `unittest` to test functions, and how to achieve full test coverage using the `coverage` tool. By following the different branches, developers can see how the project is structured and progresses, continually improving the tests and ensuring their quality.

## Conclusion

This project is a practical example of how to structure a testing project in Python, and how to use `unittest` to test functions.