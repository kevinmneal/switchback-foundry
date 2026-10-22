# Switchback Foundry

The canonical application source is `dist/`. This is buildless HTML, CSS, SVG, and JavaScript. Keep runtime assets local and preserve the one-puzzle scope unless Kevin requests expansion.

- Read `docs/HANDOFF.md` and relevant development notes before substantive changes.
- Keep rules in `dist/model.mjs`, puzzle data and witnesses in `dist/puzzle.mjs`, and presentation in `dist/app.mjs`.
- Preserve gradual hints, optional solution disclosure, the first success celebration, and prediction before the switch experiment's verdict.
- Run `npm test`, `npm run check`, and `git diff --check`. Exercise affected interactions and inspect desktop/narrow presentation when UI changes.
- Run a local HTTP preview with `python3 -m http.server 8765 --bind 127.0.0.1 --directory dist`.
- The independent checker deliberately uses a separate transition and shortest-count implementation. Do not turn it into a call-through to the production solver.
- The homepage hosts a committed copy. Do not edit it independently; use its `scripts/sync-switchback.py` and snapshot check after an approved source commit.
- Commit, push, and publication require authorization. Do not add private workspace paths or conversation artifacts to public documentation.
- Keep evolving decisions and verification in `docs/HANDOFF.md`.
