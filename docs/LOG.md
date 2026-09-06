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

## 2026-09-06 - Codex, independent research and trip logs
- Rewrote B11 and Pine Ridge as readable trip logs with original notes retained; added Trip logs navigation.
- Independently read YouTube captions, Reddit indexed threads, BWCA and Hammock Forums discussions, and agency pages. Applied Afton 8/12/25, Cleary, Sakatah, Stanley Eddy, Lake Elmo and Cannon River corrections; replaced broad footer advice with current linked policies.
- Added per-entry source-check links and scope. Unchecked original assessments explicitly labeled. Audit sources, conflicts, failed fetches and remaining work are in RESEARCH_2026-09-06.md.
- Historical CSVs are not updated source truth; preserve current source-page corrections if using the old generators.

## 2026-09-06 - Codex, compact finder replacement
- Studied AllTrails, WTA, The Dyrt and Hiking Project. Replaced the large intro, filter sidebar and repeated area sections with a compact cross-area list and selected-site panel.
- Separate Campsites, Trip logs and About views. Overview, Stay report and Sources tabs keep long reports/evidence out of the comparison list. Phone selection opens a detail screen with Back.
- Exact campsite names sort ahead of incidental mentions. Search, filters, map, unknown ratings and original evidence retained.
- Desktop and 390px/320px iframe responsive checks passed without horizontal overflow. Owner report flow, exact-name search, empty/reset, owner/group filters, tent sorting and map controls checked; browser errors empty. Standard viewport override was ineffective, so a temporary iframe harness was used and removed afterward.
- Remaining: full independent audit of inherited campsite ratings, measured spans and owner-supplied photographs. See RESEARCH_2026-09-06.md.

## 2026-09-06 - Codex, park directory redesign
- User rejected the split-panel design as still too artificial. Replaced it with a park-first directory, full-width campsite lists and full-page reading views.
- Added real, attributed DNR park photos for Lake Maria, Afton and Wild River. Park photos are explicitly distinguished from campsite photos. No synthetic scenery or new campsite claims.
- Changed typography to Public Sans / Barlow Condensed and removed the dashboard panel treatment. Less repeated audit text while browsing; full source status remains within each listing.
- Verified identical SITES block, photo loading, park/site navigation, Back, trip logs, search/source access and 390px/320px iframe layouts without horizontal overflow. Browser errors empty in exercised flows.
- Open: independent source audit remains incomplete; owner site photos and measured spans are still unavailable.
