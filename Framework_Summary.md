# ISO-QA-Lab Framework Documentation

This document details the design, methodology, and structure of the Multi-Agent QA Testing Lab, designed to comply with **ISO/IEC/IEEE 12207:2017**.

## 1. Framework Overview (The "How")

The framework is designed to automate the complex, multi-stage software lifecycle by orchestrating specialized AI agents.

*   **Orchestration Layer (OpenClaw Shell Script):** Acts as the conductor, defining the sequence of required agent interactions based on the ISO lifecycle.
*   **Agent Layer (Specialized Agents):** Specialized agents are responsible for specific tasks (e.g., Parsing requirements, Generating tests, Auditing).
*   **Communication Protocol (`AGENT_PROTOCOL.md`):** All agents communicate results in a standardized **JSON format**, ensuring that the orchestrator can reliably ingest and chain the results.
*   **Configuration Layer (`config/`):** Manages the resources (LLMs via Ollama) and operational parameters.

## 2. Design Methodology (The "Why")

The design follows a **Process-Oriented Decomposition** to map the ISO standard to the multi-agent structure:

1.  **Decomposition:** Breaking the 10 phases of the ISO standard into discrete, manageable sub-tasks.
2.  **Agent Specialization:** Assigning each sub-task to a specialized agent.
3.  **Context-Awareness:** Using the system to maintain context across steps, demonstrated by the `multi-step-agent-example.md` pattern.
4.  **Model Specialization:** Utilizing `models.yaml` to assign specialized LLMs (e.g., code models, reasoning models) to specific agent roles, optimizing for local resource constraints.

## 3. Data Flow: ISO Lifecycle Flow

The data flows sequentially through the system, transforming raw input into actionable QA artifacts:

*   **Phase 1: Acquisition (Input Gathering):** Raw Requirements & Stakeholder Feedback $\rightarrow$ Structured Requirements.
*   **Phase 2: Project Management (Planning):** Structured Requirements $\rightarrow$ Project Plan.
*   **Phase 3: Configuration (Baseline):** Plan $\rightarrow$ Baseline Settings.
*   **Phase 4: Verification (Testing):** Plan + Baseline $\rightarrow$ Test Cases $\rightarrow$ Execution $\rightarrow$ Analysis.
*   **Phase 5: Validation (Assurance):** Test Results $\rightarrow$ Validation Evidence.
*   **Phase 6: Quality Assurance (Improvement):** Audit $\rightarrow$ Bug Hunting $\rightarrow$ Improvement Plans.
*   **Phase 7: Operation & Maintenance (Sustainment):** Audit $\rightarrow$ Maintenance Logs.

## 4. Future Steps for Refinement

The framework is structurally complete. The next steps involve **implementation and iteration**:

1.  **Implement the Next Agent:** Focus on fully defining and integrating the **Project Management Agent** (`pm-project-planning/`) logic.
2.  **Implement the Execution Layer:** Begin building the robust data ingestion part of the workflow using the `sessions_spawn` mechanism to connect these modules.
3.  **Iterative Refinement:** Continuously review and update the prompt systems and configuration based on real-world testing outcomes.

---
**Goal:** Build a fully operational, multi-agent local AI lab using Ollama, demonstrating Agentic AI for enterprise QA.

**Key Principle:** The framework must be modular enough to be plugged into any external agentic methodology while maintaining a centralized, auditable structure compliant with ISO/IEC/IEEE 12207:2017.