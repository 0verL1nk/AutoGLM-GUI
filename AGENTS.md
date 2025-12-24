# Repository Guidelines

## Project Structure & Module Organization

- `AutoGLM_GUI/` FastAPI backend; API routes in `AutoGLM_GUI/api/`, configuration and state helpers nearby.
- `phone_agent/` device control layers (adb/hdc/xctest) plus prompts and device configs.
- `frontend/` React + TanStack Router UI; entry in `frontend/src/main.tsx`, styles in `frontend/src/styles.css`.
- `electron/` desktop shell and packaging assets.
- `scripts/` build, lint, and release utilities.
- `scrcpy-server-v3.3.3/` bundled scrcpy server used for streaming.

## Build, Test, and Development Commands

- `uv sync` installs Python dependencies.
- `uv run autoglm-gui --base-url http://localhost:8080/v1 --reload` runs the backend (always use `uv run`, never call `python` directly).
- `uv run python scripts/build.py` builds frontend assets required by the backend; add `--pack` to build the wheel.
- `cd frontend && pnpm install` then `pnpm dev` for the UI dev server; `pnpm build` for production.
- `cd frontend && pnpm type-check`, `pnpm lint`, `pnpm format` for frontend checks and formatting.
- `uv run python scripts/build_electron.py` builds the desktop app; `cd electron && npm run dev` for Electron dev.

## Coding Style & Naming Conventions

- Python: 4-space indentation, PEP 8 naming (`snake_case` functions, `PascalCase` classes), keep module boundaries consistent.
- Frontend: components in `PascalCase`, hooks prefixed with `use`, format with Prettier and lint with ESLint.

## Testing Guidelines

- No dedicated automated test suite yet; rely on `pnpm type-check`/`pnpm lint` and a local smoke run of `uv run autoglm-gui`.
- If adding tests, introduce a `tests/` directory and mirror module names for clarity.

## Commit & Pull Request Guidelines

- Commit messages follow Conventional Commits (examples: `feat(ui): ...`, `fix(ui): ...`, `release v1.0.0`).
- PRs should include a brief summary, linked issues when applicable, and screenshots/gifs for UI changes. Note device/OS used for manual verification.

## Configuration & Security

- Persistent config lives at `~/.config/autoglm/config.json`; never commit API keys and redact secrets in logs or screenshots.
