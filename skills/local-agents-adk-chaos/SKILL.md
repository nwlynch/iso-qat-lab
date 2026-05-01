---
name: local-agents-adk-chaos
description: >
  This skill should be used when the user wants to test the robustness of an agent
  by simulating failure conditions, network partitions, or resource exhaustion.
  It is the QA process for stress-testing the agent's failure handling logic.
  Covers state corruption, network latency injection, simulated service downtime,
  and resource throttling detection.
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

# ADK Chaos Testing & Resilience Validation

> **Principle:** Assume failure. An agent that cannot fail gracefully is not production-ready. All critical workflows MUST pass chaos testing.

## Core Concepts

Chaos Engineering is the discipline of experimenting on a system to build confidence in its capability to withstand failure. For local AI labs, this means systematically breaking things to see how the agent responds.

### 1. Failure Modes to Test

| Failure Mode | Description | Diagnostic Output | Mitigation Strategy |
| :--- | :--- | :--- | :--- |
| **Network Partition** | The agent cannot reach a required service (e.g., simulated Auth Service). | Timeouts, "Connection Refused." | Implement **Retry Logic** with exponential backoff and graceful fallbacks (e.g., use cached credentials). |
| **Resource Exhaustion** | The agent runs out of allocated memory or CPU time during complex reasoning. | Out-of-Memory (OOM) or execution time exceeding set limits. | Implement **Circuit Breakers** (stop execution if state diverges too much or computation time exceeds N). |
| **State Corruption** | An intermediary tool writes malformed or incomplete data (e.g., a partial JSON). | Schema validation errors, unexpected field types. | **Schema Validation** at every data handoff point; implement checksums on artifacts. |
| **Unexpected Payload** | The agent receives an input it was not designed for (e.g., a command instead of text). | Misinterpretation of intent. | Implement a **Guardrail/Schema Check** at the very start of the processing pipeline. |

### 2. Implementing Resilience in Agents

The key to resilience is making failure paths explicit, not just hoping they don't happen.

*   **Tool Design:** Every tool must have an explicit `try...except` block that catches common failure types (Network, File IO, Schema mismatch) and returns a structured error object, rather than crashing.
*   **Agent Instructions:** The agent's primary instruction must contain a "Failure Handling Protocol": *"If any step fails, do not panic. Instead, attempt the fallback mechanism outlined in the preceding steps."*

### 3. Local Chaos Runner Utility

This skill provides the wrapper to run the tests:

```bash
# Run a full suite test suite
agents-cli chaos run --suite "core_workflow" --config-file "chaos_config.yaml"

# Test a single failure mode on one specific agent
agents-cli chaos run --agent qa-report-generator --failure-mode "network_partition" --target-tool "get_test_results"
```

**Important Configuration:** The `chaos_config.yaml` defines the failure profile:
```yaml
failure_profile:
  - type: network_partition
    target_service: "local_metrics_db"
    delay_ms: 500 
    failure_duration_ms: 2000 
  - type: resource_throttling
    target_resource: "CPU"
    throttle_level: "high"
    duration_ms: 5000
```

---

## Related Skills

- `/local-agents-adk-workflow` — Development workflow, coding guidelines, and operational rules
- `/local-agents-adk-code` — ADK Python API quick reference for writing agent code
- `/local-agents-adk-scaffold` — Project creation and enhancement with `agents-cli scaffold create` / `scaffold enhance`
- `/local-agents-adk-eval` — Evaluation methodology, evalset schema, and the eval-fix loop
- `/local-agents-adk-observability` — Local tracing, logging, and monitoring for debugging agent behavior
- `/local-agents-adk-publish` — Local Gemini Enterprise registration
- `/local-agents-adk-deploy` — Deployment targets, CI/CD pipelines, and production workflows
