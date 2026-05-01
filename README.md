# 🧪 ISO-QA-Lab: Local AI Testing Platform

**Project Status:** ✅ **Completed and Validated (Version 1.0.0)**
**Goal:** To build a fully functional, self-contained, and secure Multi-Agent AI testing lab capable of migrating manual QA processes to an automated, local AI-assisted enterprise workflow.

**🚨 SECURITY & OPERATIONAL WARNING:**
This platform is designed to run **100% locally** using Ollama-based LLMs. It has **zero external dependencies** on cloud services (Google Cloud, Gemini, Vertex AI, etc.). Never attempt to run this code on a public cloud endpoint; it must run within a controlled, private environment.

---

## 🏛️ Architecture Overview (The Local Stack)

The system operates on a unified, local architecture governed by the `agents-cli` tool and the core `qwen3.5:9b` model.

*   **LLM Engine:** Ollama (`qwen3.5:9b`).
*   **Orchestration:** The `agents-cli` workflow.
*   **Knowledge Base:** Local file system for all test artifacts, logs, and metrics.

The system relies on seven localized, self-contained skills, which all point to local APIs and services.

---

## 🧱 Core Components (The Local Skill Suite)

The core logic is contained within the `local-agents-adk-*` skills. Each skill provides a fully localized, self-contained module for a specific QA task:

1.  `/local-agents-adk-scaffold`: Project scaffolding and structural setup.
2.  `/local-agents-adk-code`: ADK Python API reference for writing agent logic.
3.  `/local-agents-adk-eval`: The evaluation methodology (Eval-Fix Loop) for ensuring code quality.
4.  `/local-agents-adk-chaos`: Stress-tests the agent by simulating network loss, memory exhaustion, and other failure modes.
5.  `/local-agents-adk-observability`: Tools for monitoring local agent traces, logs, and performance metrics.
6.  `/local-agents-adk-deploy`: Workflow for containerizing and deploying the agent to a local service endpoint.
7.  `/local-agents-adk-publish`: Registers the agent with the local "Local Enterprise" directory, making it discoverable by other local agents.

## ⚙️ The Operational Workflow (How to Run It)

This process must be run sequentially for a new agent to achieve final maturity.

1.  **Scaffold:** Create the project structure.
    `agents-cli scaffold create [project-name]`
2.  **Code:** Develop and implement tools and core logic (`/local-agents-adk-code`).
3.  **Test (Success):** Run basic evaluation to ensure happy path functionality.
    `agents-cli eval run`
4.  **Fix:** Iterate the code based on evaluation results (Eval-Fix Loop).
5.  **Test (Failure):** Run chaos tests to prove resilience.
    `agents-cli chaos run`
6.  **Deploy:** Make the agent accessible via a local endpoint.
    `agents-cli deploy`
7.  **Publish:** Register the working agent in the local directory.
    `agents-cli publish local-enterprise`

---

## 🚀 Project Success Criteria

*   **Efficiency:** The automated flow demonstrably reduces manual testing time by over 50%.
*   **Coverage:** The system can systematically test for known gaps using the Chaos skill.
*   **Quality:** All artifacts are validated through the local Eval-Fix loop.
*   **Security:** The workflow mandates local authentication before accessing test metrics.

---
*This README serves as the official Project Definition for the Local QA Lab. All runs must be executed using the local development environment.*