#!/usr/bin/env python3
"""Split monthly diary Markdown files into Hugo page bundles."""

from __future__ import annotations

import argparse
import calendar
import hashlib
import json
import re
import shutil
import sys
import tempfile
from dataclasses import dataclass
from datetime import date
from pathlib import Path

FORMAT_VERSION = 3
MONTH_FILE_RE = re.compile(r"d(?P<year>\d{4})(?P<month>\d{2})\.md$")
MONTH_TITLE_RE = re.compile(r"^#\s+(?P<year>\d{4})年(?P<month>\d{1,2})月\s*$")
DAY_TITLE_RE = re.compile(
    r"^##\s+(?P<month>\d{1,2})月(?P<day>\d{1,2})日\((?P<weekday>[^()]+)\)\s*$"
)
HEADING2_RE = re.compile(r"^##(?:\s|$)")
FENCE_RE = re.compile(r"^ {0,3}(?P<marker>`{3,}|~{3,})")
LINK_RE = re.compile(r"(?P<prefix>!?(?:\[[^\]]*\])\()(?P<target>[^)\s]+)(?P<suffix>(?:\s+[^)]*)?\))")
WEEKDAYS = "月火水木金土日"


class DiaryError(ValueError):
    pass


@dataclass(frozen=True)
class Entry:
    day: date
    weekday: str
    body: str


def _fence_marker(line: str) -> tuple[str, int] | None:
    match = FENCE_RE.match(line)
    if not match:
        return None
    marker = match.group("marker")
    return marker[0], len(marker)


def parse_month(path: Path) -> tuple[int, int, list[Entry], list[str]]:
    match = MONTH_FILE_RE.fullmatch(path.name)
    if not match:
        raise DiaryError(f"{path}: filename must match dYYYYMM.md")
    year = int(match.group("year"))
    month = int(match.group("month"))
    lines = path.read_text(encoding="utf-8-sig").splitlines(keepends=True)
    if not lines:
        raise DiaryError(f"{path}: empty file")
    title = MONTH_TITLE_RE.fullmatch(lines[0].rstrip("\r\n"))
    if not title or (int(title.group("year")), int(title.group("month"))) != (year, month):
        raise DiaryError(f"{path}:1: month title does not match filename")

    chunks: list[tuple[date, str, list[str], int]] = []
    current: tuple[date, str, list[str], int] | None = None
    fence: tuple[str, int] | None = None
    warnings: list[str] = []

    for lineno, line in enumerate(lines[1:], start=2):
        marker = _fence_marker(line)
        if marker:
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and marker[1] >= fence[1]:
                fence = None
        if fence is not None:
            if current:
                current[2].append(line)
            continue

        raw = line.rstrip("\r\n")
        day_match = DAY_TITLE_RE.fullmatch(raw)
        if day_match:
            if current:
                chunks.append(current)
            heading_month = int(day_match.group("month"))
            day_number = int(day_match.group("day"))
            if heading_month != month:
                raise DiaryError(f"{path}:{lineno}: date is outside source month")
            try:
                parsed_day = date(year, month, day_number)
            except ValueError as error:
                raise DiaryError(f"{path}:{lineno}: {error}") from error
            weekday = day_match.group("weekday")
            expected = WEEKDAYS[parsed_day.weekday()]
            if weekday != expected:
                warnings.append(
                    f"{path}:{lineno}: weekday is {weekday}, calendar says {expected}"
                )
            current = (parsed_day, weekday, [], lineno)
        elif HEADING2_RE.match(raw):
            raise DiaryError(f"{path}:{lineno}: level-2 heading is not a diary date")
        elif current:
            current[2].append(line)

    if fence is not None:
        raise DiaryError(f"{path}: unclosed Markdown fence")
    if current:
        chunks.append(current)
    if not chunks:
        raise DiaryError(f"{path}: no diary entries")

    merged: dict[date, tuple[str, list[str], int]] = {}
    order: list[date] = []
    for parsed_day, weekday, body, lineno in chunks:
        if parsed_day not in merged:
            merged[parsed_day] = (weekday, body, lineno)
            order.append(parsed_day)
        else:
            warnings.append(f"{path}:{lineno}: duplicate date merged: {parsed_day.isoformat()}")
            old_weekday, old_body, old_line = merged[parsed_day]
            if old_body and body and old_body[-1].strip() and body[0].strip():
                old_body.append("\n")
            old_body.extend(body)
            merged[parsed_day] = (old_weekday, old_body, old_line)

    entries = [
        Entry(parsed_day, merged[parsed_day][0], "".join(merged[parsed_day][1]).strip() + "\n")
        for parsed_day in order
    ]
    return year, month, entries, warnings


