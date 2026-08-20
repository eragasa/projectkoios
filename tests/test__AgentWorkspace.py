from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

from projectkoios.agents import AgentWorkspace, AgentWorkspaceAction


def test__agent_workspace__standard_paths() -> None:
    workspace = AgentWorkspace(
        agent_name="hermes",
        root=Path("/tmp/workspaces/hermes"),
        current_repo="projectkoios",
        current_focus="routing",
    )

    assert workspace.state_path == Path("/tmp/workspaces/hermes/state.md")
    assert workspace.active_path == Path("/tmp/workspaces/hermes/active.md")
    assert workspace.decisions_dir == Path("/tmp/workspaces/hermes/decisions")
    assert workspace.sessions_dir == Path("/tmp/workspaces/hermes/sessions")
    assert workspace.handoffs_incoming_dir == Path(
        "/tmp/workspaces/hermes/handoffs/incoming"
    )
    assert workspace.handoffs_outgoing_dir == Path(
        "/tmp/workspaces/hermes/handoffs/outgoing"
    )


def test__agent_workspace_action__writes_session_note(tmp_path: Path) -> None:
    workspace = AgentWorkspace(
        agent_name="athena",
        root=tmp_path / "athena",
        current_repo="projectkoios",
        current_focus="bounded spec",
    )
    action = AgentWorkspaceAction(
        kind="session",
        title="Spec intake",
        body="Captured the current task boundary.",
        details=("one repo", "one spec"),
        created_at=datetime(2026, 7, 1, 12, 34, 56, tzinfo=UTC),
    )

    target = action.apply(workspace)

    assert target == workspace.sessions_dir / "20260701.123456_spec-intake.md"
    assert target.read_text(encoding="utf-8") == (
        "# Spec intake\n"
        "\n"
        "- Agent: athena\n"
        "- Workspace: " + str(workspace.root) + "\n"
        "- Kind: session\n"
        "- Created: 2026-07-01T12:34:56+00:00\n"
        "- Repo: projectkoios\n"
        "- Focus: bounded spec\n"
        "\n"
        "## Details\n"
        "- one repo\n"
        "- one spec\n"
        "\n"
        "Captured the current task boundary.\n"
    )


def test__agent_workspace_action__routes_fixed_files(tmp_path: Path) -> None:
    workspace = AgentWorkspace(agent_name="vulcan", root=tmp_path / "vulcan")
    state = AgentWorkspaceAction(kind="state", title="State")
    active = AgentWorkspaceAction(kind="active", title="Active")

    assert state.apply(workspace) == workspace.state_path
    assert active.apply(workspace) == workspace.active_path
