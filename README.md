IDS 706 – Assignment 1 (TA Demo Repo)

This repository is my TA demo for Assignment 1 in Data Engineering Systems (IDS 706). 
It shows how to build a minimal Python project with a script, tests, automation, and GitHub integration.

--------------------------------------------------------------------------------
Project structure
--------------------------------------------------------------------------------
ids706-assignment1_TA/
├── hello.py              # Main Python script (functions + demo run)
├── test_hello.py         # Pytest unit tests
├── requirements.txt      # Dependencies: pytest, flake8, black
├── Makefile              # Automation commands: install, test, lint, format, clean, all
├── README.md             # Documentation (Markdown file)
├── README.txt            # This text file (TA demo instructions)
└── .github/workflows/ci.yml   # (Optional) GitHub Actions workflow for CI

--------------------------------------------------------------------------------
File explanations
--------------------------------------------------------------------------------
hello.py
    - say_hello(name): returns a personalized greeting with my name as TA.
    - add(a, b): returns the sum of two numbers.
    - Can be run directly with 'python hello.py' to show example output.

test_hello.py
    - Unit tests for say_hello() and add() using pytest.

requirements.txt
    - Lists dependencies: pytest, flake8, black.
    - Install with 'pip install -r requirements.txt'.

Makefile
    - install: install dependencies
    - format: run black
    - lint: run flake8 + black --check
    - test: run pytest
    - clean: remove caches
    - all: run install + lint + test


--------------------------------------------------------------------------------
Steps I actually did (no virtual environment)
--------------------------------------------------------------------------------
1. Installed dependencies
       pip install -r requirements.txt

2. Ran formatting and linting
       make format
       make lint

3. Ran tests
       make test

4. Ran everything in one shot
       make all

5. Executed the script
       python hello.py

   Example output:
       Hello, students! This is Eric Ortega, your TA for Data Engineering Systems (IDS 706).
       2 + 3 = 5

6. Committed and pushed to GitHub
       git add .
       git commit -m "Initial commit for Assignment 1 TA demo"
       git push

--------------------------------------------------------------------------------
Notes for students
--------------------------------------------------------------------------------
- Run everything directly from the terminal (no IDE required).
- Warnings during pytest (DeprecationWarning: ast.Str) come from pytest on Python 3.12, 
  not your code. It is safe to ignore and will still pass.
- Once pushed, GitHub Actions will run lint/tests.