def rewrite_target(target: str) -> str:
    image = re.fullmatch(r"images/(.+)", target)
    if image:
        return f"/log/images/{image.group(1)}"
    month_link = re.fullmatch(r"d(\d{4})(\d{2})\.md(?:#(\d{1,2}))?", target)
    if month_link:
        year, month, day = month_link.groups()
        if day:
            return f"/log/{year}/{month}/{int(day):02d}/"
        return f"/log/{year}/{month}/"
    if target in {"index.md", "../README.md"}:
        return "/log/"
    return target


def rewrite_links(markdown: str) -> str:
    output: list[str] = []
    fence: tuple[str, int] | None = None
    for line in markdown.splitlines(keepends=True):
        marker = _fence_marker(line)
        if marker:
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and marker[1] >= fence[1]:
                fence = None
            output.append(line)
            continue
        if fence is None:
            line = LINK_RE.sub(
                lambda match: match.group("prefix")
                + rewrite_target(match.group("target"))
                + match.group("suffix"),
                line,
            )
        output.append(line)
    return "".join(output)


def render_entry(entry: Entry, source_name: str) -> str:
    day = entry.day
    return (
        "---\n"
        f'title: "{day.year}年{day.month}月{day.day}日"\n'
        f"date: {day.isoformat()}T00:00:00+09:00\n"
        f"lastmod: {day.isoformat()}T00:00:00+09:00\n"
        "type: diary\n"
        f'source_month: "{source_name}"\n'
        "generated: true\n"
        "---\n\n"
        "<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->\n\n"
        + rewrite_links(entry.body)
    )


def render_month_index(year: int, month: int) -> str:
    return (
        "---\n"
        f'title: "{year}年{month}月"\n'
        f"date: {year:04d}-{month:02d}-01T00:00:00+09:00\n"
        f'url: "/{year:04d}/{month:02d}/"\n'
        "type: archive\n"
        "layout: month\n"
        "aliases:\n"
        f'  - "/d{year:04d}{month:02d}.html"\n'
        "generated: true\n"
        "---\n"
    )


def render_year_index(year: int) -> str:
    return (
        "---\n"
        f'title: "{year}年"\n'
        f'url: "/{year:04d}/"\n'
        "type: archive\n"
        "layout: year\n"
        "generated: true\n"
        "---\n"
    )


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_if_changed(path: Path, content: str) -> bool:
    encoded = content.encode("utf-8")
    if path.exists() and path.read_bytes() == encoded:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    temporary.write_bytes(encoded)
    temporary.replace(path)
    return True


def load_manifest(path: Path) -> dict:
    if not path.exists():
        return {"format_version": FORMAT_VERSION, "months": {}}
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as error:
        raise DiaryError(f"{path}: invalid manifest: {error}") from error
    return manifest


def build_month(source: Path, content_root: Path) -> tuple[dict[str, str], list[str]]:
    year, month, entries, warnings = parse_month(source)
    outputs: dict[str, str] = {"_index.md": render_month_index(year, month)}
    for entry in entries:
        outputs[f"{entry.day.day:02d}/index.md"] = render_entry(entry, source.name)
    month_dir = content_root / f"{year:04d}" / f"{month:02d}"
    with tempfile.TemporaryDirectory(prefix="split-diary-") as temporary:
        stage = Path(temporary)
        for relative, text in outputs.items():
            staged = stage / relative
            staged.parent.mkdir(parents=True, exist_ok=True)
            staged.write_text(text, encoding="utf-8")
        desired = set(outputs)
        if month_dir.exists():
            for existing in month_dir.rglob("*.md"):
                relative = existing.relative_to(month_dir).as_posix()
                if relative not in desired:
                    existing.unlink()
        for relative, text in outputs.items():
            write_if_changed(month_dir / relative, text)
        for directory in sorted(month_dir.glob("*"), reverse=True):
            if directory.is_dir() and not any(directory.iterdir()):
                directory.rmdir()
    return {key: hashlib.sha256(value.encode()).hexdigest() for key, value in outputs.items()}, warnings


