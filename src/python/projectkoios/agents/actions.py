from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Literal

from projectkoios.agents.workspace import AgentWorkspace

WorkspaceActionKind = Literal[
    "state",
    "active",
    "decision",
    "session",
    "handoff-incoming",
    "handoff-outgoing",
]


def _slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "action"


def _timestamp(moment: datetime) -> str:
    return moment.astimezone(UTC).strftime("%Y%m%d.%H%M%S")


@dataclass(frozen=True, slots=True)
class AgentWorkspaceAction:
    kind: WorkspaceActionKind
    title: str
    body: str = ""
    details: tuple[str, ...] = ()
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    def target_path(self, workspace: AgentWorkspace) -> Path:
        filename = f"{_timestamp(self.created_at)}_{_slugify(self.title)}.md"

        match self.kind:
            case "state":
                return workspace.state_path
            case "active":
                return workspace.active_path
            case "decision":
                return workspace.decisions_dir / filename
            case "session":
                return workspace.sessions_dir / filename
            case "handoff-incoming":
                return workspace.handoffs_incoming_dir / filename
            case "handoff-outgoing":
                return workspace.handoffs_outgoing_dir / filename

        raise ValueError(f"unsupported workspace action kind: {self.kind}")

    def render(self, workspace: AgentWorkspace) -> str:
        lines = [
            f"# {self.title}",
            "",
            f"- Agent: {workspace.agent_name}",
            f"- Workspace: {workspace.root}",
            f"- Kind: {self.kind}",
            f"- Created: {self.created_at.astimezone(UTC).isoformat()}",
        ]
        if workspace.current_repo is not None:
            lines.append(f"- Repo: {workspace.current_repo}")
        if workspace.current_focus is not None:
            lines.append(f"- Focus: {workspace.current_focus}")
        if self.details:
            lines.extend(["", "## Details"])
            lines.extend(f"- {detail}" for detail in self.details)
        if self.body:
            lines.extend(["", self.body.rstrip()])
        return "\n".join(lines).rstrip() + "\n"

    def apply(self, workspace: AgentWorkspace) -> Path:
        for path in workspace.ensure_layout():
            path.mkdir(parents=True, exist_ok=True)

        target = self.target_path(workspace)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(self.render(workspace), encoding="utf-8")
        return target
