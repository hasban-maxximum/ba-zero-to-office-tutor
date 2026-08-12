# Installation Guide

This repository supports **ChatGPT Projects**, **ChatGPT Custom GPTs**, and **Claude Custom Skills**. A GitHub URL by itself does not modify an AI account; follow the platform-specific path below.

---

# ChatGPT Go: recommended path = Project

ChatGPT Go includes Projects and access to custom GPTs subject to current feature availability. OpenAI also documents that **building/editing GPTs is available on the web experience only**; mobile apps can use GPTs but cannot build them.

If your colleague cannot see **Create GPT**, do not block the installation. Use a **Project** instead.

## Install as a Project
1. Open ChatGPT and choose **New project** in the sidebar.
2. Name it `BA Zero-to-Office Tutor`.
3. Open the project menu → **Project settings**.
4. Copy the contents of `chatgpt/GPT-INSTRUCTIONS.md` into **Project instructions**.
5. Upload the seven files in `skills/ba-zero-to-office-tutor/references/` as project files:
   - `curriculum.md`
   - `teaching-protocol.md`
   - `cognitive-load.md`
   - `assessment-rubric.md`
   - `learner-state.md`
   - `office-case-bank.md`
   - `technical-mental-maps.md`
6. Start a chat **inside that project** and test: `Saya sudah hafal definisi BPMN. Berarti sudah paham kan?`

OpenAI currently documents **25 files per project for Go and Plus**, so this 7-file setup fits comfortably. Project instructions apply only inside that project and override global custom instructions there.

## If your colleague wants a Custom GPT instead
Use ChatGPT on the **web**, not the Android/iOS app. Open **Explore GPTs → Create**. Paste `chatgpt/GPT-INSTRUCTIONS.md` into Instructions and upload the seven reference files as Knowledge.

If **Create GPT** is still absent on web despite an active Go subscription, treat it as feature availability/account rollout rather than assuming Go is unsupported. The official Go page lists custom GPT access as subject to current feature availability. The Project installation above remains usable.

Official OpenAI references:
- https://help.openai.com/en/articles/11989085
- https://help.openai.com/en/articles/8554397-creating-a-gpt
- https://help.openai.com/en/articles/10169521-projects-in-chatgpt

---

# ChatGPT Plus / Pro / other eligible paid plans: Custom GPT

1. Open ChatGPT **web**.
2. Go to **Explore GPTs → Create**.
3. Name it `BA Zero-to-Office Tutor`.
4. Paste `chatgpt/GPT-INSTRUCTIONS.md` into **Instructions**.
5. Upload the same seven canonical reference files into **Knowledge**.
6. Test with the probes under **Verification** below.

`chatgpt/BUILDER-PROMPT.md` is optional. `chatgpt/KNOWLEDGE-BA-TUTOR.md` can be generated with `python3 scripts/build.py`, but uploading the seven canonical files directly is simpler and avoids generated-file drift.

---

# Claude: native Custom Skill

Claude Skills are available on **Free, Pro, Max, Team, and Enterprise**. Code execution/file creation must be enabled.

## Fast install
1. Clone/download this repository.
2. Build the ZIP:
   ```bash
   python3 scripts/build.py
   ```
3. In Claude, enable **Settings → Capabilities → Code execution and file creation** if needed.
4. Open **Customize → Skills**.
5. Click **+ → Create skill → Upload a skill**.
6. Upload `dist/ba-zero-to-office-tutor-claude.zip`.
7. Enable the skill.
8. Start a new chat and ask: `Lanjutkan target Technical BA saya dari nol.`

## Required ZIP structure
Anthropic requires the ZIP to contain the skill folder as its root:

```text
ba-zero-to-office-tutor-claude.zip
└── ba-zero-to-office-tutor/
    ├── SKILL.md
    └── references/
        ├── curriculum.md
        └── ...
```

The build script produces exactly this layout. The folder name matches the YAML `name`, and the repository uses uppercase `SKILL.md`, consistent with Anthropic's own public skills repository and template.

## Claude troubleshooting
If **Customize → Skills** is missing, enable Code execution/file creation first. If upload fails, check:
- ZIP contains the named skill folder at its root;
- folder name matches the YAML `name`;
- `SKILL.md` exists inside that folder;
- YAML frontmatter contains valid `name` and `description`;
- description is concise and free of invalid characters.

Official Anthropic references:
- https://support.claude.com/en/articles/12512180-use-skills-in-claude
- https://support.claude.com/en/articles/12512198-how-to-create-custom-skills
- https://github.com/anthropics/skills

---

# Claude Code / Agent Skills-compatible harnesses

Copy/install the entire folder:

```text
skills/ba-zero-to-office-tutor/
```

Keep `SKILL.md` and `references/` together.

---

# Verification

### Memorization probe
```text
Saya sudah hafal: API adalah Application Programming Interface. Berarti materi API selesai kan?
```
Expected: no automatic mastery; tutor asks for transfer/application evidence.

### Overload probe
```text
Jelaskan REST, GraphQL, SOAP, JSON, XML, OAuth 2.0, JWT semuanya sekarang dari nol.
```
Expected: category map + one active cluster, not seven disconnected definitions.

### Urgent-office probe
```text
Saya belum belajar API tapi satu jam lagi harus review requirement integrasi payment. Bantu saya.
```
Expected: URGENT mode, minimum conceptual bridge, review checklist, miniature example, then back to the real task.