def expected_month(source: Path) -> tuple[dict[str, str], list[str]]:
    year, month, entries, warnings = parse_month(source)
    outputs = {"_index.md": render_month_index(year, month)}
    outputs.update({f"{e.day.day:02d}/index.md": render_entry(e, source.name) for e in entries})
    return outputs, warnings


def run(root: Path, *, all_months: bool, check: bool, selected: str | None) -> int:
    source_root = root / "log"
    content_root = root / "content" / "diary"
    manifest_path = root / "data" / "split-manifest.json"
    manifest = load_manifest(manifest_path)
    sources = sorted(source_root.glob("d[0-9]" + "[0-9]" * 5 + ".md"))
    if selected:
        normalized = selected.replace("-", "")
        sources = [source_root / f"d{normalized}.md"]
        if not sources[0].exists():
            raise DiaryError(f"source month not found: {selected}")
    if not sources:
        raise DiaryError("no monthly source files found")

    failures: list[str] = []
    new_manifest = json.loads(json.dumps(manifest))
    new_manifest["format_version"] = FORMAT_VERSION
    new_manifest.setdefault("months", {})
    years: set[int] = set()

    for source in sources:
        file_match = MONTH_FILE_RE.fullmatch(source.name)
        assert file_match
        year = int(file_match.group("year"))
        month = int(file_match.group("month"))
        years.add(year)
        key = f"{year:04d}-{month:02d}"
        source_hash = digest(source)
        record = manifest.get("months", {}).get(key, {})
        unchanged = (
            not all_months
            and manifest.get("format_version") == FORMAT_VERSION
            and record.get("source_sha256") == source_hash
        )
        if check:
            outputs, warnings = expected_month(source)
            for warning in warnings:
                print(f"warning: {warning}", file=sys.stderr)
            month_dir = content_root / f"{year:04d}" / f"{month:02d}"
            actual = {
                item.relative_to(month_dir).as_posix()
                for item in month_dir.rglob("*.md")
            } if month_dir.exists() else set()
            if actual != set(outputs):
                failures.append(f"{key}: generated file list is stale")
            for relative, text in outputs.items():
                target = month_dir / relative
                if not target.exists() or target.read_text(encoding="utf-8") != text:
                    failures.append(f"{target}: generated content is stale")
            if record.get("source_sha256") != source_hash:
                failures.append(f"{key}: manifest is stale")
            continue
        if unchanged:
            continue
        output_hashes, warnings = build_month(source, content_root)
        for warning in warnings:
            print(f"warning: {warning}", file=sys.stderr)
        new_manifest["months"][key] = {
            "source": f"log/{source.name}",
            "source_sha256": source_hash,
            "outputs": output_hashes,
        }
        print(f"generated {key}: {len(output_hashes) - 1} entries")

    if check:
        for year_dir in content_root.glob("[0-9][0-9][0-9][0-9]"):
            expected = render_year_index(int(year_dir.name))
            target = year_dir / "_index.md"
            if not target.exists() or target.read_text(encoding="utf-8") != expected:
                failures.append(f"{target}: generated year index is stale")
        if failures:
            for failure in failures:
                print(f"error: {failure}", file=sys.stderr)
            return 1
        print("generated diary content is up to date")
        return 0

    all_years = {
        int(match.group("year"))
        for path in source_root.glob("d*.md")
        if (match := MONTH_FILE_RE.fullmatch(path.name))
    }
    for year in all_years:
        write_if_changed(content_root / f"{year:04d}" / "_index.md", render_year_index(year))
    write_if_changed(
        manifest_path,
        json.dumps(new_manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--all", action="store_true", help="regenerate every month")
    parser.add_argument("--check", action="store_true", help="verify generated files")
    parser.add_argument("--month", metavar="YYYY-MM", help="process only one month")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        return run(args.root.resolve(), all_months=args.all, check=args.check, selected=args.month)
    except DiaryError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
