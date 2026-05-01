---
name: local-agents-adk-scaffold
description: >
  This skill should be used when the user wants to "create an agent project",
  "start a new ADK project", "build me a new agent", "add CI/CD to my project",
  "add deployment", "enhance my project", or "upgrade my project".
  Covers `agents-cli scaffold create`, `scaffold enhance`, and `scaffold upgrade`
  commands, template options, deployment targets, and the prototype-first workflow.
  Part of the local ADK skills suite.
  Do NOT use for writing agent code (use local-agents-adk-code) or deployment
  operations (use local-agents-adk-deploy).
metadata:
  author: Local Ollama Team
  license: Apache-2.0
  version: 1.0.0
  requires:
    bins:
      - agents-cli
    install: "uv tool install local-agents-cli"
---

# ADK Project Scaffolding (Local)

> **ALWAYS START HERE.** If you are building a new agent from scratch, this is your starting point. It ensures the project is properly structured for the entire local AI lifecycle.

## Workflow Entry Point

The recommended workflow for any new agent project is:
1. **Scaffold:** Use `agents-cli scaffold create <name>` to set up the project structure, basic code skeleton, and required configuration files (`pyproject.toml`, etc.).
2. **Enhance:** Use `agents-cli scaffold enhance .` to add functionality (like deploying, monitoring, or specific tools) to an existing scaffolded project.
3. **Build/Refine:** Follow the ADK guidelines in `/local-agents-adk-workflow` to write logic using `/local-agents-adk-code`.
4. **Validate:** Use `/local-agents-adk-eval` to rigorously test the agent's behavior.

## Scaffold Commands

### 1. Create (New Project)

```bash
# Creates the basic structure for a new agent project.
agents-cli scaffold create <project_name>
```

**What it creates:**
*   A dedicated project directory structure.
*   Initial boilerplate code for `main.py` and agent definition.
*   A foundational `pyproject.toml` file to manage local dependencies and local-agents-cli.

### 2. Enhance (Add Functionality)

```bash
# Adds a specific capability (e.g., deployment, monitoring) to the current project.
agents-cli scaffold enhance . --add <capability>
```

**Common Enhancement Targets:**
*   `--add deployment`: Adds boilerplate for `agents-cli deploy` and relevant deployment configs.
*   `--add observability`: Adds logging/tracing hooks for `agents-cli-observability`.
*   `--add eval`: Initializes the evaluation boilerplate and necessary test files.

### 3. Upgrade (Major Platform Changes)

```bash
# Used when upgrading the entire scaffolding pattern (e.g., from ADK 1.x to 2.x)
agents-cli scaffold upgrade . --target <version>
```

## Template Options

The scaffold process can be directed by context:

*   **`--template <type>`**: Use this to start with a specific pre-built template (e.g., `template/web_scraper` or `template/datastore_rag`).
*   **`--dev-mode`**: Sets up the project for local development, enabling local endpoints for immediate testing.
*   **`--ci-mode`**: Adds CI/CD specific files and placeholders for CI/CD pipeline integration.

## Local Development Best Practices

*   **Dependencies:** All dependencies must be listed and managed in `pyproject.toml` and installed via `uv`.
*   **Local Run:** Always test initial functionality using `agents-cli run "prompt"` inside the scaffolded directory.
*   **Never forget:** The scaffold provides the *structure*, but you must write the *logic* using `/local-agents-adk-code`.

## Project Lifecycle Summary

| Action | Goal | Command | Relevant Skills |
|:---|:---|:---|:---|
| **SETUP** | Start a new project. | `agents-cli scaffold create <name>` | `/local-agents-adk-scaffold` |
| **BUILD** | Write core logic/tools. | (Manual coding) | `/local-agents-adk-code` |
| **TEST** | Validate agent behavior. | `agents-cli eval run` | `/local-agents-adk-eval` |
| **DEPLOY** | Make agent accessible in a controlled environment. | `agents-cli deploy` | `/local-agents-adk-deploy` |
| **OBSERVE** | Monitor deployed agent performance. | `agents-cli observe` | `/local-agents-adk-observability` |
| **REFINE** | Add capability (e.g., CI/CD). | `agents-cli scaffold enhance . --add <capability>` | `/local-agents-adk-scaffold` |
