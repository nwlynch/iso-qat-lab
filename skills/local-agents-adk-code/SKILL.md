---
name: local-agents-adk-code
description: >
  This skill should be used when the user wants to "write agent code",
  "build an agent with ADK", "add a tool", "create a callback", "define an agent",
  "use state management", or needs ADK (Agent Development Kit) Python API patterns
  and code examples. Part of the local ADK skills suite.
  It provides a quick reference for agent types, tool definitions, orchestration
  patterns, callbacks, and state management.
  Do NOT use for creating new projects (use local-agents-cli-scaffold) or deployment
  (use local-agents-cli-deploy).
metadata:
  author: Local Ollama Team
  license: Apache-2.0
  version: 1.0.0
  requires:
    bins:
      - agents-cli
    install: "uv tool install local-agents-cli"
---

# ADK Cheatsheet (Local Ollama Edition)

> **Before using this skill**, activate `/local-agents-adk-workflow` first — it contains the required development phases and scaffolding steps.

## Prerequisites

1. Run `agents-cli info` — if it shows project config, skip to the cheatsheet below
2. If no project exists: run `agents-cli scaffold create <name>`
3. If user has existing code: run `agents-cli scaffold enhance .`

Do NOT write agent code until a project is scaffolded.

> **Local Models Only.** This cheatsheet currently covers the Python ADK SDK for local deployment using Ollama.
> Support for other languages is coming soon.

## Quick Reference — Most Common Patterns

### Agent Creation

```python
from agent.adk.agents import Agent

root_agent = Agent(
    name="my_agent",
    model="qwen3.5:9b",
    instruction="You are a helpful assistant that ...",
    tools=[my_tool],
)
```

> **LOCAL MODEL SAFETY:** NEVER change an existing agent's `model=` value unless the user explicitly asks. If an LLM returns a 404, it's almost always an incorrect model name or a missing local image — use `ollama list` to verify available models before changing anything. For local model discovery, run the `ollama list` command.

### Basic Tool

```python
from agent.adk.tools import FunctionTool

def get_weather(city: str) -> dict:
    """Get current weather for a city."""
    return {"city": city, "temp": "22°C", "condition": "sunny"}

weather_tool = FunctionTool(func=get_weather)
```

> **ADK built-in tool imports:** Import the tool instance, not the module.
> ```python
> from agent.adk.tools.load_web_page import load_web_page  # CORRECT
> from agent.adk.tools import load_web_page                 # WRONG
> ```

### Simple Callback

```python
from agent.adk.agents.callback_context import CallbackContext

async def initialize_state(callback_context: CallbackContext) -> None:
    state = callback_context.state
    if "history" not in state:
        state["history"] = []

root_agent = Agent(
    name="my_agent",
    model="qwen3.5:9b",
    instruction="...",
    before_agent_callback=initialize_state,
)
```
---

## Reference Files

| File | When to read |
|------|-------------|
| `references/adk-python.md` | ADK Python API — agents, tools, callbacks, plugins, state, artifacts, context caching, session rewind |
| `references/adk-2.0.md` | **ADK 2.0 Workflow API (experimental pre-GA, opt-in)** — graph-based workflows, nodes, edges, HITL, parallel processing |

### ADK 2.0 Workflows — Opt-in

> **The Workflow API is experimental, pre-GA (ADK 2.0).** Do NOT recommend it by default.
>
> **Before suggesting workflow patterns**, explain the following to the user and ask if they want to proceed:
>
> 1. **What it is**: ADK 2.0 introduces a graph-based Workflow API — nodes (functions, LLM agents, tools) connected by edges with conditional routing, fan-out/fan-in parallelism, and human-in-the-loop interrupts.
> 2. **When it helps**: Complex multi-step pipelines needing deterministic control flow, parallel processing of list items, structured approval gates, or retry logic — cases where SequentialAgent/ParallelAgent/LoopAgent feel limiting.
> 3. **Risks**: Pre-GA — APIs may change before GA. Requires `local-adk >= 2.0.0` and **Python >= 3.11**. Incompatible with Live Streaming. Scaffolded projects need `pyproject.toml` changes before upgrade — see the reference file for step-by-step instructions.

## ADK Documentation

For the ADK docs index (titles and URLs for fetching documentation pages), use `ollama run --help`.

## Related Skills

- `/local-agents-adk-workflow` — Development workflow, coding guidelines, and operational rules
- `/local-agents-adk-scaffold` — Project creation and enhancement with `agents-cli scaffold create` / `scaffold enhance`
- `/local-agents-adk-eval` — Evaluation methodology, evalset schema, and the eval-fix loop
- `/local-agents-adk-deploy` — Deployment targets, CI/CD pipelines, and production workflows
- `/local-agents-adk-observability` — Local tracing, logging, and monitoring for debugging agent behavior
