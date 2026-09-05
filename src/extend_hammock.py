# -*- coding: utf-8 -*-
"""Append the newly researched parks and enrich the Lake Maria gap rows."""
import csv, io, pathlib

src = pathlib.Path(r"C:\Users\Kha\AppData\Local\Temp\claude\D--claude\96536e7d-aa84-46b2-b579-a1a8fd3f6d27\scratchpad\hammock.csv")
rows = list(csv.reader(io.StringIO(src.read_text(encoding="utf-8"))))
hdr, body = rows[0], rows[1:]

gap = {
 "B7": ("", "Gap-filled (SCOUT)", "", "not stated",
        "Island-feel knoll; steep climb after a marsh boardwalk/bridge; tent spots for two",
        "The most secluded site; surrounded by marsh, feels like an island; birch on site",
        "Cipher-Tu (tent camper) calls it his favorite - 'I absolutely love this site' - but gives no tree-spacing read; higher-effort approach; latrine placement he dislikes. Horses share the trail May 1-Nov 1 (MN Hiker).",
        "SCOUT walkthrough 4/2026: 'it kind of feels like you're on an island... I love this site' (no hammock read)"),
 "B8": ("1", "Poor (inferred)", "0-1", "trees a little far apart",
        "Mild slant; flat tent area with roots; downhill entry",
        "Close to Lake Maria with a lake view; new bear locker; latrine uphill",
        "INFERRED downgrade: the SCOUT walkthrough notes 'tree is a little far away' and a widow-maker on site - both bad signs for hanging. MN Hiker's guess that it resembled B11 does not hold for hammocks.",
        "SCOUT walkthrough 4/2026: 'This site looks amazing. Tree is a little far away... Widowmaker action' (no hammock read)"),
 "B14": ("", "Gap-filled (SCOUT)", "", "not stated",
        "Two prime tent areas; obviously tentable ground",
        "Best/closest view of Lake Maria - 'pretty much right on' the lake; shared latrine with B15",
        "Most popular site in the park, first to book (both sources agree). One 'really awesome' big tree on site; no tree-pair info for hanging - treat as tent-first until walked.",
        "SCOUT walkthrough 4/2026: 'probably the most popular site... most awesome view... I would highly recommend this site' (no hammock read)"),
}
for r in body:
    if r[0] == "Lake Maria" and r[1] in gap:
        g = gap[r[1]]
        r[2:] = list(g)

