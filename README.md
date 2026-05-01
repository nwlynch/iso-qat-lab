# 🤖 ISO-QA-Lab: Multi-Agent AI Testing Platform

**Mission:** Build a local, private, and highly efficient multi-agent AI lab using Ollama-based LLMs. This platform is designed to guide a Quality Assurance company through a smooth migration from manual testing to advanced, AI-assisted enterprise workflows.

**Goal:** To make the QA team significantly more efficient and to establish a robust, verifiable, and automated infrastructure for software quality assurance.

---

## 💡 1. Project Overview & Purpose

The ISO-QA-Lab is a holistic, multi-agent system built to mimic and enhance professional software development life cycle (SDLC) processes. By automating various QA tasks—from requirement parsing to bug hunting and report generation—we aim to achieve a marked reduction in manual testing time and increase overall test coverage (Target: >80%).

**Key Principle:** Augmentation, not replacement. The system enhances the existing team's skills, making them more effective.

## 📐 2. Architecture: The Agent Ecosystem

The lab operates around specialized, functional agents, each designed to manage a specific phase of the QA cycle.

### 🔬 Agent Roles & Capabilities:

| Agent | Purpose | Key Tasks |
| :--- | :--- | :--- |
| **🧬 Test Generator** | Converts abstract requirements into concrete test assets. | Parses user stories/acceptance criteria, generates comprehensive, edge-case-driven test cases (Selenium/Playwright/Jest format). |
| **🤖 Test Executor** | Executes the generated tests and captures raw data. | Runs test cases, captures detailed screenshots, logs, durations, and metrics. |
| **📊 Analytics Agent** | Interprets raw test results into actionable insights. | Calculates pass/fail rates, identifies flaky tests, generates trend reports, and suggests process improvements. |
| **🔍 Code Review Agent** | Provides expert-level software quality feedback. | Reviews Pull Requests (PRs), identifies potential bugs, suggests test improvements, and checks for security/performance concerns. |
| **🐛 Bug Hunter Agent** | Proactively searches for weaknesses and flaws. | Generates fuzzing test cases, attempts unusual input combinations, and explores state machine boundaries. |
| **📋 Regression Agent** | Ensures stability across iterations. | Runs the full regression suite automatically, detects new regressions, and updates the established test baseline. |
| **📝 Documentation Agent** | Maintains and centralizes knowledge. | Generates test documentation, creates final test run reports, updates wikis, and tracks overall test coverage. |

### 🌐 Workspace Organization:

All agents operate within a structured directory reflecting the workflow:
```
/qa-lab/
├── agents/ # Core logic modules for each agent
├── tests/ # Standardized test files (unit, e2e, etc.)
├── results/ # All output artifacts (reports, logs, metrics)
├── config/ # Reusable configuration files (model settings, framework versions)
└── docs/ # High-level strategy documents and wikis
```

## 📜 3. Methodology: ISO 12207:2017 Compliance

The lab's workflow is strictly governed by the processes defined in **ISO/IEC/IEEE 12207:2017** to ensure formal quality assurance across the entire lifecycle.

The agents are mapped to the official life cycle processes:

*   **Acquisition:** Requirements gathering and input parsing.
*   **Project Management:** Planning, risk management, and resource estimation.
*   **Product Management:** Tracking product lifecycle stages.
*   **Verification (Testing):** Core testing activities (Test Generator, Executor, Analytics, Code Review, Regression).
*   **Validation:** Ensuring the product meets user needs (UAT).
*   **Quality Assurance:** Auditing and continuous improvement (Bug Hunter, Quality Assurance Agent).
*   **Configuration Management:** Managing baselines and configuration items.
*   **Operation Support/Maintenance:** Monitoring and sustaining the product in the field.

## 🛠️ 4. Getting Started & Configuration

### 🚀 Quick Start Steps:

1.  **Prerequisites:** Ensure Ollama is running and the required models (e.g., `qwen3.5:9b`) are pulled locally.
2.  **Initialize:** Use the dedicated workflow script to set up the initial context.
3.  **Run Full Cycle:** Execute the main orchestration script to begin the QA process.

```bash
# Example: Set up environment variables for a specific run
export QA_VERBOSE=1 # Enables detailed status output for all agents
export QA_MODEL=qwen3.5:9b # Model override
export QA_TIMEOUT=600 # Agent timeout in seconds

# Start the full lifecycle workflow
./workflow/lifecycle.sh
```

### ℹ️ Environment Variables:

┌────────────┬────────────────────────────────────────────────┬───────────────────────────┐
│ Variable │ Purpose │ Example │
├────────────┼────────────────────────────────────────────────┼───────────────────────────┤
│ QA_VERBOSE │ Enables detailed status/logging. │ export QA_VERBOSE=1 │
├────────────┼────────────────────────────────────────────────┼───────────────────────────┤
│ QA_MODEL │ Allows overriding the LLM used by agents. │ export QA_MODEL=llama3:8b │
├────────────┼────────────────────────────────────────────────┼───────────────────────────┤
│ QA_TIMEOUT │ Sets a maximum time limit for agent execution. │ export QA_TIMEOUT=300 │
└────────────┴────────────────────────────────────────────────┴───────────────────────────┘