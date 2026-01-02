.PHONY: run test test-v lint format clean help

run: ## Run all examples
	uv run python main.py

test: ## Run tests
	uv run pytest

test-v: ## Run tests with verbose output
	uv run pytest -v

test-cov: ## Run tests with coverage
	uv run pytest --cov=core --cov=examples --cov-report=term-missing

lint: ## Run linter
	uv run ruff check .

format: ## Format code
	uv run ruff format .

typecheck: ## Run type checker
	uv run pyright

sync: ## Sync dependencies
	uv sync

clean: ## Clean cache files
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
