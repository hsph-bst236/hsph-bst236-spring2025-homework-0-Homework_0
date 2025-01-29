# Homework 0: Github Classroom and Python Warmup

The due date is Feb 6  at midnight. If you are using the late days, please note in the head of README.md that “I used XX late days this time, and I have XX days remaining”.

## Introduction
This repository contains a Python implementation of the Fibonacci sequence calculator with intentionally introduced formatting issues and code style problems. The main purpose of this homework is to help you:

- Get familiar with Github Classroom and our homework submission process.
- Writing and fixing code with formatting and linting issues. 
- Using `pytest` for testing.
- Get experience with GitHub Actions for automated workflow.

## Installation

1. From the terminal, clone the repository:
```bash
git clone <your-repo-url>
cd <repo-name>
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. For example, the first 10 fibonacci numbers are:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The function `fibonacci(n)` in this repository calculates the nth number in the Fibonacci sequence, where:
- fibonacci(0) = 0
- fibonacci(1) = 1 
- fibonacci(n) = fibonacci(n-1) + fibonacci(n-2) for n > 1

You can get the nth number in the Fibonacci sequence by the terminal command `python fibonacci.py <n>`. For example, running the following command to get the 4th number in the Fibonacci sequence:
```bash
python3 fibonacci.py 4
4
```

The answer is above is incorrect and you must edit the code to fix it. We provide the text above as a sample for the Usage section of the README.md file in your homework submission.

The repository contains `fibonacci.py` with all kinds of issues. Your task is to:


1. Run the tests to verify current functionality
```bash
pytest -v
```

2. Check current formatting and linting issues:
```bash
black --diff .
pylint fibonacci.py
```
3. Revise the `fibonacci.py` file to fix all formatting issues and potential bugs. In particular, all `pytest` tests should pass and `pylint fibonacci.py` should give a score of 10/10. 

4. Write a README.md file following the format of this file and instruction of the [Homework Submission Guidelines](https://junwei-lu.github.io/bst236/chapter_syllabus/syllabus/#homework-submission-guidelines)

5. Push your changes to the homework repository and check if it passes the GitHub Actions workflow.

**Hint:** You can raise value error by the following code:
```python
raise ValueError("Error message")
```

## Report

Here is the sample of the report. You should report how you solve the problems and other information requested by the homework.

We ran the `pytest` command and got the following results:
```
collected 3 items

test_fibonacci.py::test_fibonacci_base_cases FAILED
test_fibonacci.py::test_fibonacci_positive_numbers PASSED
test_fibonacci.py::test_fibonacci_negative_input FAILED
```
The failures are:
- Base cases test failed: fibonacci(0) returns 1 instead of expected 0
- Negative input test failed: Function doesn't raise ValueError for negative inputs
  
We fixed these issues by:
1. Adding a base case check for n=0 to return 0 directly
2. Adding input validation to raise ValueError for negative inputs
3. Fixed the initialization of variables a and b to handle base cases correctly

After these fixes, all tests passed successfully.

## Contributions

Junwei Lu: Homework design and writing

Phillip Nicol: Testing and revision
