# OSCA — Makefile
# Version: 0.1.0-research-draft
# Date: 2026-11-01

.PHONY: help install structure test lint format clean verify

PYTHON ?= python

help:
	@echo "OSCA — available targets"
	@echo ""
	@echo "  install          Install package in editable mode (with dev deps)"
	@echo "  structure        Check project structure"
	@echo ""
	@echo "  test             Run pytest test suite"
	@echo "  lint             Run linters (flake8)"
	@echo "  format           Format code (black, isort)"
	@echo ""
	@echo "  verify           Run structure + tests + lint"
	@echo "  clean            Remove caches and build artifacts"

install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -e ".[dev]"

structure:
	@echo "OSCA — structure:"
	@test -f README.md && echo "  README.md" || echo "  MISSING README.md"
	@test -f VERSION && echo "  VERSION" || echo "  MISSING VERSION"
	@test -f LICENSE && echo "  LICENSE" || echo "  MISSING LICENSE"
	@test -f CITATION.cff && echo "  CITATION.cff" || echo "  MISSING CITATION.cff"
	@test -f CHANGELOG.md && echo "  CHANGELOG.md" || echo "  MISSING CHANGELOG.md"
	@test -f AUTHORS.md && echo "  AUTHORS.md" || echo "  MISSING AUTHORS.md"
	@test -f CONTRIBUTING.md && echo "  CONTRIBUTING.md" || echo "  MISSING CONTRIBUTING.md"
	@test -f pyproject.toml && echo "  pyproject.toml" || echo "  MISSING pyproject.toml"
	@test -f requirements.txt && echo "  requirements.txt" || echo "  MISSING requirements.txt"
	@echo ""
	@test -d core && echo "  core/" || echo "  MISSING core/"
	@test -d invariants && echo "  invariants/" || echo "  MISSING invariants/"
	@test -d tests && echo "  tests/" || echo "  MISSING tests/"
	@test -d DOCS && echo "  DOCS/" || echo "  MISSING DOCS/"

test:
	$(PYTHON) -m pytest tests/ -v

lint:
	@echo "==> flake8"
	-flake8 core invariants tests --max-line-length=88 --extend-ignore=E203,W503
	@echo ""

format:
	@echo "==> isort"
	isort core invariants tests
	@echo "==> black"
	black core invariants tests --line-length=88

verify: structure test lint

clean:
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf __pycache__/
	rm -rf */__pycache__/
	rm -rf */*/__pycache__/
	rm -rf *.egg-info/
	rm -rf build/ dist/
	rm -rf .coverage
	rm -rf htmlcov/
