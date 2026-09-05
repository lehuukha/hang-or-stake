# -*- coding: utf-8 -*-
"""Wrap the artifact-format source in a full HTML skeleton and stage it for GitHub Pages.

The artifact host adds doctype/head/meta at publish time; GitHub Pages serves the file
verbatim, so the Pages copy needs the wrapper (charset + viewport especially).
Run after editing hang_or_stake.html; then commit+push in hang-or-stake-repo.
"""
import pathlib, re

SP = pathlib.Path(__file__).resolve().parent  # repo/src; index.html is written to the repo root
src = (SP / "hang_or_stake.html").read_text(encoding="utf-8")

m = re.match(r"\s*<title>(.*?)</title>\s*", src, re.S)
title = m.group(1) if m else "Hang or Stake"
body = src[m.end():] if m else src

page = (
    "<!doctype html>\n<html lang=\"en\">\n<head>\n"
    "<meta charset=\"utf-8\">\n"
    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
    "<title>" + title + "</title>\n"
    "<meta name=\"description\" content=\"Hammock and tent campsite guide for overnight trips near the Twin Cities — every site scored for hanging and staking.\">\n"
    "<link rel=\"icon\" href=\"data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>\U0001F3D5</text></svg>\">\n"
    "</head>\n<body>\n" + body + "\n</body>\n</html>\n"
)
out = SP.parent / "index.html"
out.write_text(page, encoding="utf-8")
print("wrote", out, len(page), "chars | title:", title)
