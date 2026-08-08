from __future__ import annotations

import importlib.util
import sys
import tempfile
import time
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).parents[1] / "scripts" / "split_diary.py"
SPEC = importlib.util.spec_from_file_location("split_diary", MODULE_PATH)
assert SPEC and SPEC.loader
split_diary = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = split_diary
SPEC.loader.exec_module(split_diary)


class SplitDiaryTest(unittest.TestCase):
    def write_month(self, root: Path, body: str, name: str = "d202402.md") -> Path:
        source = root / "log" / name
        source.parent.mkdir(parents=True, exist_ok=True)
        source.write_text(body, encoding="utf-8")
        return source

    def test_parses_content_and_ignores_heading_in_fence(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_month(
                Path(directory),
                "# 2024年2月\n\n## 2月29日(木)\n\n本文\n\n```text\n## TODO\n```\n",
            )
            year, month, entries, warnings = split_diary.parse_month(path)
            self.assertEqual((year, month), (2024, 2))
            self.assertEqual(entries[0].day.isoformat(), "2024-02-29")
            self.assertIn("## TODO", entries[0].body)
            self.assertEqual(warnings, [])

    def test_rejects_non_date_level_two_heading(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_month(
                Path(directory), "# 2024年2月\n\n## TODO\n\n## 2月1日(木)\n本文\n"
            )
            with self.assertRaises(split_diary.DiaryError):
                split_diary.parse_month(path)

    def test_rejects_invalid_date_and_wrong_month(self) -> None:
        for heading in ("## 2月30日(金)", "## 3月1日(金)"):
            with self.subTest(heading=heading), tempfile.TemporaryDirectory() as directory:
                path = self.write_month(Path(directory), f"# 2024年2月\n\n{heading}\n本文\n")
                with self.assertRaises(split_diary.DiaryError):
                    split_diary.parse_month(path)

    def test_merges_duplicate_dates_in_source_order(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = self.write_month(
                Path(directory),
                "# 2024年2月\n\n## 2月1日(木)\nfirst\n\n## 2月1日(木)\nsecond\n",
            )
            _, _, entries, warnings = split_diary.parse_month(path)
            self.assertEqual(len(entries), 1)
            self.assertLess(entries[0].body.index("first"), entries[0].body.index("second"))
            self.assertTrue(any("duplicate" in warning for warning in warnings))

    def test_rewrites_links_but_not_code(self) -> None:
        source = (
            "![image](images/example.png)\n"
            "[past](d202108.md#26)\n"
            "```md\n[past](d202108.md#26)\n```\n"
        )
        actual = split_diary.rewrite_links(source)
        self.assertIn("(/log/images/example.png)", actual)
        self.assertIn("(/log/2021/08/26/)", actual)
        self.assertIn("```md\n[past](d202108.md#26)\n```", actual)

    def test_incremental_generation_preserves_unchanged_mtime(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_month(root, "# 2024年2月\n\n## 2月1日(木)\n本文\n")
            self.assertEqual(split_diary.run(root, all_months=False, check=False, selected=None), 0)
            output = root / "content/diary/2024/02/01/index.md"
            first_mtime = output.stat().st_mtime_ns
            time.sleep(0.01)
            self.assertEqual(split_diary.run(root, all_months=False, check=False, selected=None), 0)
            self.assertEqual(output.stat().st_mtime_ns, first_mtime)

    def test_changed_month_removes_only_its_deleted_day(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            february = self.write_month(
                root,
                "# 2024年2月\n\n## 2月2日(金)\ntwo\n\n## 2月1日(木)\none\n",
            )
            self.write_month(root, "# 2024年3月\n\n## 3月1日(金)\nother\n", "d202403.md")
            split_diary.run(root, all_months=False, check=False, selected=None)
            other = root / "content/diary/2024/03/01/index.md"
            other_mtime = other.stat().st_mtime_ns
            february.write_text("# 2024年2月\n\n## 2月2日(金)\ntwo\n", encoding="utf-8")
            split_diary.run(root, all_months=False, check=False, selected=None)
            self.assertFalse((root / "content/diary/2024/02/01/index.md").exists())
            self.assertEqual(other.stat().st_mtime_ns, other_mtime)

    def test_check_detects_stale_output(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_month(root, "# 2024年2月\n\n## 2月1日(木)\n本文\n")
            split_diary.run(root, all_months=False, check=False, selected=None)
            output = root / "content/diary/2024/02/01/index.md"
            output.write_text("stale", encoding="utf-8")
            self.assertEqual(split_diary.run(root, all_months=False, check=True, selected=None), 1)


if __name__ == "__main__":
    unittest.main()
