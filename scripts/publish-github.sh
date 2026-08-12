#!/usr/bin/env bash
set -euo pipefail

REPO_NAME="ba-zero-to-office-tutor"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI (gh) is required: https://cli.github.com/" >&2
  exit 1
fi

if ! gh auth status >/dev/null 2>&1; then
  echo "GitHub CLI is not authenticated. Run: gh auth login" >&2
  exit 1
fi

if [[ ! -f "skills/ba-zero-to-office-tutor/SKILL.md" ]]; then
  echo "Run this script from the BA Zero-to-Office Tutor repository." >&2
  exit 1
fi

OWNER="$(gh api user --jq .login)"
if gh repo view "$OWNER/$REPO_NAME" >/dev/null 2>&1; then
  echo "Repository already exists: $OWNER/$REPO_NAME" >&2
  exit 1
fi

python3 scripts/build.py
python3 -m unittest tests/test_repository.py -v

if ! git rev-parse --verify HEAD >/dev/null 2>&1; then
  git checkout -B main
else
  CURRENT="$(git branch --show-current)"
  if [[ "$CURRENT" != "main" ]]; then
    git checkout -B main
  fi
fi

git add -- .gitignore INSTALL.md LICENSE README.md REFERENCES.md PUBLISH-GITHUB.md chatgpt dist docs examples scripts skills tests
git commit -m "feat: add BA Zero-to-Office Tutor skill"
gh repo create "$OWNER/$REPO_NAME" --public --source=. --remote=origin --push

echo "Published: https://github.com/$OWNER/$REPO_NAME"
