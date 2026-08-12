# Installation Guide

This repository is designed so a colleague can give its GitHub URL to an AI and receive the correct installation path without needing prompt-engineering knowledge.

## Important limitation
A GitHub URL does **not** let ChatGPT silently reconfigure a Custom GPT inside the user's account. The GPT owner still has to create/edit the GPT and add Instructions/Knowledge in the UI. The AI should guide those steps accurately rather than pretending installation happened automatically.

---

# ChatGPT Custom GPT

## Behavior file
Paste the complete contents of:

`chatgpt/GPT-INSTRUCTIONS.md`

into the GPT **Instructions** field.

## Knowledge files
Upload these seven canonical files from:

`skills/ba-zero-to-office-tutor/references/`

- `curriculum.md`
- `teaching-protocol.md`
- `cognitive-load.md`
- `assessment-rubric.md`
- `learner-state.md`
- `office-case-bank.md`
- `technical-mental-maps.md`

If you cloned the repository and ran `python3 scripts/build.py`, you may upload generated `chatgpt/KNOWLEDGE-BA-TUTOR.md` instead of the seven separate files.

Optional: `chatgpt/BUILDER-PROMPT.md` can be used with the conversational GPT Builder.

## Install
1. Open ChatGPT web → **Explore GPTs** → **Create**.
2. Name it `BA Zero-to-Office Tutor`.
3. Paste `chatgpt/GPT-INSTRUCTIONS.md` into **Instructions**.
4. Upload the seven canonical reference files above into **Knowledge** (or the generated single-file bundle if you built it locally).
5. Add conversation starters from `chatgpt/BUILDER-PROMPT.md` if desired.
6. Test with: `Saya sudah hafal definisi BPMN. Berarti sudah paham kan?`

Expected behavior: it should distinguish recall from mastery and ask for transfer/application evidence.

## If the colleague only has this GitHub URL
Give ChatGPT this instruction:

```text
Read this GitHub repository and help me install its BA tutor configuration into my ChatGPT account.
Follow INSTALL.md exactly. Do not claim you can change my GPT configuration yourself.
Tell me which file becomes Instructions, which seven files become Knowledge, then help me test the result.
```

Official OpenAI reference:
https://help.openai.com/en/articles/8554397-creating-a-gpt

---

# Claude chat / custom Skill

The canonical Agent Skill is:

`skills/ba-zero-to-office-tutor/`

To create an uploadable ZIP without relying on a prebuilt binary, clone/download the repository and run:

```bash
python3 scripts/build.py
```

Then upload:

`dist/ba-zero-to-office-tutor-claude.zip`

Typical Claude path:
**Customize → Skills → Create skill → Upload a skill**.

If you do not run the build script, zip the **contents** of `skills/ba-zero-to-office-tutor/` so `SKILL.md` and `references/` remain together.

Official Anthropic references:
https://support.claude.com/en/articles/12512180-use-skills-in-claude
https://support.claude.com/en/articles/12512198-how-to-create-custom-skills

---

# Claude Code / Agent Skills-compatible harnesses

Copy/install the entire folder:

```text
skills/ba-zero-to-office-tutor/
```

Keep `SKILL.md` and `references/` together.

---

# Verification probes

### Memorization probe
```text
Saya sudah hafal: API adalah Application Programming Interface. Berarti materi API selesai kan?
```
Expected: no automatic mastery; tutor requests transfer/application.

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
