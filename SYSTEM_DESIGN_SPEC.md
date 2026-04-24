# 📄 ISO-QA-Lab: System Design Specification Document (V 0.2)

**Project:** Multi-Agent Local AI Lab for QA Augmentation
**Standard Compliance:** ISO/IEC/IEEE 12207:2017
**Date:** 2026-04-15
**Status:** Design Complete / Ready for Scaffolding
**Target Audience:** Technical Leads, Quality Assurance Engineers

---

## 1. 🏗️ Framework Description: The Modular Multi-Agent System

The ISO-QA-Lab operates on a **modular, process-driven, multi-agent system framework**. It does not function as a single script but as an orchestrated ecosystem where specialized AI agents are responsible for discrete, well-defined process steps, mirroring the structured nature of the ISO 12207 standard.

### Core Components:

1.  **The Orchestrator (The Framework):** This layer (managed via `workflow/workflows.yaml` and guided by the `PM-Project-Planning` agent) is the central control plane. It reads the overall project goal (e.g., "Validate Feature X") and sequentially calls agents in the correct order. It handles state management, error propagation, and reporting.
2.  **The Agents (The Tools):** Each agent (e.g., `Test Generator Agent`, `Code Review Agent`) encapsulates the knowledge and logic for a specific process area (e.g., `ver-test-generator` for Test Case Generation). They operate with specialized system prompts and dedicated models (`deepseek-coder-v2:16b`, `phi4:14b`, etc.) to maximize their capability within a narrow domain.
3.  **The Data Layer (The Artifact Store):** This is the common workspace filesystem (`/home/hal2026/.openclaw/workspace/iso-qat-lab/`). All inputs, intermediate results, final reports, and baseline artifacts are stored here, ensuring traceability.
4.  **The Model Abstraction Layer (The Brains):** Managed by `config/models.yaml`, this layer allows the Orchestrator to dynamically select the best LLM for a task based on the agent's need (e.g., using `phi4:14b` for deep reasoning tasks vs. `llama3.1:8b` for fast data formatting).

### Key Design Principle: Separation of Concerns (SoC)
Every component adheres strictly to SoC. An agent is never responsible for *planning* the entire lifecycle; it is only responsible for *executing* its defined process step (e.g., the `Code Review Agent` reviews, it does not decide *when* the review happens).

---

## 2. ⚙️ Design Methodology: Mapping Engineering Standards to AI

Our methodology is to translate rigid, human-defined industry standards (like ISO 12207) into flexible, autonomous AI processes.

### Methodology: Process Decomposition & Agentification
1.  **Standard Decomposition:** We break the macro-process (e.g., "Verification") into its granular, actionable sub-processes (e.g., "Test Case Generation").
2.  **Agent Mapping:** Each sub-process becomes the dedicated remit of an Agent.
3.  **Prompt Engineering:** The Agent's system prompt (`prompt-system.md`) is meticulously designed not just to *describe* the task, but to *enforce* the methodology of the standard (e.g., forcing the Agent to always consider risk mitigation when generating test cases).
4.  **Orchestration Layering:** The workflow scripts bind these individual capabilities together. The Orchestrator acts as the Process Manager, ensuring the correct sequence and data handover between modules.

### Methodological Strengths:
*   **Auditability:** Every decision point and process step is tied to a specific Agent and an ISO clause, providing a perfect audit trail.
*   **Iterative Improvement:** By isolating components, we can upgrade or replace one agent (e.g., swap out `Bug Hunter Agent` for a commercial tool integration) without rewriting the entire pipeline.
*   **Scalability:** Adding support for a new standard (e.g., IEC 61508 for safety-critical systems) simply means adding a new set of agents and workflow nodes, rather than rewriting the core logic.

---

## 3. 📊 Data Flow: The Lifecycle Traceability Path

This details the flow of data artifacts, ensuring **end-to-end traceability** as mandated by modern quality standards.

