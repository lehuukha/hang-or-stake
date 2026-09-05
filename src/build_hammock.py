# -*- coding: utf-8 -*-
"""Hammock-spot workbook built from the two MN Hiker campsite-walkthrough transcripts."""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

OUT = r"C:\Users\Kha\Downloads\MN_Hammock_Spots_Afton_LakeMaria.xlsx"

# score: 5 best .. 0 none/avoid ; None = not assessed on camera
AFTON = [
    # site, score, verdict, hangs, spans_ft, ground, setting, notes, quote
    ("25", 5, "Best in park", "3+", "11-13, plus a ~15", "Flat, lots of tent room",
     "Next to a small open prairie; far end of the trail, little foot traffic",
     "Multiple usable pairs plus room for many tents. Neighbors site 27.",
     "an excellent campsite for hammockers ... this is the best one by far"),
    ("3", 4, "Good", "several", "not measured", "Two tent pads", "Wooded, uphill from 0/1/2",
     "The densest timber he found; he suspects this stand is why the park keeps a wooded map for hammockers.",
     "lots of trees ... plenty of spots for hammocks here"),
    ("6", 4, "Good", "2-3", "not measured", "Two adjacent tent pads", "Wooded, primitive outhouse nearby",
     "Roomier than nearby 5; convenient to the privy.",
     "hammocking check you probably get two in there three if you're lucky"),
    ("22", 4, "Good", "2", "not measured", "Flat, a little muddy on one side", "End of the road past 21",
     "No real tent pads, so it favors hangers.",
     "probably more hammock friendly than anything"),
    ("27", 3, "Decent", "~2", "~10 (small hammock) + a longer pair",
     "One flat spot by the ring; rest on a slant", "End of the road up the main hill",
     "The 10 ft pair only works with a short hammock. Neighbors site 25.",
     "a good spot for about two hammocks maybe and then one comfortable tent"),
    ("21", 3, "Decent", "1-2", "~12", "Two tent pads", "Nestled in woods, not visible from 20",
     "A second option exists but sits on a deer trail; he'd skip that one.",
     "in general looks like one solid hammock spot"),
    ("11", 3, "Decent", "1-2", "not measured", "Mostly open, slightly tilted in spots",
     "Under a distinctive shade tree; near water, wood and the privy",
     "Big site - 3-4 tents alongside.",
     "I'd call this a one maybe two hammock site plus maybe three or four tents"),
    ("7", 3, "Decent", "1", "11-12, with a second tree as backup", "Open, muddy near the fire ring",
     "Prairie site on a cliff edge, big view",
     "Exposed - wind noise was constant on camera.",
     "pretty open as a hammock spot if you don't mind being on a cliff"),
    ("13", 2, "Marginal", "1", "~12", "Decent flat space for a couple of tents", "Wooded, heavy deer traffic",
     "One pair and that's it.",
     "maybe a hammock spot from there to there that looks to be about 12 feet that's about it"),
    ("15", 2, "Marginal", "1", "~13 (a second pair ~17 he'd skip)", "Very flat - among the flattest in the park",
     "Open site",
     "Signs someone has camped at the 13 ft pair before.",
     "as far as hammocks this is about a 13 foot gap"),
    ("20", 2, "Marginal", "1", "~13.5", "Two tent pads", "Wooded",
     "One span only.",
     "there is one spot right here it's about thirteen thirteen and a half feet across that's about it"),
    ("26", 2, "Marginal", "1", "not measured", "Noticeably slanted; one flat spot near the ring",
     "Big open field ringed by woods, on a corner of two roads",
     "Longest walk in the park; deer take refuge here.",
     "we've got a decent spot from that tree to that tree and that's about it"),
    ("1", 2, "Marginal", "maybe 1", "not measured", "Two tent pads", "Top of the first hill",
     "First site in; minimal beyond the pads, table and ring.",
     "maybe a hammock spot over there and really that's about it"),
    ("4", 1, "Poor", "maybe 1", "not measured", "Grass, no designated pads",
     "Overlooking the valley, just off the path",
     "Grass site with few trees.",
     "not really any hammock spots maybe this one just maybe"),
    ("8", 1, "Poor", "maybe 1", "11-12", "Open prairie, lots of tent space",
     "Beautiful prairie with a big view; privy nearby",
     "Two gigantic trees but nothing else usable.",
     "doesn't look like there's any real hammock spots maybe maybe those two"),
    ("18", 1, "Poor", "maybe 1", "not measured", "One tent pad", "Beautiful river view; fire ring right on the edge",
     "The one candidate pair sits too close to the tent pad.",
     "not too much in the way of hammock maybe one over there between those two"),
    ("17", 1, "Poor", "maybe 1", "not measured", "Designated tent site plus a flat spot",
     "Deep in the woods above a ravine, drop-off at the edge",
     "The only pair straddles what looks like a deer trail - he'd not risk it.",
     "I wouldn't mess with that you end up with deer inside your tarp"),
    ("2", 1, "Poor", "maybe 1", "not measured", "One large tent pad", "Across from site 0",
     "",
     "as far as hammocking goes it doesn't look very promising maybe one over yonder"),
    ("12", 1, "Poor", "workable but bad", "~15-16 (too long) or ~10 (tarp won't fit)",
     "Flat, flat, flat - big tent capacity", "Heavy deer sign; featured in his other videos",
     "His usual pair here is 15-16 ft; the alternative is only ~10 ft, too short for his tarp.",
     "this is a tent site for sure"),
    ("5", 1, "Poor", "0-1", "not measured", "One pad, open space, edge of a drop-off",
     "Across a ravine from 3; a real hike in",
     "Poplar stand, but the trees are mostly up the hill off-site.",
     "if you're gonna be hammocking this is one I probably wouldn't go to"),
    ("10", 0, "Avoid for hanging", "0", "-", "Tilted - the first non-flat site he saw",
     "Closest to water, wood and the privy",
     "Fine enough for a tent or two.",
     "I wouldn't recommend hanging any hammocks in here definitely not"),
    ("14", 0, "Avoid", "0", "-", "Slanted; the area around the table turns to mud",
     "Right off the path, site 23 visible from it",
     "The one site he'd actively avoid - bad for tents too.",
     "out of all the campsites I'd say 14 is one that I would try to avoid"),
    ("16", 0, "Avoid for hanging", "0", "-", "Space for a few tents",
     "Best privacy in the park - a ring of trees and shrubbery",
     "Tent-only, but the nicest privacy screen he found.",
     "you got space for a few tents here and no hammocks this is definitely a tent only site"),
    ("23", 0, "Avoid for hanging", "0", "-", "Decently flat, slight slant", "Open field, no shade",
     "Pure field site.",
     "there are no hammock sites whatsoever this is a field campsite for sure"),
    ("24", 0, "Avoid for hanging", "0", "-", "Flat, slight downhill", "Smaller site for smaller groups",
     "Fits two tents.",
     "as far as hammocks go I would not bother"),
    ("0", None, "Not assessed", "", "", "No tent pads", "Very quick exit back to the trail",
     "He noted only the fire ring and picnic table; no hammock read given.",
     "campsite 0 has no tent pads just a nice happy place for you to set up"),
    ("9", None, "Not assessed", "", "", "Tent pad next to the fire ring",
     "Prairie, grass and flowers in spring; deer everywhere",
     "Oversized old fire scars eat into the usable space. No hammock read given.",
     "some big fires that people had that don't quite allow you to camp where you think you should"),
    ("19", None, "Not assessed", "", "", "Two tent pads on two levels", "River view like 18; on a cliff edge",
     "He flags it as a poor choice with small children. No hammock read given.",
     "just like 18 is on the edge of a cliff"),
]

