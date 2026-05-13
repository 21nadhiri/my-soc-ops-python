# AGENTS

## ✓ Development Checklist
- [ ] Lint: `uv run ruff check .`
- [ ] Build/Sync: `uv sync`
- [ ] Test: `uv run pytest`

## Project
FastAPI + Jinja2 + HTMX session-based Social Bingo game with server-rendered templates. Core files: `app/main.py`, `app/game_service.py`, `app/game_logic.py`, `app/models.py`. Templates in `app/templates/` and `app/templates/components/`.

## Commands
- `uv sync` – install/sync dependencies
- `uv run pytest` – run tests
- `uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000` – dev server
- `uv run ruff check .` – lint

## Agent Guidance
- Work in `app/` and `tests/` folders.
- Keep HTMX server-rendered flows intact.
- Update tests when changing behavior.
- Python 3.13+ required.
- **No VS Code Simple Browser** – HTMX requires a real browser.
- Avoid `.solutions/` folder; it's for lab reference only.

## References
[README.md](README.md), [Frontend Design](https://github.com/21nadhiri/my-soc-ops-python/blob/main/.github/instructions/frontend-design.instructions.md), [CSS Utilities](https://github.com/21nadhiri/my-soc-ops-python/blob/main/.github/instructions/css-utilities.instructions.md)
