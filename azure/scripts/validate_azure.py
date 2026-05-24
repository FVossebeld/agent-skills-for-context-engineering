#!/usr/bin/env python3
"""Validate the Azure companion distribution.

This validator is intentionally separate from researcher/scripts/validate_repo.py.
The core validator owns the platform-agnostic corpus under ../skills; this script
guards the additive Azure source root without adding Azure skills to core fixtures.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
REQUIRED_SECTIONS = [
    "## When to Activate",
    "## Core Concepts",
    "## Practical Guidance",
    "## Examples",
    "## Guidelines",
    "## Gotchas",
    "## Integration",
    "## References",
]


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing opening frontmatter delimiter")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("missing closing frontmatter delimiter")
    data: dict[str, str] = {}
    for raw in text[4:end].splitlines():
        if not raw.strip() or raw.startswith(" "):
            continue
        if ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def main() -> int:
    findings: list[str] = []
    skill_names: list[str] = []

    for skill_dir in sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir()):
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            findings.append(f"{skill_file}: missing SKILL.md")
            continue

        text = skill_file.read_text(encoding="utf-8")
        lines = text.splitlines()
        try:
            frontmatter = parse_frontmatter(text)
        except ValueError as exc:
            findings.append(f"{skill_file}: {exc}")
            continue

        name = frontmatter.get("name", "")
        description = frontmatter.get("description", "")
        skill_names.append(skill_dir.name)

        if name != skill_dir.name:
            findings.append(f"{skill_file}: frontmatter name does not match directory")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            findings.append(f"{skill_file}: name must be lowercase kebab-case")
        if not description:
            findings.append(f"{skill_file}: missing description")
        if len(lines) > 500:
            findings.append(f"{skill_file}: exceeds 500 lines")
        for section in REQUIRED_SECTIONS:
            if section not in text:
                findings.append(f"{skill_file}: missing required section {section}")
        if "Do not activate" not in text:
            findings.append(f"{skill_file}: missing non-activation boundary")

    corpus = json.loads((ROOT / "corpus" / "index.json").read_text(encoding="utf-8"))
    corpus_names = sorted(item["name"] for item in corpus["skills"])
    if corpus_names != sorted(skill_names):
        findings.append(f"corpus/index.json skill names differ: corpus={corpus_names} skills={sorted(skill_names)}")

    manifest = json.loads((ROOT / ".plugin" / "plugin.json").read_text(encoding="utf-8"))
    plugin = manifest["plugins"][0]
    if plugin.get("source") != "./azure":
        findings.append("azure/.plugin/plugin.json must keep source './azure'")
    manifest_names = sorted(Path(path).name for path in plugin["skills"])
    if manifest_names != sorted(skill_names):
        findings.append(f"plugin skills differ: manifest={manifest_names} skills={sorted(skill_names)}")

    if findings:
        print(json.dumps({"ok": False, "findings": findings}, indent=2))
        return 1

    print(json.dumps({"ok": True, "skill_count": len(skill_names)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

