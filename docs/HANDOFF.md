# Current state

Updated 2026-10-22. Switchback Foundry is a public, standalone project; the playable copy remains at https://kevinmneal.com/lab/switchback/.

## Working layout

- `dist/`: complete static runtime, including local base styles, theme control, and favicon.
- `tests/check-model.mjs`: independent rule and puzzle-property checker.
- `scripts/build-preview.py`: optional single-file HTML export.
- `docs/DEVELOPMENT.md`: full rules, interaction behavior, solution properties, and prior browser verification.
- `.github/workflows/check.yml`: model and syntax checks; no deployment.

The source was extracted from the homepage release `2e1616dba8ffaee2f39c3c9c8766370a30530af7`, using the current homepage tree at `b800c31`. The model, app, puzzle CSS, base CSS, theme logic, and favicon were preserved byte-for-byte. Puzzle data is unchanged; its verification-command comment now points to `npm test`. HTML asset/navigation paths and the source link changed. The independent checker changed its import paths only.

## Current design

One curated maze, `long-way-round-v2`, with two movement actions, one switch, undo, and reset. Help unfolds gradually. Any first escape is celebrated before the optional route challenge. The switch experiment requires a prediction before a requested verdict. Walkthroughs preserve the player's run and do not award a personal win. Progress is in memory and resets on reload.

Verified puzzle structure includes a unique 11-move shortest route, an early recoverable fork, meaningful 13- and 17-move alternatives, a necessary position revisit, and an unreachable exit after replacing the switch with floor. These are structural properties, not a measure of enjoyment.

## Verification

`npm test` checks 600 restart states and 1,200 transitions plus shortest counting, witnesses, repeated switch entry, terminal behavior, edited-board isolation, and route-choice properties. `npm run check` checks runtime and test syntax. Prior browser verification covered hints, 11- and 13-move wins, challenge opt-in, saved-run restoration, prediction gating, edited-board play, desktop and narrow layouts, and both themes.

Extraction checks confirmed all local runtime assets resolve, unchanged application behavior, and an export with 68 unique element IDs, two syntactically valid inline modules, and no external runtime assets. The standalone HTTP preview was exercised through hints, an 11-move personal win, reset, and theme switching. Desktop dark and 390-pixel-wide light layouts were visually inspected; no browser warnings or errors appeared. An independent extraction review found and corrected one stale verification-command comment.

Physical-device and spoken screen-reader audits remain outstanding. Direct-file export launch has not been visually tested; HTTP playback and export syntax/structure have been checked.

## Publishing the website copy

After authorized changes are checked and committed here, run from a clean homepage checkout:

```sh
python3 scripts/sync-switchback.py --source /path/to/switchback-foundry
python3 scripts/sync-switchback.py --check
python3 scripts/build-agent-pages.py --check
```

The homepage snapshot records the source revision and SHA-256 of every hosted file. Inspect the diff and preview before an authorized homepage push. The live address stays the same; this source repository's checks do not deploy it automatically.

## Next useful work

Observe first-time players: do they understand turn-and-step, plan a useful return, and see why switch arrival matters? Use those observations before expanding or changing the maze. No generator, daily service, accounts, or leaderboard is currently planned.
