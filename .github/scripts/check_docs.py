#!/usr/bin/env python3
"""Basic docs checks: SVGs parse as XML, relative Markdown links and
in-page anchors resolve, and no old project names remain."""
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OLD_NAMES = re.compile(r"cog[ _-]?os|brainos", re.IGNORECASE)
LINK = re.compile(r"\]\(([^)\s]+)\)")
SKIP = {".git", ".github"}
errors = []


def files(pattern):
    return [p for p in ROOT.rglob(pattern)
            if p.is_file() and not SKIP & set(p.relative_to(ROOT).parts)]


def slug(heading):
    text = re.sub(r"[^\w\- ]", "", heading.strip().lower())
    return text.replace(" ", "-")


def anchors(md):
    found = set()
    for line in md.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^#{1,6}\s+(.*)$", line)
        if m:
            found.add(slug(m.group(1)))
    return found


for svg in files("*.svg"):
    try:
        ET.parse(svg)
    except ET.ParseError as exc:
        errors.append(f"{svg.relative_to(ROOT)}: invalid SVG ({exc})")

for md in files("*.md"):
    for target in LINK.findall(md.read_text(encoding="utf-8")):
        if re.match(r"^[a-z]+:", target):
            continue
        path, _, frag = target.partition("#")
        dest = (md.parent / path).resolve() if path else md
        if not dest.exists():
            errors.append(f"{md.relative_to(ROOT)}: broken link {target}")
        elif frag and dest.suffix == ".md" and frag.lower() not in anchors(dest):
            errors.append(f"{md.relative_to(ROOT)}: missing anchor {target}")

for f in files("*"):
    text = f.read_text(encoding="utf-8", errors="ignore")
    for n, line in enumerate(text.splitlines(), 1):
        if OLD_NAMES.search(line):
            errors.append(f"{f.relative_to(ROOT)}:{n}: old project name")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("docs check passed")
