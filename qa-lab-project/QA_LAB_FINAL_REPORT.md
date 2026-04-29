# 🚀 QA Lab Project: Comprehensive System Overview (V1.0.0-alpha)

## Overview
This project establishes a multi-agent, AI-assisted local Quality Assurance (QA) laboratory. It is designed to assist the company in migrating from manual testing to an automated, AI-driven workflow. The entire process is designed to align with the standards set by **ISO/IEC/IEEE 12207:2017** throughout every stage (Requirement Analysis, Test Planning, Implementation, Validation, and Reporting).

## 🤖 Core Components: The 7 Agents
The system operates as a pipeline orchestrated by `run_qa_cycle.py`. Each agent is a specialized, modular microservice responsible for one key QA function.

### 1. 🧬 Test Generator Agent
*   **Purpose:** The system's entry point. It consumes user requirements (user stories/specs) and translates them into structured, executable test metadata.
*   **Mechanism:** Uses LLM prompting to parse natural language into machine-readable test formats (ID, Type, Framework, Priority).
*   **Input:** Natural Language Requirements.
*   **Output:** List of Test Cases (structured JSON/YAML).

### 2. 🤖 Test Executor Agent
*   **Purpose:** The active testing component. It runs the generated tests against a live application instance.
*   **Mechanism:** Utilizes **Playwright** to manage a headless browser context, executing actions (navigation, clicking, filling forms) and capturing system outputs (screenshots, logs).
*   **Input:** Test Case List.
*   **Output:** Raw Test Results (PASS/FAIL map).

### 📊 Analytics Agent
*   **Purpose:** Transforms raw pass/fail flags into business intelligence.
*   **Mechanism:** Calculates quantitative metrics: Total Tests, Pass Count, Fail Count, and Pass Rate. It also flags patterns and calculates initial severity ratings.
*   **Input:** Raw Test Results.
*   **Output:** Structured Analysis Report (Summary, Metrics, Failures).

### 🔍 Code Review Agent
*   **Purpose:** Acts as the developer feedback loop. It analyzes *why* tests failed.
*   **Mechanism:** Takes the failure report and prompts the LLM to act as a senior engineer, suggesting specific lines of code, file paths, and architectural changes needed for remediation.
*   **Input:** Failed Tests Report.
*   **Output:** Actionable Code Suggestions List.

### 🐛 Bug Hunter Agent
*   **Purpose:** Moves beyond known test cases by acting adversarially.
*   **Mechanism:** Uses failure patterns and requirements to prompt the LLM to think outside the box, generating *new, speculative* edge cases and fuzzing inputs.
*   **Input:** Requirements & Failed Tests.
*   **Output:** Critical, un-tested edge cases.

### 📋 Regression Agent
*   **Purpose:** Ensures stability. This agent runs a fixed, comprehensive suite of tests against the baseline to prove that new changes haven't broken old features.
*   **Mechanism:** Compares the current run's results against historical, known-good baselines to detect regressions.
*   **Input:** Baseline Configuration.
*   **Output:** Stability Report (Pass/Fail vs. Baseline).

### 📝 Documentation Agent
*   **Purpose:** The final compiler. It synthesizes all disparate outputs into one coherent, human-readable document.
*   **Mechanism:** Consumes the Analysis Report, Code Review suggestions, Bug Hunter findings, and Regression status to create the final markdown report.
*   **Output:** Final Report (Markdown/HTML).

---
## 📈 Execution Flow (The Cycle)
The entire process is driven by `run_qa_cycle.py` and runs in this strict order:
**Requirements $\rightarrow$ Test Generate $\rightarrow$ Test Execute $\rightarrow$ Analyze $\rightarrow$ Bug Hunt $\rightarrow$ Code Review $\rightarrow$ Regress $\rightarrow$ Document $\rightarrow$ Final Report.**

## 💾 System Dependencies
*   **LLM:** Ollama (qwen3.5:9b primary, gemma4:e4b fallback).
*   **Browser Automation:** Playwright (Chromium/Firefox/WebKit).

## 🚀 Next Milestones (Future Work)
1.  **Full Code Implementation:** Replace all `asyncio.sleep()` placeholders with actual API calls.
2.  **CI/CD Integration:** Implement automated triggers for continuous workflow testing.
3.  **Tool Integration:** Connect the system to version control (Git) and CI pipelines (GitHub Actions).

## 📜 Compliance Documentation
*   **Standard:** This architecture is mapped to process controls outlined in **ISO/IEC/IEEE 12207:2017**.
*   **Traceability:** Every stage maps directly to a required process step (e.g., Test Generation $\rightarrow$ Test Planning).
*   **Next Target:** We will establish a dedicated folder structure for mapping outputs to specific ISO clauses.
