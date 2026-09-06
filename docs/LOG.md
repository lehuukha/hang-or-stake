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

## 2026-09-06 - Codex, geographic area map
- Replaced the hand-positioned SVG and approximate drive-time rings with a lazy-loaded Leaflet/OpenStreetMap explorer. Searchable area list, keyboard-accessible pins, listing counts, zoom/reset and direct campsite browsing.
- Eight state-park reference points sourced from the Minnesota DNR Compass service, with exact coordinates and retrieval date in data/park_locations.json and source links in the selection panel. These are not campsite or trailhead positions. Ten other areas remain selectable without invented pins.
- Mobile layout puts the map above the searchable list. External-library failure retains working park selection. No location permission requested and no tiles prefetched.
- Checked JavaScript syntax, desktop map/selection, 390px and 320px layouts without overflow, unknown-location selection and simulated library failure. Original SITES data unchanged.
- Open: source coordinates for the remaining county/forest/river areas; broader campsite-source audit remains incomplete.

## 2026-09-06 - Codex, remaining map locations verified
- Verified all ten previously unpinned areas from official Three Rivers, Rice/Wright/Washington county, Minnesota/Wisconsin DNR, and NPS coordinate sources. All 18 areas now have sourced geographic references; the combined St. Croix/Chengwatana entry has two facility pins.
- Rum River is explicitly a calculated center of the official DNR bounding box, with its map extent shown on selection. The extent is not claimed to be a legal boundary. Other broad areas use named facility references, with scope explained and linked in the panel.
- Osceola Landing coordinates were read from page 55 of the NPS response-strategy PDF. They are a landing reference, not an individual campsite or surveyed current ramp position. Governor Knowles uses the official headquarters directions pin, not Randall Creek.
- Preserved campsite ratings/reports. Checked all 18 location keys, 19 rendered pins, forest selection/extent, source links and campsite navigation. Phone selection notes scroll within a capped panel.
- Previous location-verification open item is closed. Exact campsite pins and the separate inherited campsite-score audit remain outside this verification.

## 2026-09-06 - Codex, Muddy Boots Camping source triage
- Inspected the user-supplied YouTube channel's Latest and Oldest catalogs in the browser. Saved site-specific links for Afton 1-27, boat/canoe site 1 and the campground overview, plus BWCA leads, in MUDDY_BOOTS_SOURCE_INVENTORY.md.
- Rechecked dated captions for Afton 8 and 25. These are already-used sources, not independent new corroboration. No campsite scores or live-page content changed.
- Flagged conflicting Smoke/Flame titles for BWCA campsite 918. Full remaining-video review is pending; inventory entries explicitly distinguish titles checked from captions reviewed.

## 2026-09-06 - Codex, all-area campsite-count audit
- Audited all 18 areas using official DNR camping data and notes, Three Rivers details and 2026 Cleary map, county inventories/maps, Wisconsin DNR and NPS section maps. Findings and provenance are in docs/CAMPING_INVENTORY_AUDIT.md and data/camping_inventory.json.
- Replaced guide-entry counts in park directory and map pins with actual scoped inventory. Park pages distinguish count breakdown/source/status from the number of guide entries. Group, bike-only, paddle-access and dispersed categories stay separate.
- Confirmed Afton 27+1, Lake Maria 17 plus B1 closure, Wild River 8, Nerstrand 4+6, Frontenac 2+6, Cleary 14, Lake Elmo 5, William O'Brien 2 (130/131), Cannon River 4, Stanley Eddy 12 and Governor Knowles 9. Ann Lake has six mapped walk-ins with current operational breakdown not reconfirmed. No invented fixed dispersed total.
- Added Wild River Breezy Valley and Meadow Vista, corrected Dry Creek to Dry Creek Hollow, and added Nerstrand's cart-in category. New entries have unknown hammock/tent ratings.
- Withdrew Minnesota Valley's historical eight-walk-in claim as current inventory and cleared unsupported current tent ratings on its two historical entries. Current DNR page/map lists equestrian camping only; direct DNR confirmation remains required. Removed unsupported NPS blanket count of 13 from current listing/park prose.
- Count audit also surfaced a DNR note that neither Frontenac backpack site is good for hammocks; added it without assigning a new score. Marked Lake Maria B1 closed per the August 2026 alert and removed its Solo pick; retained historical evidence.
- JavaScript syntax, 18 inventory keys, 74 guide entries, eight Wild River entries, unknown new ratings, 320px directory/source disclosure overflow and map count/source navigation checked. Grouped entries still represent multiple sites; individual suitability audit remains separate work.
