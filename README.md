# ttrpg_engine

This repository holds a mathless, simulationist, exception-based fantasy TTRPG design framework, mid-rewrite. The rules themselves live in `ttrpg_idealization/`; a frozen snapshot of everything from before the reorganization lives beside it.

## Layout

```text
ttrpg_engine/
├── ttrpg_idealization/                                          # active framework rewrite
│   ├── 00_architecture/                                         # registry, architecture map, manifests
│   ├── 01_framework/                                            # canonical rule specifications (in migration)
│   ├── 02_decisions/01_master_decision_log.md                   # DEC-001 … running
│   ├── 03_workflows/ … 07_publication_drafts/
│   └── chat_history/                                            # design conversation log
└── ttrpg_idealization_pre_reorganization_archive_2026-08-07/    # frozen pre-rewrite snapshot (900 files)
```

The active root's relative links to the archive work because both trees sit side by side here, just as they did in the original workspace.

## Cloning without the archive

The archive is the bulk of the file count (900 files, mostly conversation logs and research). If you're working in limited storage, clone without it — git can fetch only what you check out:

```sh
git clone --filter=blob:none --no-checkout https://github.com/ThiagoRibas-dev/ttrpg_engine.git
cd ttrpg_engine
git sparse-checkout set ttrpg_idealization
git checkout main
```

That gives you the root files and `ttrpg_idealization/` only; the archive's contents are never downloaded. (Anything under `ttrpg_idealization/` that links into the archive will point at files you don't have locally.)

## Where to start reading

- `ttrpg_idealization/README.md` — the project's own front door.
- `ttrpg_idealization/FRAMEWORK_REORGANIZATION_MODEL_DRAFT.md` — the reorganization plan the rewrite follows.
- `ttrpg_idealization/00_architecture/framework_architecture_map.md` — the map of what exists and what's still pending.
- `AGENTS.md` inside the active root — working conventions (decision log, chat-history practice, editing rules, publishing procedure).
