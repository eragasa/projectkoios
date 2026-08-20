from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class AgentWorkspace:
    agent_name: str
    root: Path
    current_repo: str | None = None
    current_focus: str | None = None

    @property
    def state_path(self) -> Path:
        return self.root / "state.md"

    @property
    def active_path(self) -> Path:
        return self.root / "active.md"

    @property
    def decisions_dir(self) -> Path:
        return self.root / "decisions"

    @property
    def sessions_dir(self) -> Path:
        return self.root / "sessions"

    @property
    def handoffs_dir(self) -> Path:
        return self.root / "handoffs"

    @property
    def handoffs_incoming_dir(self) -> Path:
        return self.handoffs_dir / "incoming"

    @property
    def handoffs_outgoing_dir(self) -> Path:
        return self.handoffs_dir / "outgoing"

    def resolve(self, *parts: str | Path) -> Path:
        path = self.root
        for part in parts:
            path = path / Path(part)
        return path

    def ensure_layout(self) -> tuple[Path, ...]:
        return (
            self.root,
            self.decisions_dir,
            self.handoffs_dir,
            self.handoffs_incoming_dir,
            self.handoffs_outgoing_dir,
            self.sessions_dir,
        )