MARIA = [
    ("B2", 5, "Best in park", "many", "your pick", "Flat throughout",
     "On a peninsula; little trails down to the lake",
     "He has hung here before. Trailhead lot for B1-B3 holds only 5-6 cars. Watch where you pitch relative to the central fire ring and the wind.",
     "you could hang a hammock just about anywhere ... there's just so many spots"),
    ("B11", 5, "Star site", "4-5", "not measured", "Flat, flat, flat; drains fast",
     "End of the line - secluded and big; no lake view",
     "Largest site he saw. Don't take the hang that crosses the latrine path. One rock at the entrance to avoid.",
     "I'd say B11 is your star campsite so far"),
    ("B13", 5, "Excellent", "3", "needs slightly larger straps", "Flat, little leaf litter, can get muddy",
     "Wooded, no lake view",
     "Three spans called out one after another. No widow-makers overhead.",
     "an A for hammocks just bring slightly larger straps"),
    ("B6", 4, "Good", "2-3", "one pair under 10 ft - reach for a farther tree",
     "Back end noticeably slanted; flat near the fire ring", "Right on the pond (turtles); its own privy",
     "Options both inside and outside the site, but don't hang across the walking/deer trail.",
     "you could hang two or three in here"),
    ("B4", 4, "Good", "2-3", "not measured", "Large, slightly slanted; muddy low area, high and dry up top",
     "Off the beaten path over a little bridge; swamp on both sides",
     "Rivals B11 for size. Bring bug spray.",
     "we got one we got two and we've got maybe a third spot if you want to sleep over a stump"),
    ("B9", 3, "Decent", "1-2", "not measured", "Cozy but good; two tent spots", "Privy shared with B10, uphill",
     "",
     "good for hammocks good for tents"),
    ("B1", 3, "Decent (seen from afar)", "some", "not measured", "Up on a hill, some slanted ground",
     "Occupied when he filmed - assessed at a distance",
     "He rates it green for hammocks and room for 4 tents, but never walked it.",
     "definitely some trees in there for hammocking"),
    ("G2 Oak Hill (group)", 3, "Moderate", "a few", "thick trunks - big straps",
     "More slanted than Whitetail near the lot; very flat spots farther in",
     "Group site overlooking a pond; ~2.5 fire rings",
     "Big enough that even modest tree density yields several hangs. He guesses ~20 people fit.",
     "based on the trees though modestly hammock friendly even for a big site"),
    ("B16", 2, "Marginal", "1-2", "not measured", "Nice tent pad plus a second flat area",
     "Non-reservable; near Sloth/Slog Lake with a good view out",
     "Young and old growth with nothing in between. Oddly, every tree in the site leans.",
     "potential hammocking there definite hammocking over there"),
    ("B12", 2, "Marginal", "1-2", "~10 (tight), ~12, or ~16 to the big tree",
     "Very flat, one small rock and a dip", "Wooded",
     "All three options need long straps.",
     "you got options but you need big straps"),
    ("B15", 1, "Poor", "1 (a stretch)", "long - he barely made it work", "Flat, flat, flat",
     "Overlooks Maria Lake (Bjorkland on the map); shares a privy with B14",
     "He and his wife stayed here; the single hang he found was a real reach. Took 4 inches of rain that night.",
     "the only place that I could find a hammock was from here to there and it was a stretch"),
    ("B10", 1, "Poor", "1", "not measured", "Slanted across the site; flat by the food box",
     "Uphill climb in; privy shared with B9",
     "The one hang option risks blocking the latrine path.",
     "not the best for hammocking pretty good for tenting"),
    ("B17", 1, "Poor", "maybe 1, tricky", "not measured", "Decently flat, good tent space",
     "Most secluded of the near sites; lake off in the distance; swamp with frogs behind",
     "Woodpecker damage and a clear widow-maker he'd not camp under. Don't hang over the latrine trail.",
     "you might be able to finagle one in here but it's probably going to be tricky"),
    ("B5", 1, "Poor", "maybe 1", "small hammock only, big tree to little tree",
     "Level in spots; slanted and lumpy near the ring", "Very easy walk in; water and privy close",
     "The other option means hanging toward the privy - he says don't.",
     "overall this is a very tent friendly site not very friendly for hammocks"),
    ("B3", 0, "Avoid for hanging", "0", "trees too far apart", "Slanted on a hill",
     "By the camper cabin and water",
     "The site that taught him to check tree spacing - trunks are huge and too widely spaced.",
     "the trees are too far apart for hammocking and they're huge"),
    ("G1 Whitetail (group)", None, "Not assessed", "", "", "Lots of good flat space, upper and lower",
     "True group site overlooking a pond; own privy; 2 fire rings",
     "No hammock read given. The pad next to the privy is the short straw if the wind is wrong.",
     "more space than you can think of this is a true group campsite"),
    ("B14", None, "Not assessed (occupied)", "", "", "Up on a hill",
     "Overlooks Maria Lake; best view in the park",
     "First site to book every time. He'd reserve it first for tent camping. Trees look like the same old-growth/young-growth mix as B15.",
     "14 is one of the first campsites to book every time"),
    ("B8", None, "Not assessed (occupied)", "", "", "Flat",
     "Downhill walk in, west-facing view over Maria Lake; secluded",
     "Seen from a distance only; he guesses it is similar to B11.",
     "number eight is probably similar to 11 in a lot of ways"),
    ("B7", None, "Not assessed (occupied)", "", "", "On a hill - won't flood",
     "The most secluded site in the park; completely surrounded by grass",
     "Bring bug spray. Horses share the trail in from May 1 to Nov 1 - watch your step.",
     "it doesn't get any more secluded and private than that"),
]