NEW = [
 ("Wild River", "Aspen Knob", "4", "Confirmed hang", "2+ (two best trees)", "not stated",
  "Tent pad, fire ring, bear box, own latrine; 1.3 mi in, rolling but gentler than Afton",
  "Set 150-200 ft off the main trail, fully wooded, no lake/river view, little sky",
  "PARK OFFICE RECOMMENDED for hammocks (by email) and the videographer hung here. Bugs moderate; wood gatherable at backpack sites.",
  "Trip video (Tjev63PKq14): 'those two trees in the center of the frame are the best options for hanging a hammock... Aspen Knob's certainly suitable'"),
 ("Wild River", "Spring Creek", "3", "Office-recommended", "not stated", "not stated",
  "Backpack site off the River Trail",
  "Along the St. Croix, ~1 mi from the boat landing, river views on the walk in",
  "The other of the two sites the park office named when asked which suit hammocks; no first-hand hang footage found.",
  "Same video: 'when I was emailing the park office about suitable places to hammock camp they recommended this one as well as Aspen Knob'"),
 ("Wild River", "Deer Creek", "3", "One good hang (reviewer)", "1", "not stated",
  "Fire ring and picnic table overlooking creek and river",
  "~30 min hike from the visitor center; also canoe-accessible",
  "A Tripadvisor camper found a pine-grove nook that fits a small tent or 'the perfect spot to hang a hammock'.",
  "Tripadvisor review: 'a spot nestled in some pine trees... the perfect spot to hang a hammock'"),
 ("Wild River", "Buck Hill", "0", "Avoid for hanging", "0", "-",
  "Beautiful site otherwise", "Backpack site",
  "A four-person hammock group had to abandon it and rebook another site.",
  "Backpacking with Barkley (e8NB4gLUhWY): 'there is not a single hammock option... not hammock friendly at all'"),
 ("Wild River", "Dry Creek", "", "Not assessed", "", "",
  "", "Beyond a run of steep hills past Aspen Knob",
  "The Aspen Knob videographer turned around at the hills; park office warned wood may be scarce there.",
  "Same video: 'a lot of hills including this really steep one that made me think enough was enough'"),
 ("Nerstrand Big Woods", "Walk-in sites (4)", "", "Likely good (inferred)", "", "not surveyed",
  "Tent-only walk-ins; easy access",
  "Maple-basswood old-growth Big Woods remnant; waterfall hike; ~40 min south by Northfield",
  "INFERRED: mature hardwood forest almost guarantees hangable pairs, but nobody has published a site-level survey; the SCOUT all-camp-spots video has no captions to mine. Forum posters recommend it for a first hang.",
  "hammockforums (zoo, 2012): 'Nerstrand State Park - primitive walk-in sites: good hiking, nice waterfall... easy access'"),
 ("Frontenac", "Cart-in C6", "", "Most private (inferred)", "", "not stated",
  "Ground rough and lumpy for tents - which favors a hammock if pairs exist",
  "Just over the bluff from the Mississippi/Lake Pepin, across from Maiden Rock; most secluded site in the park bar the backpack pair",
  "INFERRED: the SCOUT narrator (tent camper) never rates hangs; he calls C6 the most private secluded campsite in the park but not ideal for a tent - scout trees in person.",
  "SCOUT cart-in video (o6Foux_2hYk): 'this is the most private site... laying a tent on this wouldn't be kind'"),
 ("Frontenac", "Cart-in C3", "", "Narrator's pick (inferred)", "", "not stated",
  "Level grass, good fire pit",
  "Closest to the (very nice) vault toilet; C4 is uncomfortably close next door",
  "His favorite cart-in and the one he booked; a 'really cool tree' on site. No hammock info - inferred only.",
  "Same video: 'you got this really cool tree right here... this is my favorite site so far here'"),
 ("Frontenac", "Backpack sites (2)", "", "Not assessed", "", "",
  "Wood provided", "A hike out from the cart-in area; the two sites sit near each other",
  "Exist per the SCOUT narrator; no walkthrough with captions found.",
  "Same video: 'there are backpack sites over there... they do provide wood over there'"),
 ("Sand Dunes SF", "Dispersed / Ann Lake walk-ins", "", "Confirmed hangs, one hazard", "", "your pick",
  "Free dispersed camping plus walk-in sites at the campground",
  "Oak/pine forest by Zimmerman; quietest after a hard freeze",
  "Forum hangers camp here without hassle - but POISON IVY is endemic: one regular got it badly twice, once in early spring in long clothing.",
  "hammockforums (mooseprime, 2016): 'the last 2 times I ventured into the Sand Dunes for dispersed camping, I got poison ivy pretty bad'"),
 ("Cleary Lake Regional", "Lakeside walk-in", "3", "One good site", "several trees", "not stated",
  "Walk-in on a trail with little foot traffic, no neighboring sites",
  "Right on the lake; closest option to the metro on this list (Prior Lake)",
  "The OTHER walk-ins at Cleary are explicitly NOT hammock-friendly - book the lakeside one. Canoe-in island group site also has room to hang.",
  "hammockforums (zoo, 2012): 'the one by the lake has some real nice trees to string up from... the other walk-in sites... aren't really conducive to hammocks'"),
 ("Sakatah Lake", "Site 3 (drive-in)", "5", "Group-hang best", "8-10", "not stated",
  "Drive-in campground - not backpacking",
  "Rangers hammock-friendly; on the Sakatah Singing Hills bike trail (Waterville)",
  "From a 2017 four-sister survey of the whole campground for group hangs. Max 6 campers/site. Runners-up: site 1 (4-6), sites 6 & 8 (5-6), site 11 (3-4). Three bike-in sites exist, unsurveyed.",
  "hammockforums (GingeGirl, 2017): 'Site 3: 8-10 hammocks' - full site-by-site list in the thread"),
]
for t in NEW:
    body.append(list(t))

out = io.StringIO()
w = csv.writer(out, lineterminator="\n")
w.writerow(hdr)
for r in body:
    w.writerow(r)
p = pathlib.Path(r"C:\Users\Kha\Downloads\MN_Hammock_Spots_Afton_LakeMaria.csv")
p.write_text(out.getvalue(), encoding="utf-8")
src.write_text(out.getvalue(), encoding="utf-8")  # keep scratch master in sync
print("rows now:", len(body), "| wrote", p)
