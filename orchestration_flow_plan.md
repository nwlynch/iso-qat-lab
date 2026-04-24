# ISO-QA-Lab Orchestration Flow Plan (The Conductor Script)

**Goal:** To execute the entire QA lifecycle by sequentially calling specialized agents, validating the output against defined schemas at every handoff, and managing state transitions.

**Tooling Context:** This pseudo-code assumes the existence of:
1.  `sessions_spawn` or a similar agent execution mechanism.
2.  The schemas located in `iso-qat-lab/config/`.
3.  The agent prompts located in `iso-qat-lab/config/agent-prompts.yaml`.

## Flow: Full Lifecycle Execution (`run-full-lifecycle.sh`)

### 0. Initialization & Setup
1.  **Load Configuration:** Read `models.yaml` and establish which models are available for which agents.
2.  **Initialize State:** Create/update a global `state.json` object to track all artifacts generated so far (this acts as the primary memory for the session).
3.  **Schema Loading:** Load and validate the schemas from `config/`.

### 1. Phase 1: Acquisition (Input Gathering)
*   **Action:** Call `acq-requirements-parser` using the initial requirements document as input.
*   **Input:** Raw Requirements Document.
*   **Schema Check:** Must strictly adhere to **`requirement_artifact_schema.json`**.
*   **State Update:** Upon success, ingest the resulting JSON structure into `state.json` under the `requirements` key.

### 2. Phase 2: Project Management (Planning)
*   **Trigger:** Requires `state.json.requirements`.
*   **Action:** Call `pm-project-planning`.
*   **Input:** Reference to `state.json.requirements`.
*   **Schema Check:** Validation against the expected Project Plan structure (requires defining a new schema, `project_plan_artifact.json`).
*   **State Update:** Ingest plan into `state.json.project_plan`.

### 3. Phase 3: Configuration (Baseline)
*   **Trigger:** Requires `state.json.project_plan`.
*   **Action:** Call `cfg-configuration`.
*   **Input:** Reference to `state.json.project_plan`.
*   **Schema Check:** Validation against `baseline_settings_artifact.json` (Schema TBD).
*   **State Update:** Ingest baseline into `state.json.baseline`.

### 4. Phase 4: Verification (The Core Loop)
*   **Trigger:** Requires `state.json.project_plan` AND `state.json.baseline`.
*   **Sub-Step 4.1: Test Generation:**
    *   Call `ver-test-generator`.
    *   Input: `state.json.project_plan` + `state.json.baseline`.
    *   Schema Check: Must adhere to **`test_case_artifact_schema.json`**.
    *   State Update: Save generated test cases to `state.json.test_cases`.
*   **Sub-Step 4.2: Test Execution:**
    *   Iterate over all generated test cases in `state.json.test_cases`.
    *   For each, call `ver-test-executor`.
    *   Input: Specific Test Case ID + Environment Context.
    *   Schema Check: Output must validate against **`test_case_artifact_schema.json`** (only updating the `test_status` and `execution_details` fields).
    *   State Update: Update the specific test case in `state.json.test_cases` with the result.
*   **Sub-Step 4.3: Analysis:**
    *   Call `ver-test-analytics`.
    *   Input: All updated test results from `state.json.test_cases`.
    *   Schema Check: Requires defining `test_analysis_report.json`.
    *   State Update: Save analysis report to `state.json.test_analysis`.

### 5. Phase 5 - Phase 7: Validation, Audit, Sustainment
*   These phases follow a similar pattern: **[CALL AGENT] $\rightarrow$ [SCHEMA VALIDATION] $\rightarrow$ [UPDATE STATE]**

---
**Action Items:**
1.  Define the schemas for the missing artifacts (`project_plan_artifact.json`, `baseline_settings_artifact.json`, `test_analysis_report.json`).
2.  Build the shell script logic to manage the state transitions (the actual "conductor").