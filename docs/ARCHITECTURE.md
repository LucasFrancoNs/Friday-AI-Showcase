# Architecture overview

Friday is organized around **capability isolation**, **policy enforcement**, and **deterministic-first tooling**.

```text
User goal
   |
Capability Router
   |
Policy / provenance gate
   |
+----------------------+----------------------+-------------------+
|                      |                      |                   |
Doctor / Debugger   Dynamic Agents        Self-Healing        Sandbox
|                      |                      |                   |
+----------------------+----------+-----------+-------------------+
                                  |
                              Reviewer
                                  |
                           explicit promotion
```

## Design principles

- **Large capability surface, small runtime bundle.** Only relevant tool schemas/modules are loaded for a task.
- **Deterministic first.** Doctor, Debugger, Web Repair, context compaction and many security checks do not require an LLM.
- **Local first.** Sensitive code/data should prefer local inference when available.
- **Data is not authorization.** Web pages, documents and external messages may provide information but do not grant permission.
- **AI writes to staging.** Generated code is expected to work in a sandbox/staging workspace before promotion.
- **Fail closed.** Missing isolation or uncertain repair should block automatic execution rather than silently downgrade safety.

## Public vs. private

This repository is a **sanitized showcase/open-core demonstration**. The private project contains additional integrations, personal companion UI, local configuration, device automation, and experimental modules that are intentionally not published here.