HEADERS = ["Site", "Score (0-5)", "Verdict", "Hangs", "Tree spans (ft)", "Ground / tent notes",
           "Setting", "Cautions & extras", "What he said (auto-caption, verbatim)"]
WIDTHS = [20, 11, 22, 14, 30, 30, 38, 46, 52]

HEAD_FILL = PatternFill("solid", fgColor="1F3B2C")
BAND = PatternFill("solid", fgColor="F2F5F2")
SCORE_FILL = {5: "63BE7B", 4: "A9D08E", 3: "FFE699", 2: "FFD9A0", 1: "F4B183", 0: "E6A0A0"}
THIN = Side(style="thin", color="C8D0C8")
BORDER = Border(bottom=THIN)


def build_sheet(wb, title, rows, subtitle):
    ws = wb.create_sheet(title)
    ws["A1"] = title
    ws["A1"].font = Font(name="Arial", size=14, bold=True, color="1F3B2C")
    ws["A2"] = subtitle
    ws["A2"].font = Font(name="Arial", size=9, italic=True, color="606060")

    hdr = 4
    for c, h in enumerate(HEADERS, 1):
        cell = ws.cell(hdr, c, h)
        cell.font = Font(name="Arial", size=10, bold=True, color="FFFFFF")
        cell.fill = HEAD_FILL
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    ws.row_dimensions[hdr].height = 30

    for i, row in enumerate(rows):
        r = hdr + 1 + i
        for c, val in enumerate(row, 1):
            cell = ws.cell(r, c, val if val != "" else None)
            cell.font = Font(name="Arial", size=10)
            cell.alignment = Alignment(vertical="top", wrap_text=(c >= 5))
            cell.border = BORDER
            if i % 2:
                cell.fill = BAND
        sc = row[1]
        c2 = ws.cell(r, 2)
        c2.alignment = Alignment(horizontal="center", vertical="top")
        if sc in SCORE_FILL:
            c2.fill = PatternFill("solid", fgColor=SCORE_FILL[sc])
            c2.font = Font(name="Arial", size=10, bold=True)
        ws.cell(r, 9).font = Font(name="Arial", size=9, italic=True, color="4A4A4A")
        ws.row_dimensions[r].height = 42

    last = hdr + len(rows)
    for c, w in enumerate(WIDTHS, 1):
        ws.column_dimensions[get_column_letter(c)].width = w
    ws.auto_filter.ref = "A%d:I%d" % (hdr, last)
    ws.freeze_panes = "B%d" % (hdr + 1)

    note = ws.cell(last + 2, 1,
                   "Rows are ordered best-to-worst for hammock hanging. Quotes come from YouTube auto-captions, "
                   "so wording is approximate. A blank score means the site was occupied or he gave no hammock read on camera.")
    note.font = Font(name="Arial", size=9, italic=True, color="606060")
    return ws, hdr, last


