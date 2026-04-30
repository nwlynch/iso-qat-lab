# 🛡️ QA Agent Lab: Local Private AI Assurance Platform

A self-contained, local-first, multi-agent development lab built to migrate Quality Assurance workflows from manual testing to highly automated, AI-assisted enterprise systems.

**Mission:** To provide a secure, privacy-preserving framework for building and testing AI agents using local, open-weights Large Language Models (LLMs) via Ollama.

---

## 📐 Repository Location Note
**The entire project source code resides at:** `/home/nwlynch/src/iso-qat-lab/qa-lab/`

## 🚀 💡 Core Philosophy: Local & Private First
This platform is designed to eliminate reliance on proprietary cloud APIs and services, ensuring that all sensitive project data, test cases, and agent logic remain entirely within the local, on-premises network.

## 🔬 Architecture Components
The lab is structured around several interconnected, specialized Python modules:

### 🌐 1. Agent Orchestration (`local_agents_cli.py`)
The main control layer. It manages the entire lifecycle: scaffold creation, running the test suite, calling evaluators, and simulating deployment.

### 💾 2. Persistent Memory (`mempalace_wrapper.py`)
The "institutional memory" of the lab. It stores verbatim conversation history, bug reports, and best practices.
*   **Function:** Stores the knowledge base, allowing agents to check past findings, ensuring continuous learning and preventing regression.

### 🔬 3. Evaluation & Metrics (`local_evaluator.py`)
Replaces cloud-based metrics engines. It runs the critical **LLM-as-Judge** process, systematically scoring an agent's performance against predefined test sets and generating quantitative reports.

### 🐛 4. Bug Hunter Agent (`bug_hunter_agent.py`)
The active detection unit. It goes beyond simple unit tests by:
*   **OWASP Scanning:** Generating and simulating tests for critical vulnerabilities (Injection, XSS, Auth bypass).
*   **Fuzzing:** Using the LLM to perform deep, simulated threat modeling and boundary condition testing.
*   **Reporting:** Generating executive summaries and prioritized action items for development teams.

## 🛠️ Getting Started
### Prerequisites
1. **Python:** Python 3.9+
2. **LLM Runtime:** Ollama must be running locally (e.g., `ollama serve`).
3. **Dependencies:** Required Python libraries.

### Setup Steps
1. **Clone the Repository:**
   ```bash
   git clone [Your-GitHub-Repo-URL] iso-qat-lab
   cd iso-qat-lab
   ```
2. **Activate Environment:**
   ```bash
   source venv/bin/activate 
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
*A note: The `requirements.txt` file must be updated to reflect all necessary libraries for the local stack.*

### 🧪 Running the Cycle (Live Test)
To see the full, working, local workflow demonstration, execute the main CLI script:
```bash
python qa-lab/local-agents-adk/local_agents_cli.py
```

***
*(This documentation is managed by the QA Lab system.)*