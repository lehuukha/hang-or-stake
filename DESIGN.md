# Hang or Stake design

## Direction
Compact outdoor finder with a separate reading panel. Replaces the rejected marketing introduction, persistent sidebar and repeated park sections. The user requested clarity, substantially less clutter and the craft of an established premium outdoor product; design decisions were delegated to Codex.

## Reference study
[AllTrails Minnesota explorer](https://www.alltrails.com/explore/us/minnesota) informed the compact control bar and stable results/detail relationship. [WTA Hiking Guide](https://www.wta.org/go-outside/hikes) informed separation of browse summaries and longer reading. [The Dyrt](https://thedyrt.com/) and [Hiking Project](https://www.hikingproject.com/) were also consulted for discovery structure. No reference photography, branding, map geometry or ratings were copied.

The Impeccable direction seed was run. The user's requested familiar, clear outdoor-finder direction takes precedence over the unrelated stylistic challengers. Compact controls and a disciplined comparison grid serve the actual campsite task.

## Visual system
- Warm pale canvas (#f5f4ef), white reading surface, dark green ink (#22352e), muted ink (#606d66), restrained forest accent (#255b43).
- Manrope for navigation, facts and lists; Newsreader for campsite titles and report headlines. System fallbacks remain available if fonts fail.
- Single comparison list, fine separators, restrained rounded outer surfaces. No decorative hero, dashboard statistics or synthetic campsite photography.
- Explicit dark appearance retained, including a switch in About for phone access.

## Interaction
- Campsites, Trip logs and About are separate views.
- One control bar: search, shelter choice, area and a closed-by-default filter disclosure.
- Results sort across areas, with exact campsite-name searches first. Owner stays break equal-score ties. Show more expands the initial eight results.
- Desktop: list left, selected campsite right. Overview, Stay report (when available), Sources & notes separate different reading tasks.
- Phone: list first; selecting a site opens a full-width detail screen with Back. No inline expansion of the entire results list.
- Evidence remains available in the source tab, with source-check scope and inherited-assessment labels. Unknowns and estimates are preserved.
- Schematic map is optional, explicitly labeled, with no claim of navigation accuracy.

## Verification, September 6, 2026
Desktop inspection plus local iframe tests at 390px and 320px outer widths. Browser viewport override did not take effect, so the iframe harness supplied real responsive document widths. Both documents had no horizontal overflow. Checked owner log selection, mobile report/back behavior, exact-name search, no-match/reset, group exclusion, owner filtering, tent sorting, source disclosure and map open/close. JavaScript syntax valid; browser error log empty in tested flows. Full source audit remains incomplete and is documented separately.
