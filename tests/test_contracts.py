from asi_os.core.contracts import AgentTask, TaskState


def test_agent_task_defaults() -> None:
    task = AgentTask(goal="test", agent="demo")
    assert task.state == TaskState.CREATED
    assert task.limits.max_steps == 20
