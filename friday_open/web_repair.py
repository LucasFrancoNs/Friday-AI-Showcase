"""Conservative deterministic HTML repair used by the showcase.

Only unambiguous trailing unclosed tags are auto-repaired. Crossed/mismatched
structures are diagnosed but intentionally not rewritten.
"""

from __future__ import annotations

from dataclasses import dataclass
from html.parser import HTMLParser


_VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


@dataclass(frozen=True)
class RepairResult:
    ok: bool
    changed: bool
    confidence: float
    output: str
    message: str


class _StackParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[str] = []
        self.mismatch: str | None = None

    def handle_starttag(self, tag: str, attrs) -> None:  # type: ignore[override]
        if tag not in _VOID:
            self.stack.append(tag)

    def handle_startendtag(self, tag: str, attrs) -> None:  # type: ignore[override]
        return

    def handle_endtag(self, tag: str) -> None:
        if not self.stack or self.stack[-1] != tag:
            self.mismatch = tag
            return
        self.stack.pop()


def repair_html(source: str) -> RepairResult:
    parser = _StackParser()
    parser.feed(source)
    parser.close()

    if parser.mismatch:
        return RepairResult(False, False, 0.35, source, f"mismatched closing tag: </{parser.mismatch}>")
    if not parser.stack:
        return RepairResult(True, False, 1.0, source, "HTML structure is balanced")

    suffix = "".join(f"</{tag}>" for tag in reversed(parser.stack))
    return RepairResult(True, True, 0.98, source + suffix, f"closed {len(parser.stack)} trailing tag(s)")
