"""audit.py — Audit trail for all authorization decisions."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class AuditRecord:
    """A single audit record."""
    trace_id: str
    decision: str
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    details: dict[str, Any] = field(default_factory=dict)


class AuditLog:
    """Append-only audit log."""

    def __init__(self) -> None:
        self._records: list[AuditRecord] = []

    def record(self, record: AuditRecord) -> None:
        self._records.append(record)

    def all_records(self) -> tuple[AuditRecord, ...]:
        return tuple(self._records)