wb = openpyxl.Workbook()
wb.remove(wb.active)

sum_ws = wb.create_sheet("Summary")
a_ws, a_h, a_last = build_sheet(
    wb, "Afton", AFTON,
    'Source: MN Hiker, "Afton State Park - A Look at all 27 Backpacking Sites" (youtu.be/-Zt33CT61XA)')
m_ws, m_h, m_last = build_sheet(
    wb, "Lake Maria", MARIA,
    'Source: MN Hiker, "Lake Maria State Park - A Look at All 19 Backpacking Sites" (youtu.be/b6r5FnQruMg)')

s = sum_ws
s["A1"] = "Best Hammock Spots - Afton & Lake Maria State Parks (MN)"
s["A1"].font = Font(name="Arial", size=15, bold=True, color="1F3B2C")
s["A2"] = ("Built from two MN Hiker campsite walkthroughs. His working benchmark: a usable span is roughly 12-16 feet "
           "between trees, and he says a 10-foot gap is too tight for his tarp. Several \"marginal\" sites move up if you carry long straps.")
s["A2"].font = Font(name="Arial", size=10, italic=True, color="505050")
s.merge_cells("A2:F2")
s.row_dimensions[2].height = 30
s["A2"].alignment = Alignment(wrap_text=True, vertical="top")

s["A4"] = "Score legend"
s["A4"].font = Font(name="Arial", size=11, bold=True)
legend = [(5, "Best - hang almost anywhere, or 3+ good spans"),
          (4, "Good - 2-3 usable hangs"),
          (3, "Decent - 1-2 usable hangs"),
          (2, "Marginal - one span, or needs long straps"),
          (1, "Poor - one tricky or stretched option at best"),
          (0, "None - he says don't bother hanging here")]
for i, (sc, txt) in enumerate(legend):
    r = 5 + i
    c = s.cell(r, 1, sc)
    c.fill = PatternFill("solid", fgColor=SCORE_FILL[sc])
    c.font = Font(name="Arial", size=10, bold=True)
    c.alignment = Alignment(horizontal="center")
    s.cell(r, 2, txt).font = Font(name="Arial", size=10)
