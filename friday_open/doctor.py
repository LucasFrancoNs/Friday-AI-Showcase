"""Deterministic Python health checks for the public Friday showcase."""

from __future__ import annotations

import ast
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Finding:
    path: str
    line: int | None
    severity: str
    message: str


def scan_python_file(path: str | Path) -> list[Finding]:
    file_path = Path(path)
    try:
        source = file_path.read_text(encoding="utf-8")
    except OSError as exc:
        return [Finding(str(file_path), None, "error", f"read failed: {exc}")]

    try:
        tree = ast.parse(source, filename=str(file_path))
    except SyntaxError as exc:
        return [Finding(str(file_path), exc.lineno, "error", exc.msg)]

    findings: list[Finding] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and len(node.body) == 1 and isinstance(node.body[0], ast.Pass):
            findings.append(Finding(str(file_path), node.lineno, "info", f"function '{node.name}' is a stub"))
    return findings
