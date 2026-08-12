# BA Zero-to-Office Tutor Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a portable, tested tutoring skill that turns the office BA learning targets into understanding-first, office-transfer learning.

**Architecture:** Keep the behavioral kernel in a compact `SKILL.md`; move curriculum, pedagogy, assessment, cognitive-load rules, and case banks into focused references. Generate a consolidated ChatGPT knowledge file and a Claude ZIP from the same source so the platforms do not drift.

**Tech Stack:** Markdown, YAML frontmatter, Python standard library, ZIP, Git.

## Global Constraints
- Do not diagnose ADHD or infer intelligence from slow processing.
- Understanding and transfer outrank memorized definitions.
- Reduce cognitive load without lowering professional standards.
- Teach technology categories and mental models before product-specific implementation.
- Preserve the 11 office learning targets as explicit curriculum coverage.
- ChatGPT installation documentation must not falsely claim GitHub-link self-installation.

---

### Task 1: Define behavior tests first
**Files:** Create `tests/behavior-scenarios.md`, `tests/test_repository.py`
- [ ] Write scenarios for rote recall, overload, multi-language scope, confusion recovery, urgent office requests, ambiguity coaching, and mastery evidence.
- [ ] Write repository structure/frontmatter/content assertions.
- [ ] Run tests and confirm expected failures because implementation files do not exist yet.

### Task 2: Implement skill behavioral kernel
**Files:** Create `skills/ba-zero-to-office-tutor/SKILL.md`
- [ ] Define triggers, modes, session protocol, mastery contract, pacing adaptation, BA depth boundary, and reference loading rules.
- [ ] Re-run repository tests.

### Task 3: Implement reference modules
**Files:** Create focused Markdown files under `skills/ba-zero-to-office-tutor/references/`.
- [ ] Curriculum and dependency graph.
- [ ] Teaching protocol and cognitive-load adaptation.
- [ ] Assessment rubric and learner-state schema.
- [ ] Office case bank and technical mental maps.
- [ ] Re-run repository tests.

### Task 4: Implement platform packaging
**Files:** Create `chatgpt/*`, `scripts/build.py`, `INSTALL.md`.
- [ ] Generate ChatGPT knowledge bundle from canonical references.
- [ ] Package Claude skill folder as ZIP.
- [ ] Document accurate ChatGPT and Claude installation paths.
- [ ] Re-run repository tests and build script.

### Task 5: Public repository documentation and verification
**Files:** Create `README.md`, `LICENSE`, `REFERENCES.md`, `examples/*`, `.gitignore`.
- [ ] Explain use, scope, learning philosophy, commands, and platform differences.
- [ ] Add acknowledgements and source references.
- [ ] Run final test/build/checksum verification.
- [ ] Commit locally on `build/initial-skill`.
