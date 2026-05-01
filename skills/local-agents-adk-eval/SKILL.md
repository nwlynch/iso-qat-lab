---
name: local-agents-adk-eval
description: >
  This skill should be used when the user wants to "evaluate an agent",
  "evaluate my ADK agent", "write an evalset", "debug eval scores",
  "compare eval results", or needs guidance on ADK (Agent Development Kit) evaluation
  methodology and the eval-fix loop.
  Covers eval metrics, evalset schema, LLM-as-judge, tool trajectory scoring,
  and common failure causes.
  Part of the local ADK skills suite.
  Do NOT use for API code patterns (use local-agents-adk-code), deployment
  (use local-agents-adk-deploy), or project scaffolding (use local-agents-adk-scaffold).
metadata:
  author: Local Ollama Team
  license: Apache-2.0
  version: 1.0.0
  requires:
    bins:
      - agents-cli
    install: "uv tool install local-agents-cli"
---

# ADK Evaluation Methodology (Local Validation)

> **CRITICAL PHASE:** Do NOT deploy or publish an agent until evaluation passes. This skill is the safety gate for quality.

## The Eval-Fix Loop

Agent development is inherently iterative. This loop is the formal, repeatable process for validating the agent's ability to meet requirements:
1. **Define Evalset:** Write a comprehensive set of test cases and edge cases covering all use paths.
2. **Run Evaluation:** Execute the tests against the current agent version.
3. **Analyze Results:** Review failure reports, identify root causes (e.g., wrong tool called, poor reasoning, unhandled state), and generate metrics.
4. **Fix Agent:** Use `/local-agents-adk-code` to refactor the agent's logic or tools.
5. **Repeat:** Go back to Step 2 until quality metrics are met.

## Core Concepts

### 1. Evalset Schema

The evalset is your single source of truth for expected behavior. It must contain:
*   **Prompt:** The user input/user story.
*   **Expected Outcome:** The ideal, correct final answer.
*   **Expected Tool Calls:** The exact sequence of tools/functions the agent must call to achieve the outcome.
*   **Metrics:** The criteria the agent will be graded against (e.g., `Did it call the right tool?`, `Was the final answer accurate?`).

### 2. Evaluation Types

| Type | Goal | Focus | Best For |
|---|---|---|---|
| **Functional** | Does the code work? | Tool output validity, function success. | Unit testing agent utilities. |
| **Behavioral** | Does the agent behave correctly? | Tool sequencing, multi-step reasoning, prompt handling. | Catching logical flaws and tool misuse. |
| **Safety** | Does the agent stay safe? | Jailbreak resistance, refusal to answer sensitive questions. | Hardening the system against abuse. |

### 3. Using LLM-as-Judge

Modern evaluation often uses a powerful LLM (like `qwen3.5:9b` in a specific role) to judge the agent's output instead of relying solely on deterministic assertions. This is crucial for subjective tasks like tone or coherence.

**LLM-as-Judge Prompting:**
Ensure your evalset includes an explicit section instructing the judging model on:
1. The persona/role of the judge.
2. The specific criteria and scoring scale (e.g., 1-5 stars).
3. The JSON format for the judge's final output.

## Tools & Metrics

When running `agents-cli eval run`, the output should provide:
*   **Pass/Fail Rate:** Overall success rate.
*   **Tool Trajectory Graph:** A visual/structured map of tool calls, highlighting deviations from the expected path.
*   **Top Failure Modes:** A summary of the most common failure reasons (e.g., "Missing state transfer," "Tool argument mismatch," "Confused persona").

## Common Failure Causes (The Pitfalls)

| Failure | Root Cause | Fix Strategy |
|---|---|---|
| **Stuck Loop** | Agent fails to recognize completion or needs more input. | Implement maximum loop attempts (e.g., 3 attempts) or force an explicit `STOP` signal. |
| **Context Overload** | Prompt context is too large, causing the LLM to forget key instructions. | Use context summarization tools or enforce strict context window partitioning. |
| **Tool Argument Mismatch** | The agent calls the tool but provides the wrong type or number of arguments. | Explicitly define tool schema and create pre-computation checks in the agent code. |
| **Regression** | A fix for one bug breaks an unrelated feature. | Keep a detailed set of "Golden Tests" that cover core functionality and run them first on every PR. |

> **Reminder:** Always profile your evaluation (e.g., once a week) against a baseline of "Golden Tests" to detect silent regressions.

---

## Related Skills

- `/local-agents-adk-workflow` — Development workflow, coding guidelines, and operational rules
- `/local-agents-adk-code` — ADK Python API quick reference for writing agent code
- `/local-agents-adk-scaffold` — Project creation and enhancement with `agents-cli scaffold create` / `scaffold enhance`
- `/local-agents-adk-deploy` — Deployment targets, CI/CD pipelines, and production workflows
- `/local-agents-adk-observability` — Local tracing, logging, and monitoring for debugging agent behavior
- `/local-agents-adk-publish` — Local Gemini Enterprise registration
