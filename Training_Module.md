# 🎓 QA Workflow Training Module: From Requirement to Report

**Target Audience:** Quality Assurance Team Members
**Goal:** To guide team members through the complete, localized, AI-assisted test lifecycle, replacing manual report generation and manual workflow steps.
**Prerequisite Knowledge:** Basic understanding of the features being tested and access to the Local Ollama/ADK Terminal.

---

## 🌐 Introduction: The New QA Workflow

Our new system, the Local AI Testing Lab, is designed to automate the entire flow, ensuring high quality, detailed tracking, and mandatory security checks, all running on our private, local Ollama infrastructure.

**The old process (Manual $\rightarrow$ Report) is replaced by the automated process (Requirement $\rightarrow$ Report).**

**Your Role:** Your expertise is now in defining the *requirements* and *analyzing the results*, not running the tests or writing the report.

---

## 🧪 Phase 0: Initiation & Scaffolding (Setup)

When a new testing feature is required, the AI team will provision the development environment.

**What you see:** A new project scaffolded using the `/local-agents-adk-scaffold` skill.
**What you do:** Review the initial scope defined in the project's `README.md`.
**What to know:** If the scaffold misses a required tool or data source, notify the AI team immediately.

## 📝 Phase 1: Defining the Test Logic (Build & Code Review)

The AI team uses the `/local-agents-adk-code` skill to write the agent's core logic. This is where the agent is given its "job."

**What you see:** The `qa-report-generator` agent initialized with specific tools (e.g., `get_test_results`).
**What you do:** Review the tools. Do the inputs/outputs match the test plan? If not, advise the AI team to modify the tool schemas.

## 🔒 Phase 2: Security & Authentication (Mandatory Gate)

**[NEW CRITICAL STEP]**
The agent *cannot* proceed to any sensitive action (like fetching test results) without proving identity.

**Workflow:**
1.  The agent automatically initiates the local authentication check (`qa-analyst`).
2.  **If Authentication Fails:** The process stops immediately, and an error message is displayed, requiring a credentials review before proceeding. *This is a security feature.*

## 🚦 Phase 3: Simulation & Evaluation (The Safety Check)

Before we consider the agent "finished," we must prove it works under stress.

**A. Success Testing (`/local-agents-adk-eval`):**
We run the `eval` skill to validate standard paths (e.g., "Pass/Fail scenario"). This ensures the *ideal* path works.

**B. Chaos Testing (`/local-agents-adk-chaos`):**
**This is the most important step.** We intentionally break the system (e.g., simulate a network outage).
*   **What to look for:** Does the agent crash, or does it return a graceful, structured error message (like "Connection failed, retrying...")?
*   **Expected:** The agent must recover or report the failure *politely and helpfully*.

## 🚀 Phase 4: Deployment & Publishing

Once the agent passes **Success Testing** AND **Chaos Testing**:

1.  **Deployment (`/local-agents-adk-deploy`):** The agent is deployed to the local service endpoint. This makes the agent available at a fixed, local address (e.g., `http://localhost:8080/qa-report-generator`).
2.  **Publication (`/local-agents-adk-publish`):** The agent is registered with the local "Local Enterprise" registry. This makes the agent discoverable by other internal AI systems, allowing other agents to call it by name.

## 📋 Final Output: The Executive Summary

After all phases pass, the final output—the polished Markdown report—is generated. This report is the single artifact you need to hand off to stakeholders, containing the summary, details, and clear next steps.

---
**🛠️ Actionable Checklist for Your Review**
1. [ ] Review `STATUS.md`: Does the current high-level plan match reality?
2. [ ] Execute `qa-report-generator`: Check Auth $\rightarrow$ Success $\rightarrow$ Report.
3. [ ] Execute `qa-report-generator` with Chaos Test: Check Auth $\rightarrow$ Fail $\rightarrow$ Graceful Recovery.
4. [ ] Confirm the report meets stakeholder needs.

**The process is now fully automated, secure, and reliable.**
