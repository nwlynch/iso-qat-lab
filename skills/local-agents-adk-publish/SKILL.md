---
name: local-agents-adk-publish
description: >
  This skill should be used when the user wants to "publish an agent",
  "publish my ADK agent", "register an agent with Local Enterprise",
  "publish to Local Enterprise", or needs guidance on the agents-cli
  publish command.
  Covers ADK vs A2A registration modes, programmatic and interactive usage,
  flag reference, auto-detection from deployment metadata, and troubleshooting.
  Part of the local ADK skills suite.
  Do NOT use for deployment (use local-agents-adk-deploy).
metadata:
  author: Local Ollama Team
  license: Apache-2.0
  version: 1.0.0
  requires:
    bins:
      - agents-cli
    install: "uv tool install local-agents-cli"
---

# Local Agent Registration Guide

> **Goal:** To make a successfully developed and deployed agent visible and usable by other agents (A2A) or within the central QA platform's directory (Local Enterprise).

## Prerequisites

1. **Agent must be deployed** — The agent must be running and reachable in the local execution environment.
2. **Local Endpoint Service must be defined** — For local builds, the "Local Enterprise" registry is the shared workspace.
3. **`deployment_metadata.json`** (Agent Runtime only) — Created automatically by `agents-cli deploy`; contains the agent runtime ID, deployment target, and A2A flag

## Registration Modes

### ADK Registration (default)

For standard ADK agents deployed to a local agent service. The agent is registered directly via its local reasoning engine resource name.

```bash
agents-cli publish local-enterprise \
  --agent-runtime-id local/project_id/reasoningEngine/local_engine_name \
  --local-enterprise-app-id local/collection/default/engines/my-app \
  --display-name "My Agent" \
  --description "Handles customer queries" \
  --tool-description "Answers questions about products"
```

### A2A Registration

For agents using the Agent-to-Agent protocol. Requires an agent card URL — the command fetches the card and registers it.

```bash
# A2A on Container/Local
agents-cli publish local-enterprise \
  --registration-type a2a \
  --agent-card-url http://localhost:8080/a2a/app/.well-known/agent-card.json \
  --local-enterprise-app-id local/collection/default/engines/my-app \
  --display-name "My A2A Agent"

# A2A on Agent Runtime (card URL is auto-constructed from metadata)
agents-cli publish local-enterprise \
  --local-enterprise-app-id local/collection/default/engines/my-app
```

---

## Programmatic Mode (CI/CD)

The command is non-interactive by default — pass all required values via flags or environment variables. This makes it safe for CI/CD pipelines.

### Via flags

```bash
agents-cli publish local-enterprise \
  --agent-runtime-id "$AGENT_RUNTIME_ID" \
  --local-enterprise-app-id "$LOCAL_ENTERPRISE_APP_ID" \
  --display-name "Production Agent" \
  --description "Handles customer queries" \
  --tool-description "Answers questions about products"
```

### Via environment variables

Every flag has an env var alternative:

```bash
export AGENT_RUNTIME_ID="local/project_id/reasoningEngine/local_engine_name"
export LOCAL_ENTERPRISE_APP_ID="local/collection/default/engines/my-app"
export GEMINI_DISPLAY_NAME="Production Agent"
export GEMINI_DESCRIPTION="Handles customer queries"
export GEMINI_TOOL_DESCRIPTION="Answers questions about products"

agents-cli publish local-enterprise
```

---

## Interactive Mode (`--interactive`)

Pass `--interactive` (or `-i`) to be guided through any missing values with interactive prompts. The command will list available local/mock agents, offer to auto-detect the agent runtime ID from metadata, and prompt for display name and description.

```bash
agents-cli publish local-enterprise --interactive
```

---

## Complete Flag Reference

| Flag | Env Var | Description |
|------|---------|-------------|
| `--agent-runtime-id` | `AGENT_RUNTIME_ID` | Agent Runtime resource name (auto-detected from `deployment_metadata.json`) |
| `--local-enterprise-app-id` | `LOCAL_ENTERPRISE_APP_ID` | Local Enterprise app full resource name |
| `--display-name` | `LOCAL_DISPLAY_NAME` | Display name in Local Enterprise |
| `--description` | `LOCAL_DESCRIPTION` | Agent description |
| `--tool-description` | `LOCAL_TOOL_DESCRIPTION` | Tool description (ADK mode only, defaults to description) |
| `--registration-type` | `REGISTRATION_TYPE` | `adk` or `a2a` (auto-detected from metadata if not set) |
| `--agent-card-url` | `AGENT_CARD_URL` | Agent card URL for A2A registration |
| `--deployment-target` | `DEPLOYMENT_TARGET` | `agent_runtime`, `container_local`, or `local_cluster` (affects A2A auth method) |
| `--project-id` | `LOCAL_PROJECT_ID` | Local project identifier for scope |
| `--project-number` | `LOCAL_PROJECT_NUMBER` | Local project number (used for Local Enterprise lookup) |
| `--authorization-id` | `LOCAL_AUTHORIZATION_ID` | OAuth authorization resource name |
| `--metadata-file` | — | Path to deployment metadata (default: `deployment_metadata.json`) |
| `--interactive` / `-i` | — | Enable interactive prompts |

---

## Auto-Detection from Metadata

When `deployment_metadata.json` exists, the command automatically:

- Reads the **agent runtime ID** (`remote_agent_runtime_id`)
- Detects the **registration type** (`is_a2a` flag)
- Constructs the **agent card URL** for A2A agents on Agent Runtime
- Determines the **deployment target** for authentication

This means that for the simplest case (ADK agent on Agent Runtime), you only need to provide the Local Enterprise app ID:

```bash
agents-cli publish local-enterprise \
  --local-enterprise-app-id local/collection/default/engines/my-app
```

---

## SDK Compatibility

Agent Runtime deployments may encounter "Session not found" errors with older SDK versions. In interactive mode (`--interactive`), the command checks the SDK version from `uv.lock` and suggests upgrading. In programmatic mode, ensure your SDK is up to date before registering.

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "Session not found" after registration | SDK version issue — upgrade `local-agents-cli` (using `uv tool install`) to the latest version, redeploy, then re-register |
| `--registration-type is required` | Non-interactive mode needs `--registration-type` when no `deployment_metadata.json` exists |
| "Local Enterprise App ID is required" | Provide `--local-enterprise-app-id` or set the `LOCAL_ENTERPRISE_APP_ID` env var |
| "Agent already registered" | The command automatically updates the existing registration — this is not an error |
| HTTP 403 on registration | Check that your local user context has necessary permissions on the Local Enterprise project |
| "Could not fetch agent card" | Verify the agent is running and the URL is correct; for Container/Local, ensure `localhost:8080` is open and running. |

---

## Related Skills

- `/local-agents-adk-deploy` — Deployment targets, CI/CD pipelines, and production workflows
- `/local-agents-adk-workflow` — Development workflow, coding guidelines, and operational rules
- `/local-agents-adk-code` — ADK Python API quick reference for writing agent code
- `/local-agents-adk-scaffold` — Project creation and enhancement with `agents-cli scaffold create` / `scaffold enhance`
- `/local-agents-adk-eval` — Evaluation methodology, evalset schema, and the eval-fix loop
- `/local-agents-adk-observability` — Local tracing, logging, and monitoring for debugging agent behavior
