#!/usr/bin/env python3
"""Validate the skills repo: JSON parses, every SKILL.md has valid frontmatter,
skill name matches its folder, and every referenced reference file exists.

Stdlib only — no dependencies, so CI needs no install step.
Run locally: python3 scripts/validate_skills.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []


def err(msg):
    errors.append(msg)


def check_json(path: Path):
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        err(f"{path.relative_to(ROOT)}: invalid JSON — {e}")


def frontmatter(text: str):
    """Return the frontmatter block between the first two '---' lines, or None."""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    return m.group(1) if m else None


def check_skill(skill_md: Path):
    rel = skill_md.relative_to(ROOT)
    text = skill_md.read_text(encoding="utf-8")
    fm = frontmatter(text)
    if fm is None:
        err(f"{rel}: missing YAML frontmatter (must start with a '---' block)")
        return
    # required fields
    name_m = re.search(r"^name:\s*(\S+)", fm, re.MULTILINE)
    desc_m = re.search(r"^description:\s*", fm, re.MULTILINE)
    if not name_m:
        err(f"{rel}: frontmatter missing 'name:'")
    if not desc_m:
        err(f"{rel}: frontmatter missing 'description:'")
    # name must match folder
    if name_m:
        name = name_m.group(1)
        folder = skill_md.parent.name
        if name != folder:
            err(f"{rel}: name '{name}' does not match folder '{folder}'")
    # referenced reference files must exist
    for ref in re.findall(r"references/[A-Za-z0-9_-]+\.md", text):
        if not (skill_md.parent / ref).exists():
            err(f"{rel}: references '{ref}' but the file is missing")


def main():
    # 1. all JSON parses
    for p in ROOT.rglob(".claude-plugin/*.json"):
        check_json(p)
    for p in ROOT.rglob("*/evals/evals.json"):
        check_json(p)

    # 2. every skill validates
    skills = list(ROOT.rglob("*/skills/*/SKILL.md"))
    if not skills:
        err("no SKILL.md files found — expected */skills/*/SKILL.md")
    for s in skills:
        check_skill(s)

    if errors:
        print(f"✗ {len(errors)} problem(s):")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print(f"✓ validated {len(skills)} skill(s) + manifests — all good")


if __name__ == "__main__":
    main()
