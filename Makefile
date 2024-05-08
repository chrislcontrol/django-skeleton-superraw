PIP := pip install
DATABASE_PASS := postgres

PROJECT_NAME := django-project
PYTHON_VERSION := 3.11.4
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)


# Setup dependencies
.pip:
	pip install --upgrade pip

setup-dev: .pip
	$(PIP) requirements/requirements-dev.txt

# Create virtualenv
.create-venv:
	pyenv install -s $(PYTHON_VERSION)
	pyenv uninstall -f $(VENV_NAME)
	pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME)
	pyenv local $(VENV_NAME)

create-venv: .create-venv setup-dev

# Containers:
# Postgres Local
run-postgres:
	docker start $(PROJECT_NAME)-postgres 2>/dev/null || docker run --name $(PROJECT_NAME)-postgres -p 5432:5432 -e POSTGRES_PASSWORD='$(DATABASE_PASS)' -d postgres:15-alpine

containers-down:
	docker stop $$(docker ps -aq)

containers-up: run-postgres

containers-reset: containers-down containers-up

# Tests
test:
	pytest -v --cov-report=term-missing  --cov-report=html --cov=.

# Code convention
code-convention:
	flake8
	pycodestyle
