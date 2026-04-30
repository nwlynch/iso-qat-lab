# Local Agents ADK Skill Wrapper

## Objective
This skill wrapper aims to replicate the functionality of the Google Agents CLI skill suite (`google-agents-cli-*`) using only local, open-weights LLM services (e.g., Ollama, llama.cpp).

The goal is to create a self-contained, privacy-focused multi-agent development lifecycle, eliminating all reliance on external cloud APIs (GCP, Vertex AI, etc.).

## Architecture Pillars
1.  **Local Orchestration:** All workflow control (scaffolding, deployment simulation, evaluation calls) will be managed by Python logic.
2.  **Ollama Backend:** All LLM calls (Code Generation, Reasoning, Tool Use) will route through a standardized Python client talking to the local Ollama API.
3.  **Simulated Services:** Cloud infrastructure components (like "Deployment" or "Cloud Run") will be replaced by local filesystem operations, configuration file generation, and local service emulation (e.g., running a local FastAPI server container).

## Dependencies
- `ollama`: The primary local LLM runner.
- `pydantic`: For standardized input/output schema definitions.
- `uvicorn`/`fastapi`: For serving simulated endpoints.

## Core Skills to Replace (High Level)
- `agents-cli scaffold create` -> `local_agents_cli.scaffold()`
- `agents-cli deploy` -> `local_agents_cli.deploy_simulation()`
- `agents-cli eval` -> `local_agents_cli.evaluate()`

## Development Status
*   **Status:** Phase 1 - Abstraction Layer Creation.
*   **Next Step:** Begin detailed function-by-function API replacement.