| Phase / ISO Process | Input Artifacts | Agent Responsible | Action Taken | Output Artifacts | Traceability Link |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Acquisition** | Requirements Docs, User Stories, Stakeholder Interviews | `acq-requirements-parser` | Interpretation, Structuring, Gap Analysis | Structured Requirements Spec (`*.req`) | $\text{Req Spec} \to \text{All Tests}$ |
| **Planning/Setup** | $\text{Structured Requirements Spec}$ | `pm-project-planning` | Work breakdown, Resource estimation, Timeline creation | Project Plan (`*.plan`), Test Strategy | $\text{Plan} \to \text{Workload}$ |
| **Test Design** | $\text{Structured Requirements Spec}, \text{Project Plan}$ | `Test Generator Agent` | Generates functional, negative, performance test cases. | Test Case Set (`*.testcases.json`), Test Data Fixtures (`*.data`) | $\text{Test Cases} \to \text{Execution}$ |
| **Execution** | $\text{Test Case Set}, \text{Test Data}, \text{Env Config}$ | `Test Executor Agent` | Runs automated suites, captures state and logs. | Raw Test Results (`*.raw.json`), Screenshots, Logs | $\text{Raw Results} \to \text{Analysis}$ |
| **Analysis** | $\text{Raw Test Results}, \text{History Logs}$ | `Analytics Agent` | Calculates metrics (Pass Rate, Coverage), detects trends, identifies anomalies. | Metrics Report (`*.metrics.json`), Trend Analysis | $\text{Metrics} \to \text{Review/Report}$ |
| **Defect Finding** | $\text{Raw Test Results}, \text{Error Logs}$ | `Bug Hunter Agent` | Root cause analysis, vulnerability discovery, reproduction documentation. | Bug Report (`*.bug.yaml`), Severity Rating | $\text{Bugs} \to \text{Code Fixes}$ |
| **Code Remediation** | $\text{Bug Report}, \text{Test Code}$ | `Code Review Agent` | Suggests fixes, enforces best practices, validates fix completeness. | Code Fix Suggestions, Updated Test Snippets | $\text{Fixes} \to \text{New Code Baseline}$ |
| **Regression** | $\text{New Code Baseline}, \text{Old Baseline}$ | `Regression Agent` | Re-runs core tests to ensure fix safety and stability. | Regression Impact Report (`*.impact`) | $\text{Impact} \to \text{Validation}$ |
| **Validation** | $\text{Impact Report}, \text{User Feedback}$ | `val-user-acceptance` | Verifies solution meets business intent, not just technical specs. | UAT Sign-off Document | $\text{Sign-off} \to \text{Completion}$ |
| **Reporting** | $\text{All Artifacts}$ | `Documentation Agent` | Aggregates findings into formal reports (Executive Summary, Technical Report). | Final Report (`*.pdf`/`.md`) | $\text{Completion} \to \text{Knowledge Base}$ |

---

## 4. 🔮 Future Refinement Steps & Options

To move from a robust *design* to a production-grade *system*, the following enhancements are critical:

### A. Agent Definition Refinement (Prompt Level)
1.  **Tool Calling Synthesis:** Integrate external tool definitions directly into agent prompts. Instead of the agent *knowing* it has a `read` tool, the prompt should mandate: *"If you require external data not present in the initial context, you MUST output a structured tool-call JSON payload."*
2.  **Multi-Agent Consensus:** For high-stakes tasks (e.g., "Is this bug critical?"), implement a voting mechanism where 2 or more agents must agree, passing the consensus result to the Orchestrator.
3.  **State Persistence Hooks:** Enhance prompts to explicitly manage memory checkpoints: *"Before concluding, save all intermediate findings to the designated artifact directory before proceeding to the next step."*

### B. Data Flow & Integration Options
1.  **Structured Data Input:** Move away from reading Markdown files for inputs. Implement dedicated parsers (e.g., a `Jira_Client` agent) that ingest data via structured API calls (JSON/XML) directly into the execution flow.
2.  **Live Feedback Loop:** Implement a continuous feedback loop where the `Documentation Agent` doesn't just *write* reports, but also triggers mini-reviews in the `Bug Hunter Agent` based on the report's findings ("Review these 5 findings, and generate a new test case for each").
3.  **Visualization Layer:** Build a dedicated `dashboard-agent` that consumes all metrics JSONs and outputs a read-only dashboard view (e.g., a simple hosted embed).

### C. Operational & Scope Options
1.  **Advanced Testing:** Integrate dedicated agents for non-functional areas:
    *   `performance-agent`: Uses specialized load-testing tools (e.g., JMeter scripts via `exec`) and feeds results to `Analytics Agent`.
    *   `security-policy-agent`: Compares generated code against a codified internal security policy.
2.  **Versioning & Baselining:** Integrate formal Git/SCM hooks. The `Regression Agent` must not only report regressions but must also automatically propose a Git branch merge request with the relevant build/test logs attached.

***

This document serves as the comprehensive blueprint. We have successfully mapped our project to the industry standard, defined the roles, and mapped the entire data pipeline. The next actionable step, once resources permit, is to move to **Phase 1: Scaffolding and Smoke Testing**.