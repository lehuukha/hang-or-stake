# Hang or Stake design

## Intent
A modern campsite browser with a clear editorial introduction and a practical comparison workspace. Light is the default for use while planning trips or checking a phone outdoors; a persistent dark-theme control supports evening use.

## Typography
Manrope with system-ui fallback. Strong, compact headings; restrained supporting text. Labels and source text use sentence case. No decorative display font or all-caps badges repeated across every row.

## Color
Light: white surfaces, #f6f7f8 canvas, #192c26 primary ink, #5c6c66 secondary ink, #22634d accent.
Dark: #111b17 canvas, #18251f surface, #f0f5f2 primary ink, #b3c4ba secondary ink, #afe1c6 accent.
Accent signals selection, links, and field evidence. Numeric ratings and text carry meaning without depending on color.

## Layout and interaction
- Sticky masthead with navigation and theme switch.
- Brief introduction and latest B11 stay report shortcut.
- Setup switch and search above the browser.
- Sticky filter sidebar on desktop; collapsible filter panel on phones.
- Campsites grouped by park, with five initially shown per area when browsing all areas. Search or choosing an area reveals all matches.
- Numeric hammock and tent ratings side by side; supporting details and source evidence expand inline.
- Native modal dialog for the schematic area map, with Escape and close-button support.
- Unknowns, inferred labels, capacity estimates and quotes remain part of the underlying data.

## Accessibility
Explicit input labels, pressed-state setup buttons, live result count, native details and dialog controls, visible keyboard focus and reduced-motion handling. Checked in desktop and 390px/320px phone viewports without horizontal overflow. Light and dark foreground/background text pairs checked for WCAG AA contrast.
