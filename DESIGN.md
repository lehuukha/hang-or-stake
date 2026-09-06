# Hang or Stake design

## Current direction, September 6, 2026
The owner rejected both the spacious introduction and compact split-panel dashboard. The site now starts with a park directory, using actual Minnesota DNR park photographs. Choosing a park opens a full-width campsite list; choosing a campsite opens a full-page reading view with Back. Sources and reports remain separate tabs within that view.

## Visual language
White background, charcoal text, understated olive accents, straight-edged controls and open layouts. Public Sans for reading and UI, Barlow Condensed for the wordmark and place headings. No oversized numbered campsite title floating in a dashboard panel. No repeated pending-research message on every browse row; verification scope remains explicit inside each entry.

Lake Maria, Afton and Wild River use banner images verified on their official DNR pages. Photos load from the DNR image host, link back to their source, and are labeled as park landscapes, never photographs of individual campsites. Other areas use a plain text directory rather than invented or irrelevant images. External images and fonts depend on their hosts; names, navigation and data still work without them.

## Interaction
- Campsites navigation returns to the park directory.
- Search and advanced filters can show matching campsite listings across parks.
- Shelter choice controls score ordering. All source data, unknowns and estimates are retained.
- Campsite reading uses the full content width, with Overview, Stay report when available, and Sources & notes.
- Trip logs opens the two owner reports directly through their list entries.
- On phones, park photographs become small thumbnails alongside the place descriptions. No horizontal overflow was found in 390px and 320px iframe tests.
- Dark appearance is retained. The optional area explorer uses a geographic map with a searchable park list. All 18 areas have official-source references, with scope explained in the selection panel. The combined forest entry has two facility pins; Rum River uses a labeled map-extent center.

## Verification
Compared the entire SITES data block with the prior commit: identical. Checked park selection, full-page campsite selection, Back, both trip logs, exact-name search, source access and image loading. Desktop and phone screenshots inspected; browser error log empty in tested flows.
