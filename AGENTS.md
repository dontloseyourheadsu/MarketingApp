# Repository Guidelines

## Project Structure & Module Organization
- `frontend/`: Angular app (feature modules under `src/app`, assets in `src/assets`).
- `backend/`: Axum (Rust) service (`src/` for code, `tests/` for integration tests).
- `README.md`: High‑level scope and tech stack.

## Build, Test, and Development Commands
- Frontend dev: `cd frontend && npm install && npm start` (runs `ng serve` on localhost).
- Frontend build: `npm run build` (production bundle to `dist/`).
- Backend dev: `cd backend && cargo run` (starts Axum server with hot compile).
- Backend test: `cargo test` (unit + integration tests).
- Lint/format: Frontend `npm run lint && npm run format`; Backend `cargo clippy && cargo fmt`.

## Coding Style & Naming Conventions
- TypeScript: 2‑space indent; use ESLint + Prettier. Files `kebab-case.ts`; classes/interfaces `PascalCase`; variables/functions `camelCase`.
- Rust: format with `rustfmt`; prefer `clippy` clean. Files and functions `snake_case`; types/traits `PascalCase`; constants `SCREAMING_SNAKE_CASE`.
- Modules: Group Angular features by folder; keep Rust crates/modules cohesive by domain (handlers, services, repos).

## Testing Guidelines
- Frontend: Spec files `*.spec.ts` colocated with components; run `npm test` or `ng test`.
- Backend: Unit tests in module files with `#[cfg(test)]`; integration tests under `backend/tests/`.
- Coverage: Aim for critical paths (auth, ads delivery, media upload) with meaningful assertions; prefer fast, deterministic tests.

## Commit & Pull Request Guidelines
- History shows short, descriptive subjects (e.g., “Unsubscribe flow”). Keep subject ≤ 50 chars, imperative mood, with context in body as needed.
- Reference issues/PRs with `#123`. Squash merges preferred.
- PRs: Include summary, screenshots for UI changes, reproduction steps, and any schema/config changes. Link related issues.

## Security & Configuration Tips
- Do not commit secrets. Use env vars for `DATABASE_URL`, `JWT_SECRET`, and AWS credentials. Provide a redacted `.env.example`.
- Validate inputs at API boundaries; enforce auth on all mutating routes.
- For local dev, use a separate Postgres DB and an S3 mock or a dedicated test bucket.

