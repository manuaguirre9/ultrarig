#!/usr/bin/env python3
"""
UltraRig Documentation Integrity Linter

Validates all local Markdown links, relative file references, and code block formatting
across the repository to ensure documentation consistency.

Usage:
    python scripts/lint_docs.py
"""

import os
import sys
import re
from pathlib import Path


def find_markdown_files(root_dir: Path) -> list:
    """Find all markdown files, ignoring .git, system generated, and build folders."""
    ignore_dirs = {".git", ".system_generated", "scratch", "node_modules", ".github"}
    md_files = []
    for path in root_dir.rglob("*.md"):
        parts = set(path.parts)
        if not parts.intersection(ignore_dirs):
            md_files.append(path)
    return sorted(md_files)


def validate_file(file_path: Path, root_dir: Path) -> tuple:
    """Validate relative links and code blocks in a markdown file."""
    issues = []
    link_count = 0

    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        return [f"Could not read file: {e}"], 0

    # 1. Check code block balance
    code_block_markers = re.findall(r"^```", content, re.MULTILINE)
    if len(code_block_markers) % 2 != 0:
        issues.append("Unbalanced code block markers (odd number of ``` fences)")

    # 2. Extract links: [text](link)
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    for match in link_pattern.finditer(content):
        link_count += 1
        link_target = match.group(2).strip()

        # Skip web links, email links, and purely in-page anchors
        if re.match(r'^(https?://|mailto:|#)', link_target):
            continue

        # Skip GitHub-specific relative routing (e.g. ../../releases/latest or ../../issues)
        if link_target.startswith("../../releases") or link_target.startswith("../../issues"):
            continue

        # Strip anchor if present: path/to/file.md#section -> path/to/file.md
        clean_target = link_target.split("#")[0]
        if not clean_target:
            continue

        # Resolve path relative to current file's directory
        resolved_path = (file_path.parent / clean_target).resolve()

        if not resolved_path.exists():
            issues.append(f"Broken relative link: '{link_target}' (resolved to non-existent: {resolved_path.name})")

    return issues, link_count


def main():
    root_dir = Path(__file__).resolve().parent.parent
    print(f"Linting documentation in repository: {root_dir}")

    md_files = find_markdown_files(root_dir)
    total_links = 0
    total_issues = 0
    file_issue_map = {}

    for md_file in md_files:
        rel_path = md_file.relative_to(root_dir)
        issues, count = validate_file(md_file, root_dir)
        total_links += count
        if issues:
            file_issue_map[str(rel_path)] = issues
            total_issues += len(issues)

    print("\n" + "=" * 60)
    print(f"Documentation Lint Summary:")
    print(f"  Files inspected:  {len(md_files)}")
    print(f"  Links validated:  {total_links}")
    print(f"  Issues detected:  {total_issues}")
    print("=" * 60 + "\n")

    if total_issues > 0:
        print("❌ Issues found in documentation:")
        for filename, issues in file_issue_map.items():
            print(f"\n📄 {filename}:")
            for issue in issues:
                print(f"   - {issue}")
        sys.exit(1)
    else:
        print("✅ All markdown files, relative links, and formatting checks passed successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
