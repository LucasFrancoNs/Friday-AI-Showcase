"""Small deterministic capability router used by the public showcase.

The private Friday project contains a much broader registry and policy layer.
This module intentionally demonstrates the routing idea without exposing private
integrations, credentials, or device-control internals.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Route:
    capabilities: tuple[str, ...]
    reason: str


_RULES: tuple[tuple[tuple[str, ...], tuple[str, ...]], ...] = (
    (("html", "css", "frontend", "web repair"), ("web_repair",)),
    (("traceback", "python error", "self-heal", "self heal"), ("self_healing",)),
    (("sandbox", "untrusted code"), ("sandbox", "security")),
    (("doctor", "health check", "integrity"), ("doctor", "defender")),
    (("debug", "debugger"), ("debugger",)),
    (("agent", "team", "multi-agent", "multi agent"), ("orchestration",)),
    (("memory", "context", "long session"), ("session_context",)),
)


def route(text: str) -> Route:
    normalized = " ".join(text.lower().split())
    selected: list[str] = ["capability_control"]
    matched: list[str] = []

    for keywords, capabilities in _RULES:
        if any(keyword in normalized for keyword in keywords):
            matched.extend(keyword for keyword in keywords if keyword in normalized)
            for capability in capabilities:
                if capability not in selected:
                    selected.append(capability)

    if len(selected) == 1:
        selected.append("conversation")

    return Route(tuple(selected), ", ".join(matched) if matched else "general conversation")
