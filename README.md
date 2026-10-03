# menato_test

A small sandbox for testing [Memanto](https://github.com/HARSHAVARDHAN-RAJU5/memanto) persistent memory across several AI coding agents. Each agent has its own folder with the Memanto instructions, skill and hooks it needs, plus a tiny calculator project to work on.

Memanto is a CLI that gives an agent memory between sessions. The agent is instructed to run `memanto memory sync` and `memanto recall` at the start of a session, and `memanto remember` to store what it learns.

Based on my fork of memanto: https://github.com/HARSHAVARDHAN-RAJU5/memanto

## Repository layout

| Folder | Agent | Instructions file | Memanto skill / config |
| --- | --- | --- | --- |
| `claude/` | Claude Code | `CLAUDE.md` | `.claude/skills/memanto/SKILL.md`, `.claude/settings.json` |
| `Xeno-test-claude/` | Claude Code (separate test project) | `CLAUDE.md` | `.claude/skills/memanto/SKILL.md`, `.claude/settings.json` |
| `codex/` | OpenAI Codex | `AGENTS.md` | `.agents/skills/memanto/SKILL.md`, `.agents/hooks.json` |
| `cursor/` | Cursor | `.cursor/rules/memanto.mdc` | `.cursor/skills/memanto/SKILL.md`, `.cursor/hooks.json` |
| `gemini/` | Gemini CLI | `GEMINI.md` | `.gemini/skills/memanto/SKILL.md` |

The `claude/`, `codex/` and `cursor/` folders also contain a `calculator.py` used as a simple task for the agent.

## How it works

- **Instructions file** (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, or a Cursor rule) holds a Memanto-managed section. It tells the agent when to sync, recall and remember.
- **Skill** (`SKILL.md`) is a reference for command syntax, memory types, confidence levels, provenance and tagging.
- **Hooks** run `memanto memory sync --project-dir .` when a session starts and before context is compacted, so memory is loaded and saved automatically.

## Getting started

1. Install Memanto and make sure the `memanto` command works in your shell.
2. Open one of the agent folders (for example `claude/`) in the matching agent.
3. Start a session. The agent should run `memanto memory sync` and `memanto recall` first.
4. Ask it to work on `calculator.py`, end the session, then start a new one and check whether it remembers what it did.

Useful commands:

```bash
memanto remember "A rule or fact worth keeping" --type TYPE --tags "tag1,tag2" --confidence 0.9
memanto recall "query" --limit 10
memanto memory sync --project-dir .
```

## Calculator

`calculator.py` is a command-line calculator that safely evaluates arithmetic with `+ - * / **`, parentheses and an `sq()` function, using Python's `ast` module rather than `eval`.

```bash
python calculator.py
```

## Notes

- `.venv/`, `__pycache__/`, `.env` and `settings.local.json` are git-ignored.
- The hook commands in `hooks.json` and `settings.json` contain paths from my Windows machine. Update them for your own Python install.
