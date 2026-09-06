# Session log (newest first). Every tool appends an entry when it stops working.

## 2026-09-06 - Codex, visual redesign
- Rebuilt the guide as a modern campsite browser: new typography, light/dark themes, desktop filter sidebar, mobile filter disclosure, readable numeric ratings, featured B11 stay-report shortcut, separate map dialog and expandable source evidence.
- Added field-tested filtering, visible result totals and reset/empty-state actions. Full area selection and search reveal all matching sites; all-area browsing initially shows five per area.
- Preserved all campsite records, scores, quotes and estimates byte-for-byte; no additional site facts introduced. Added PRODUCT.md and DESIGN.md for future design continuity.
- Validation: JavaScript syntax and whitespace checks; comparison of all site/park data with the prior commit; browser checks for search, gear ordering, rating filters, group exclusion, field-tested filter, empty/reset states, source disclosure, B11 shortcut, map selection and light/dark themes. Phone checks at 390px and 320px found no horizontal overflow; browser reported no JavaScript errors.
- Open: measured B11 spans and direct walk-in distance remain unavailable. The area map remains schematic.

## 2026-09-06 - Codex
- Added the owner's Sept 5-6 B11 solo stay report, tree location, suspension reach limits, warmth and bug observations. Marked B11 field-tested and updated the total to two.
- Direct walk-in about 0.75 mile and four hammocks plus two tents are explicitly owner estimates; spans remain not measured. Existing scores and earlier tent evidence retained, with limits of field verification stated.
- Corrected stale publish-path instructions in HANDOFF.md; publisher already uses repo-relative paths. Regenerated index.html.
- Open: measured spans and direct walk-in distance remain unavailable.

## 2026-09-05 — Claude Code
- Moved the project out of a Claude scratchpad into `D:\hang-or-stake` so Claude Code and Codex share one folder.
- Added `src/` (page source and build scripts), `data/` (site CSV and research JSON), `notes/` (fetched Reddit threads, gitignored), `docs/` (gear context, decision briefs, Codex kickoff prompt), `HANDOFF.md`, `AGENTS.md`, `CLAUDE.md`.
- Fixed `src/publish_pages.py` to use repo-relative paths; regenerated `index.html` from it (no content change intended).
- Open: fold in the owner's Sept 5-6 Lake Maria B11 stay report (bear locker confirmed; walk-in distance and hang span not yet recorded). Push to GitHub not yet done from this folder.
