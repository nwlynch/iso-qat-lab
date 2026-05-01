---
name: local-agents-adk-observability
description: >
  This skill should be used when the user wants to "set up tracing",
  "monitor my ADK agent", "configure logging", "add observability",
  "debug local agent traffic", or needs guidance on monitoring deployed
  agents.
  Covers local tracing, logging, and monitoring techniques, analyzing
  agent execution traces and system logs.
  Part of the local ADK skills suite.
metadata:
  author: Local Ollama Team
  license: Apache-2.0
  version: 1.0.0
  requires:
    bins:
      - agents-cli
    install: "uv tool install local-agents-cli"
---

# Local Agent Monitoring & Observability

> **Purpose:** To provide insights into how an agent runs in a private, local environment, replicating the best practices of commercial observability suites but using only local tools (e.g., local logs, file system monitoring, local database querying).

## Local Monitoring Tools

Since we are isolated from cloud providers, monitoring relies on three primary mechanisms:
1.  **Local Logging/CLI Tools:** The primary way to view execution errors and traces.
2.  **File System Artifacts:** Agents must explicitly write key states, logs, and metrics to defined directories.
3.  **In-Process Hooks:** Using `before_agent_callback` hooks (see `/local-agents-adk-code`) to capture context data before the LLM call.

### 1. Tracing (The "How" and "Why")

**Goal:** To track the sequence of events within a single agent turn.
**Local Method:** Agents must be designed to log the start and end of each tool call, reasoning step, and model query.
**Tool:** Use `local_logging_tool` (a simulated CLI tool) to query historical, structured logs:
```bash
# Example query for local logs
local_logging_tool read "resource.type=local_engine_trace AND resource.labels.service_name=SERVICE" --project=PROJECT --limit=50 --format="table(timestamp,severity,textPayload)"
```
**Key Concept:** Always check for sequential calls. If Tool A runs, and then the agent calls Tool B, the logs must show A's completion *before* B's initiation.

### 2. Metrics & Logging (The "What")

**Goal:** To quantify performance (time, cost, success rate) and record operational details.
**Local Method:**
*   **Metric Logging:** Agents should write JSON/YAML files to the `results/metrics/` directory upon completion.
*   **Log Generation:** Use the `local_logging_tool` to query structured logs.
**Example Log Data:**
```json
{
  "timestamp": "2026-05-01T17:42:00Z",
  "level": "INFO",
  "source": "agent.main",
  "message": "Agent successfully completed full cycle."
}
```

### 3. Code Artifact Analysis (The "Where")

When debugging, always start by inspecting the agent's working files.
*   **`__pycache__`:** Look for compiled artifacts or temporary state files.
*   **`results/logs/`:** Check for raw, unparsed tool outputs or error dumps from underlying libraries.

---

## Common Debugging Workflow

When an agent fails unexpectedly:
1. **Check Logs:** Use `local_logging_tool` to find the timestamp of the failure.
2. **Reproduce:** Run the exact input prompt one-off with `agents-cli run "prompt"` to isolate the bug.
3. **Inspect:** Review the relevant file in the `/qa-lab/` directory to see the code that handles that specific step.
4. **Fix & Re-Test:** Use `/local-agents-adk-code` and then re-run evaluation with `/local-agents-adk-eval`.

## Related Skills

- `/local-agents-adk-workflow` — Development workflow, coding guidelines, and operational rules
- `/local-agents-adk-code` — ADK Python API quick reference for writing agent code
- `/local-agents-adk-scaffold` — Project creation and enhancement with `agents-cli scaffold create` / `scaffold enhance`
- `/local-agents-adk-eval` — Evaluation methodology, evalset schema, and the eval-fix loop
- `/local-agents-adk-deploy` — Deployment targets, CI/CD pipelines, and production workflows
- `/local-agents-adk-publish` — Local Gemini Enterprise registration
