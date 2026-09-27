"""Bounded deterministic context compaction demo."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CompactResult:
    summary: str
    recent: tuple[str, ...]
    compacted: bool


def compact(messages: list[str], max_chars: int = 60_000, keep_recent_chars: int = 24_000, summary_chars: int = 12_000) -> CompactResult:
    total = sum(len(message) for message in messages)
    if total <= max_chars:
        return CompactResult("", tuple(messages), False)

    recent: list[str] = []
    recent_size = 0
    split_at = len(messages)
    for index in range(len(messages) - 1, -1, -1):
        candidate = messages[index]
        if recent and recent_size + len(candidate) > keep_recent_chars:
            break
        recent.insert(0, candidate)
        recent_size += len(candidate)
        split_at = index

    old = messages[:split_at]
    bullets = [f"- {item.strip()[:240]}" for item in old if item.strip()]
    summary = "\n".join(bullets)
    if len(summary) > summary_chars:
        summary = summary[: summary_chars - 3] + "..."
    return CompactResult(summary, tuple(recent), True)
