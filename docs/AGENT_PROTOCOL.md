# Agent Protocol

## Agent manifest

```yaml
name: coding-agent
version: 0.1.0
capabilities:
  - repo.read
  - repo.write
  - code.execute
  - tests.run
model_role: coding
risk_profile: medium
approval:
  production_deploy: human
limits:
  max_steps: 40
  max_wall_time_seconds: 1800
```

## Task contract

```json
{
  "task_id": "uuid",
  "goal": "string",
  "parent_task_id": "uuid|null",
  "agent": "coding-agent",
  "priority": 50,
  "deadline": null,
  "context": {},
  "capabilities": ["repo.read"],
  "limits": {
    "max_steps": 20,
    "max_cost": 1.0
  }
}
```

## Result contract

```json
{
  "task_id": "uuid",
  "status": "completed",
  "summary": "string",
  "artifacts": [],
  "evidence": [],
  "metrics": {},
  "error": null
}
```
