# Installation Guide

## Important: what a GitHub link can and cannot do

An AI can read this public repository and explain the installation steps when web access is available. **ChatGPT cannot install or reconfigure a Custom GPT into the user's account merely because it received a GitHub URL.** The owner of the GPT must still create/edit the GPT and supply its Instructions/Knowledge through the ChatGPT UI.

That distinction is deliberate: this repository is designed so a colleague can send the repo URL to an AI and the AI can immediately identify the correct platform-specific installation path without requiring the colleague to understand prompt engineering.

---

# ChatGPT (recommended for ChatGPT Plus/Pro and other plans that can create GPTs)

OpenAI documents Custom GPT behavior separately from Knowledge: behavior/workflow belongs in **Instructions**, while reference material belongs in uploaded **Knowledge** files.

## Files to use
- `chatgpt/GPT-INSTRUCTIONS.md` → paste into GPT **Instructions**.
- `chatgpt/KNOWLEDGE-BA-TUTOR.md` → upload as **Knowledge**.
- Optional: `chatgpt/BUILDER-PROMPT.md` → paste into the conversational GPT Builder to bootstrap the configuration.

## Install
1. On ChatGPT web, open **Explore GPTs** and choose **Create**.
2. Name it `BA Zero-to-Office Tutor`.
3. In **Configure**, paste the complete contents of `chatgpt/GPT-INSTRUCTIONS.md` into **Instructions**.
4. Upload `chatgpt/KNOWLEDGE-BA-TUTOR.md` under **Knowledge**.
5. Add the conversation starters from `chatgpt/BUILDER-PROMPT.md` if desired.
6. Test with: `Saya sudah hafal definisi BPMN. Berarti sudah paham kan?` A correct setup should challenge transfer/application rather than immediately mark the topic mastered.

## If your colleague only receives the GitHub URL
They can paste this into ChatGPT:

```text
Read this GitHub repository and help me install its BA tutor configuration into my ChatGPT account:
<REPOSITORY_URL>

Follow the repository's INSTALL.md exactly. Do not claim you can change my GPT configuration yourself. Tell me which files go into Instructions and Knowledge, then help me test the result.
```

Replace `<REPOSITORY_URL>` with the published repository URL.

Official OpenAI reference:
https://help.openai.com/en/articles/8554397-creating-a-gpt

---

# Claude chat custom Skill

Anthropic supports uploading a custom Skill as a ZIP. Code execution must be enabled for Skills.

## File to use
`dist/ba-zero-to-office-tutor-claude.zip`

## Install
1. Open Claude.
2. Go to **Customize → Skills**.
3. Choose **+ → Create skill → Upload a skill**.
4. Upload `dist/ba-zero-to-office-tutor-claude.zip`.
5. Enable the skill.
6. Start a new chat and ask: `Lanjutkan target Technical BA saya dari nol.`

Official Anthropic references:
https://support.claude.com/en/articles/12512180-use-skills-in-claude
https://support.claude.com/en/articles/12512198-how-to-create-custom-skills

---

# Claude Code / other Agent Skills-compatible harnesses

The canonical skill directory is:

```text
skills/ba-zero-to-office-tutor/
```

For a harness that supports the Agent Skills convention, install/copy that entire folder into the skills directory recognized by the harness. Keep `SKILL.md` and `references/` together.

If using a repository-based skills installer, point it at the published repository and select `skills/ba-zero-to-office-tutor` when the installer supports subdirectory installation.

---

# Verify behavior after installation

Use these three probes:

### Probe 1 — memorization
```text
Saya sudah hafal: API adalah Application Programming Interface. Berarti materi API selesai kan?
```
Expected: tutor refuses to equate a definition with mastery and gives a transfer task.

### Probe 2 — overload
```text
Jelaskan REST, GraphQL, SOAP, JSON, XML, OAuth 2.0, JWT semuanya sekarang dari nol.
```
Expected: tutor creates a category map and teaches one cluster first instead of dumping seven definitions.

### Probe 3 — office urgency
```text
Saya belum belajar API tapi satu jam lagi harus review requirement integrasi payment. Bantu saya.
```
Expected: tutor enters urgent mode and gives minimum bridge concepts plus a review checklist.
