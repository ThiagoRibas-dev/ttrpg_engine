# Agent Operating Guide — Framework Rewrite Root

## Active-root boundary

This root is the active framework rewrite. The sibling archive is historical source material. Since 2026-09-19 both trees live side by side inside the git repository, so the archive is a sibling directory of this root:

```text
../ttrpg_idealization_pre_reorganization_archive_2026-08-07/
```

The repository root (which holds `.gitignore`, the repo `README.md`, and both trees) is `ttrpg_engine/`.

No archived rule is active until it is explicitly migrated into `01_framework/`, registered in `00_architecture/framework_registry.yaml`, and recorded in `00_architecture/migration_manifest.md`.

## Source-of-truth order

1. Explicit current-session user decisions.
2. Migrated canonical specifications in `01_framework/`.
3. Active Decision Records and `02_decisions/01_master_decision_log.md`.
4. `00_architecture/framework_registry.yaml` for formal document relationships and ownership metadata.
5. Workflows in `03_workflows/`.
6. Research in `04_research/` and experiments in `05_experiments/`.
7. The sibling archive and `99_archive/`.

## Documentation policy

- Rule files own rules.
- The YAML registry owns formal relationships.
- Decision records own major rationale.
- Research owns evidence and alternatives.
- Experiments are never canon.
- Use precise relative Markdown links to exact sections on first meaningful cross-system reference.
- Use stable anchors for canonical registered procedures once migration starts.
- Do not manually duplicate formal dependency lists inside rule files.

## Editing practices

- **Never batch multiple edits to the same file in one parallel tool block.** Apply them one at a time, or combine them into a single edit. Parallel same-file edits can silently clobber each other while still reporting success (incident: 2026-09-18, during the DEC-108 updates).
- **Validate file writes with a `python3` check block after substantive edits** — verify expected content landed, relative links resolve, and registry/anchor integrity holds. This is what caught the 2026-09-18 incident.

## Git publishing

The project is published at `https://github.com/ThiagoRibas-dev/ttrpg_engine` (public). First push: 2026-09-19, containing both trees. Push again at meaningful milestones (batch completions, decision clusters), not necessarily every turn.

- **Layout:** both trees are siblings inside the repo, which is what keeps every relative archive link working.
- **Credentials:** a fine-grained throwaway PAT lives at `~/.git-creds/github_token` (600), used via the askpass script `~/.git-creds/git-askpass.sh` (700) and `core.askPass` in `~/.gitconfig` (all outside the repo and outside git). Never commit, echo, or record the token; redact it from chat-history records. The user can revoke it at any time.
- **Snapshot caveat:** workspace snapshots do not persist `.git/config`, and files restored from snapshot may lose executable permissions. At the start of a new session, before pushing:
  `git -C /home/user/ttrpg_engine remote add origin https://github.com/ThiagoRibas-dev/ttrpg_engine.git`
  `chmod 700 ~/.git-creds/git-askpass.sh && chmod 600 ~/.git-creds/github_token`
  The global config (askpass, identity) persists in `~/.gitconfig` and needs no restore. (Both caveats fired for real on 2026-09-23; the restore took under a minute.)
- **Cloning without the archive** (limited storage): partial clone + sparse checkout, as documented in the repo `README.md`:
  `git clone --filter=blob:none --no-checkout <url> && cd ttrpg_engine && git sparse-checkout set ttrpg_idealization && git checkout main`
- **Commit identity:** `ThiagoRibas-dev <56689080+ThiagoRibas-dev@users.noreply.github.com>`.
- **Before every push:** grep the repo for `github_pat_` (must be zero hits) and confirm `git status` is clean after the commit.
- **Uploads stay out of the repo** (user ruling, 2026-09-19): the workspace `uploads/` directory is reference material only. Files are incorporated case-by-case — into research, conversion notes, or content — when explicitly migrated; never bulk-published.

## Chat history

Store every user and assistant turn under `chat_history/` with sequential zero-padded filenames. Legacy records were copied unchanged from the archived root; do not edit or reorder them.
