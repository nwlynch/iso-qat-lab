# 🧪 ISO-QA-Lab Project Snapshot (V1.0 Draft) 🧪

**Date Saved:** {datetime.now().strftime('%Y-%m-%d')}
**Author:** System Assisted by Neville
**Goal:** To build a fully operational, multi-agent local AI laboratory compliant with ISO/IEC/IEEE 12207:2017 for AI-assisted Enterprise QA.

---

## 🗺️ Project Structure Snapshot
All core components reside within the `iso-qat-lab/` directory.

### 📂 Directory Contents Summary:
*   `agent-prompts.yaml`: Contains all agent instructions, roles, and model assignments.
*   `config/`: Contains all required data contracts (schemas) and configurations.
*   `config/requirement_artifact_schema.json`: Schema for Phase 1 output.
*   `config/test_case_artifact_schema.json`: Schema for Phase 4 test results.
*   `config/project_plan_artifact_schema.json`: Schema for Phase 2 output.
*   `config/baseline_settings_artifact_schema.json`: Schema for Phase 3 output.
*   `config/test_analysis_report_schema.json`: Schema for Phase 4 summary.
*   `orchestration_flow_plan.md`: The high-level, conceptual, step-by-step plan.
*   `run_lifecycle.py`: The Python executable blueprint that controls the flow via function calls.

---

## ➡️ Next Steps for Resumption (Recommended Action)
1.  **Run the Script:** Execute `python3 run_lifecycle.py` from the `iso-qat-lab/` directory.
2.  **Implementation Detail:** The script must be updated to make real API calls instead of using simulation placeholders (`simulate_agent_call`).

---
**This snapshot captures the full scope of the design and implementation blueprint.**
