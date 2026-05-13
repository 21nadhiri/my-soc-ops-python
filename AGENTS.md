# AGENTS

## What this project is
- A Python web app built with FastAPI + Jinja2 + HTMX.
- The app is a session-based Social Bingo game with server-rendered templates and HTMX-driven interactions.
- Key app files: `app/main.py`, `app/game_service.py`, `app/game_logic.py`, `app/models.py`, and `app/data.py`.
- Templates live under `app/templates` and `app/templates/components`; static assets under `app/static`.

## Supported workflows
- Install and sync dependencies: `uv sync`
- Run tests: `uv run pytest`
- Run the app locally: `uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`
- Lint proactively with: `uv run ruff check .`

## Agent guidance
- Prefer working in the `app/` and `tests/` folders.
- Keep HTMX usage intact and avoid replacing server-rendered component flows with client-side SPA code unless the task explicitly requires it.
- Use existing templates and partial includes when modifying the UI.
- When changing behavior, update or add tests in `tests/` and confirm with `uv run pytest`.
- If dependencies or packaging change, sync the environment again with `uv sync`.

## Important notes
- This repo uses Python 3.13+.
- The app is designed to run in a real browser; do not use VS Code Simple Browser for HTMX validation.
- `app/main.py` defines session-based endpoints and renders template fragments for HTMX responses.
- `.solutions/` contains lab solutions and should not be the primary source for feature implementation.

## Helpful docs
- `README.md`
- `.github/instructions/frontend-design.instructions.md`
- `.github/instructions/css-utilities.instructions.md`
- `workshop/` for lab background and context
