#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "ba-zero-to-office-tutor"
REF_DIR = SKILL_DIR / "references"
CHATGPT_DIR = ROOT / "chatgpt"
DIST = ROOT / "dist"

REFERENCE_ORDER = [
    "curriculum.md",
    "teaching-protocol.md",
    "cognitive-load.md",
    "assessment-rubric.md",
    "learner-state.md",
    "office-case-bank.md",
    "technical-mental-maps.md",
]


def require(path: Path) -> None:
    if not path.exists():
        raise SystemExit(f"Missing required file: {path.relative_to(ROOT)}")


def build_chatgpt_knowledge() -> Path:
    out = CHATGPT_DIR / "KNOWLEDGE-BA-TUTOR.md"
    chunks = [
        "# BA Zero-to-Office Tutor — Knowledge Bundle\n",
        "This file is generated from the canonical skill references. Behavior rules belong in GPT-INSTRUCTIONS.md; this file provides curriculum/reference knowledge.\n",
    ]
    for name in REFERENCE_ORDER:
        path = REF_DIR / name
        require(path)
        chunks.append(f"\n---\n\n<!-- SOURCE: skills/ba-zero-to-office-tutor/references/{name} -->\n\n")
        chunks.append(path.read_text(encoding="utf-8").rstrip() + "\n")
    out.write_text("".join(chunks), encoding="utf-8")
    return out


def zip_tree(source: Path, output: Path, top_level: str | None = None) -> None:
    if output.exists():
        output.unlink()
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in sorted(source.rglob("*")):
            if path.is_dir():
                continue
            rel = path.relative_to(source)
            arc = Path(top_level) / rel if top_level else rel
            zf.write(path, arc.as_posix())


def build_claude_zip() -> Path:
    out = DIST / "ba-zero-to-office-tutor-claude.zip"
    zip_tree(SKILL_DIR, out, "ba-zero-to-office-tutor")
    return out


def build_repository_zip() -> Path:
    out = DIST / "ba-zero-to-office-tutor-repository.zip"
    if out.exists():
        out.unlink()
    excluded_roots = {".git", "dist", "__pycache__"}
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in sorted(ROOT.rglob("*")):
            if path.is_dir():
                continue
            rel = path.relative_to(ROOT)
            if rel.parts and rel.parts[0] in excluded_roots:
                continue
            if "__pycache__" in rel.parts:
                continue
            zf.write(path, (Path("ba-zero-to-office-tutor") / rel).as_posix())
    return out


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    DIST.mkdir(exist_ok=True)
    require(SKILL_DIR / "SKILL.md")
    require(CHATGPT_DIR / "GPT-INSTRUCTIONS.md")
    knowledge = build_chatgpt_knowledge()
    claude_zip = build_claude_zip()
    repo_zip = build_repository_zip()

    outputs = [knowledge, claude_zip, repo_zip]
    sums = DIST / "SHA256SUMS.txt"
    lines = []
    for path in outputs:
        lines.append(f"{sha256(path)}  {path.relative_to(ROOT).as_posix()}")
    sums.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("Built:")
    for path in outputs + [sums]:
        print(f"- {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