s.cell(11, 1, "(blank)").font = Font(name="Arial", size=10, bold=True)
s.cell(11, 2, "Site was occupied, or he gave no hammock read on camera").font = Font(name="Arial", size=10)

s["A13"] = "Site counts by score"
s["A13"].font = Font(name="Arial", size=11, bold=True)
for c, h in enumerate(["Score", "Afton", "Lake Maria", "Both"], 1):
    cell = s.cell(14, c, h)
    cell.font = Font(name="Arial", size=10, bold=True, color="FFFFFF")
    cell.fill = HEAD_FILL
    cell.alignment = Alignment(horizontal="center")
for i, sc in enumerate([5, 4, 3, 2, 1, 0]):
    r = 15 + i
    c = s.cell(r, 1, sc)
    c.fill = PatternFill("solid", fgColor=SCORE_FILL[sc])
    c.font = Font(name="Arial", size=10, bold=True)
    c.alignment = Alignment(horizontal="center")
    s.cell(r, 2, "=COUNTIF(Afton!$B$%d:$B$%d,$A%d)" % (a_h + 1, a_last, r))
    s.cell(r, 3, "=COUNTIF('Lake Maria'!$B$%d:$B$%d,$A%d)" % (m_h + 1, m_last, r))
    s.cell(r, 4, "=B%d+C%d" % (r, r))
s.cell(21, 1, "Scored").font = Font(name="Arial", size=10, bold=True)
s.cell(21, 2, "=COUNT(Afton!$B$%d:$B$%d)" % (a_h + 1, a_last))
s.cell(21, 3, "=COUNT('Lake Maria'!$B$%d:$B$%d)" % (m_h + 1, m_last))
s.cell(21, 4, "=B21+C21")
s.cell(22, 1, "Sites listed").font = Font(name="Arial", size=10, bold=True)
s.cell(22, 2, "=COUNTA(Afton!$A$%d:$A$%d)" % (a_h + 1, a_last))
s.cell(22, 3, "=COUNTA('Lake Maria'!$A$%d:$A$%d)" % (m_h + 1, m_last))
s.cell(22, 4, "=B22+C22")
for rr in range(15, 23):
    for cc in (2, 3, 4):
        s.cell(rr, cc).font = Font(name="Arial", size=10)
        s.cell(rr, cc).alignment = Alignment(horizontal="center")

s["A24"] = "Top picks"
s["A24"].font = Font(name="Arial", size=11, bold=True)
picks = [
    ("Afton", "Site 25", "The one he calls the best by far: three-plus spans (11-13 ft plus a ~15 ft), flat tent room, an open prairie beside it, and almost no passing traffic."),
    ("Afton", "Site 3", "Densest timber in the park - plenty of spots, two tent pads, deep in the woods."),
    ("Afton", "Site 6", "Two hangs, three if you're lucky, and the privy is right there."),
    ("Lake Maria", "B2", "Hang anywhere: flat ground on a peninsula with little trails down to the lake. Trailhead lot holds only 5-6 cars."),
    ("Lake Maria", "B11", "Four to five hang spots on the biggest, flattest, best-draining site - but no lake view."),
    ("Lake Maria", "B13", "Graded an A for hammocks with three called-out spans; bring slightly longer straps."),
]
for c, h in enumerate(["Park", "Site", "Why"], 1):
    cell = s.cell(25, c, h)
    cell.font = Font(name="Arial", size=10, bold=True, color="FFFFFF")
    cell.fill = HEAD_FILL
for i, row in enumerate(picks):
    r = 26 + i
    for c, val in enumerate(row, 1):
        cell = s.cell(r, c, val)
        cell.font = Font(name="Arial", size=10, bold=(c == 2))
        cell.alignment = Alignment(vertical="top", wrap_text=(c == 3))
    s.row_dimensions[r].height = 32

s["A33"] = ("Sources: transcripts pulled 2026-08-30 from youtu.be/-Zt33CT61XA and youtu.be/b6r5FnQruMg (MN Hiker). "
            "Every rating reflects what the narrator said on camera - none of these are sites verified in person. "
            "Downed trees, conditions and park rules change, so check current MN DNR reservation info before booking.")
s["A33"].font = Font(name="Arial", size=9, italic=True, color="606060")
s.merge_cells("A33:F34")
s["A33"].alignment = Alignment(wrap_text=True, vertical="top")

for col, w in zip("ABCDEF", [16, 16, 74, 12, 12, 12]):
    s.column_dimensions[col].width = w
s.sheet_view.showGridLines = False

wb.calculation.fullCalcOnLoad = True
wb.save(OUT)
print("wrote", OUT)
