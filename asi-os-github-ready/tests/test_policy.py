from asi_os.core.contracts import AgentTask
from asi_os.security.policy import PolicyEngine


def test_policy_denies_missing_capability() -> None:
    task = AgentTask(goal="x", agent="a")
    decision = PolicyEngine().authorize(task, "shell.execute")
    assert not decision.allowed
