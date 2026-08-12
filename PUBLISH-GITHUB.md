# Publish to GitHub

Intended repository name:

```text
ba-zero-to-office-tutor
```

## One-command path with GitHub CLI

From the repository root, after `gh auth login`:

```bash
bash scripts/publish-github.sh
```

The script creates a **public** repository under the currently authenticated GitHub account, sets `origin`, commits the current repository contents, and pushes the `main` branch.

It stops if:
- `gh` is not installed;
- GitHub CLI is not authenticated;
- a repository with the same name already exists under the authenticated account;
- the working directory is not this project.

Review the files before running because publishing makes the repository public.

## Manual GitHub web + connected-agent path

If an AI connector cannot create repositories:
1. Create an empty public repository named `ba-zero-to-office-tutor` on GitHub. Do not initialize it with README, license, or `.gitignore`.
2. Grant the connected GitHub app access to that repository.
3. Ask the connected agent to upload the prepared repository contents.

The connector still needs write permission to the target repository.
