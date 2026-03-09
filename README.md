# Python CI/CD Pipeline Demo

A reference project demonstrating a production-grade CI/CD pipeline for a Python Flask application using GitHub Actions.

## What This Demonstrates

- **Three-stage pipeline**: Feature branch CI → Staging → Production
- **Fail-fast gates**: Lint and format checks run before tests; tests run before Docker builds
- **Immutable image tags**: Every image is tagged with its Git SHA — no `latest` in CI
- **Image promotion**: The same image binary is promoted through Dev → Staging → Prod (no rebuilds)
- **Manual approval gate**: Production deployments require an explicit reviewer sign-off via GitHub Environments
- **Pre-commit hooks**: Black (formatting), Flake8 (linting), detect-secrets (credential scanning), and general hygiene checks

## Project Layout

```
app/            Flask app + business logic
tests/          Pytest unit and integration tests
.github/
  workflows/
    feature-ci.yml   Lint → Test → Build & push dev image (on feature/* and fix/*)
    staging.yml      Re-verify → Promote image → Deploy (on push to main)
    production.yml   Manual dispatch with approval gate → Promote → Deploy
.pre-commit-config.yaml
Dockerfile           Multi-stage build (builder + non-root runtime)
docker-compose.yml   Local dev stack
```

## Quick Start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
pre-commit install          # install git hooks
pytest                      # run tests
black --check .             # check formatting
flake8 .                    # lint
docker compose up --build   # run locally
```
