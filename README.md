# FRIDAY // Autonomous Systems Interface

> A local-first experimental AI agent architecture focused on modular capabilities, deterministic diagnostics, sandboxed code workflows, security boundaries and long-session resilience.

**Friday-AI-Showcase** is the public, sanitized portfolio edition of my personal Friday AI project. It intentionally does **not** include private credentials, personal memory, character/Live2D assets, private integrations, or full device-control internals.

The public UI uses an **original holographic systems HUD**. It is inspired by general science-fiction interface design; it is not affiliated with or a reproduction of Marvel/JARVIS.

## Live-style HUD demo

Open [`index.html`](index.html) locally to view the zero-dependency holographic interface. It visualizes the architecture rather than controlling your computer.

```text
FRIDAY
  |
  +-- Capability Router
  +-- Policy / Security Engine
  +-- Doctor + Debugger
  +-- Self-Healing
  +-- Sandbox Gate
  +-- Dynamic Agent Teams
  +-- Defender / Performance Guard
  +-- Session Context Resilience
  +-- Web Repair
```

## Why this architecture exists

The goal is **not** to give one model every tool all the time. Friday tries to stay large in capability but small during each task:

```text
request
  -> route intent
  -> expose only relevant capabilities
  -> enforce policy
  -> run deterministic tools first
  -> use a model only when reasoning is actually needed
```

## Public demo modules

| Module | What it demonstrates |
|---|---|
| `capability_router.py` | deterministic small-bundle routing |
| `doctor.py` | local Python structural checks |
| `context_manager.py` | bounded deterministic session compaction |
| `web_repair.py` | conservative high-confidence HTML repair |
| `index.html` | original holographic Friday HUD |

These are deliberately smaller public implementations. The private project contains the broader experimental runtime.

## Engineering themes

- **Deterministic-first Doctor / Debugger** — common structural errors do not need an LLM.
- **Local-first model strategy** — sensitive workflows can prefer local inference.
- **Capability routing + lazy loading** — avoid exposing/loading the whole agent at once.
- **Dynamic teams with fixed permission profiles** — roles can be dynamic; privileges cannot invent themselves.
- **Sandbox-first coding** — AI-generated code belongs in staging before promotion.
- **Prompt-injection defense** — external content is data, not authorization.
- **Defender + performance guard** — integrity and resource regressions are measurable.
- **Chaos testing** — intentionally stress routing, memory, budgets and failing components.
- **Context resilience** — long sessions are bounded without silently deleting recent turns.

## Quick test

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

The browser HUD has no package dependencies: open `index.html` directly.

## Repository boundaries

Not published here:

- API keys / `.env` / `key.env`
- cookies or authentication material
- personal memory and conversation history
- logs/checkpoints/runtime artifacts
- private automation and account integrations
- Live2D character/model assets
- personal device configuration

## Evolution

The private project evolved through several engineering milestones: Doctor/Debugger, Policy Engine, autonomous loops, capability routing, dynamic teams, self-healing, prompt-injection defense, sandbox gating, strategic autonomy, Defender/Performance Guard, Chaos Lab and context resilience.

This repository presents those ideas as a clean portfolio/open-core surface rather than publishing every private implementation detail.

## Author

Built by **Lucas Franco** as a long-term personal AI/agent engineering project.
