#!/usr/bin/env python3
"""Validate the generated Hugo site without third-party dependencies."""

from __future__ import annotations

import argparse
import sys
import urllib.parse
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attribute = "src" if tag in {"img", "script"} else "href" if tag in {"a", "link"} else None
        if attribute:
            value = dict(attrs).get(attribute)
            if value:
                self.links.append(value)


def target_path(public: Path, url: str) -> Path | None:
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme or parsed.netloc or not parsed.path.startswith("/log/"):
        return None
    relative = urllib.parse.unquote(parsed.path.removeprefix("/log/")).lstrip("/")
    target = public / relative
    if parsed.path.endswith("/"):
        target /= "index.html"
    return target


def run(public: Path) -> int:
    errors: list[str] = []
    html_files = sorted(public.rglob("*.html"))
    if not html_files:
        errors.append(f"{public}: no HTML files found")
    for html_file in html_files:
        parser = LinkParser()
        try:
            parser.feed(html_file.read_text(encoding="utf-8"))
        except (OSError, UnicodeError) as error:
            errors.append(f"{html_file}: cannot parse: {error}")
            continue
        for link in parser.links:
            target = target_path(public, link)
            if target is not None and not target.exists():
                errors.append(f"{html_file}: broken internal link {link}")

    rss = public / "index.xml"
    try:
        root = ET.parse(rss).getroot()
        items = root.findall("./channel/item")
        if not items:
            errors.append(f"{rss}: RSS has no items")
    except (OSError, ET.ParseError) as error:
        errors.append(f"{rss}: invalid RSS: {error}")

    required = [
        public / "index.html",
        public / "index.xml",
        public / "2026/08/index.html",
        public / "2026/08/08/index.html",
        public / "d202608.html",
    ]
    for target in required:
        if not target.exists():
            errors.append(f"{target}: required output is missing")

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1
    print(f"site check passed: {len(html_files)} HTML files, {len(items)} RSS items")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("public", nargs="?", type=Path, default=Path("public"))
    args = parser.parse_args()
    return run(args.public.resolve())


if __name__ == "__main__":
    raise SystemExit(main())
