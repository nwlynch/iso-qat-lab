# 🛡️ QA Agent Lab: Local Private AI Assurance Platform

A self-contained, local-first, multi-agent development lab built to migrate Quality Assurance workflows from manual testing to highly automated, AI-assisted enterprise systems.

**Mission:** To provide a secure, privacy-preserving framework for building and testing AI agents using local, open-weights Large Language Models (LLMs) via Ollama.

---

## 🚀 💡 Core Philosophy: Local & Private First

This platform is designed to eliminate reliance on proprietary cloud APIs and services, ensuring that all sensitive project data, test cases, and agent logic remain entirely within the local, on-premises network.

## 🔬 Architecture Components

The lab is structured around several interconnected, specialized Python modules:

### 🌐 1. Agent Orchestration (`local_agents_cli.py`)
The main control layer. It manages the entire lifecycle: scaffold creation, running the test suite, calling evaluators, and simulating deployment.

### 💾 2. Persistent Memory (`mempalace_wrapper.py`)
The "institutional memory" of the lab. Instead of relying on stateless sessions, all findings are mined, stored, and retrievable.
*   **Function:** Stores verbatim conversation history, bug reports, and best practices.
*   **Benefit:** Agents can contextually check against past failures, ensuring continuous learning and preventing regression.

### 🔬 3. Evaluation & Metrics (`local_evaluator.py`)
Replaces cloud-based metrics engines. It runs the critical **LLM-as-Judge** process, systematically scoring an agent's performance against predefined test sets and generating quantitative reports.

### 🐛 4. Bug Hunter Agent (`bug_hunter_agent.py`)
The active detection unit. It goes beyond simple unit tests by:
*   **OWASP Scanning:** Generating and simulating tests for critical vulnerabilities (Injection, XSS, Auth bypass).
*   **Fuzzing:** Using the LLM to perform deep, simulated threat modeling and boundary condition testing.
*   **Reporting:** Generating executive summaries and prioritized action items for development teams.

## 🛠️ Getting Started

### Prerequisites
1.  **Python:** 3.9+
2.  **LLM Runtime:** Ollama must be running locally (e.g., `ollama serve`).
3.  **Dependencies:** `pip install -r requirements.txt` (Requires `requests`, `pydantic`, etc.)

### Setup Steps
1.  **Initialize Environment:** (Assuming the `venv` is active)
    ```bash
    source venv/bin/activate
    ```
2.  **Bootstrap the Project:**
    ```bash
    python local-agents-adk/local_agents_cli.py scaffold
    ```
3.  **Run the Full Cycle:**
    ```bash
    python local-agents-adk/local_agents_cli.py run
    ```

## 🗺️ Local Workflow Diagram

**(Conceptual Flow)**

1.  **[User Input]** $\rightarrow$ `local_agents_cli`
2.  **[Task]** $\rightarrow$ Calls `local_evaluator`
3.  **[Memory Retrieval]** $\rightarrow$ Queries `mempalace_wrapper` (Injects Context)
4.  **[Test Case Gen]** $\rightarrow$ Calls `bug_hunter_agent` (Uses `mempalace` context)
5.  **[Run & Detect]** $\rightarrow$ Simulates Agent execution
6.  **[Report]** $\rightarrow$ Writes findings to `mempalace` (Memory Commit)
7.  **[Deployment]** $\rightarrow$ Executes `simulate_deployment` (Local Container Build)

---
*Built on the principles of open-weights LLMs and advanced multi-agent coordination.*