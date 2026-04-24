# TaskFlow — Traceability Matrix

| Field   | Value             |
|---------|-------------------|
| Project | TaskFlow          |
| Date    | 2026-04-17        |

---

## Requirements ↔ Tests ↔ Defects

| Requirement ID | Requirement Title        | Test Cases              | Bugs    | Coverage Status |
|----------------|--------------------------|-------------------------|---------|-----------------|
| REQ-F01        | Task creation            | TC-001, TC-002, TC-003, TC-004 | BUG-001 | Covered         |
| REQ-F02        | Task board filtering     | TC-005, TC-006          | BUG-003 | Covered         |
| REQ-F03        | Assignment email notifications | TC-007, TC-008    | BUG-002 | Covered         |
| REQ-NF01       | Page load performance    | TC-009                  | BUG-004 | Partial         |
| REQ-NF02       | OAuth API authentication | TC-010                  | BUG-005 | Covered         |
| REQ-D01        | Title length constraints | TC-002, TC-003, TC-004  | None    | Covered         |
| REQ-D02        | Filter response time     | None                    | None    | **Not Covered** |
| REQ-A01        | Data volume handling     | None                    | BUG-004 | **Not Covered** |
| REQ-A02        | UI usability             | None                    | None    | **Not Covered** |

## Coverage Summary

- **Covered:** 5 / 9 requirements
- **Partial:** 1 / 9 requirements (REQ-NF01 — single test, no boundary/negative)
- **Not Covered:** 3 / 9 requirements (REQ-D02, REQ-A01, REQ-A02)

> **Gap Note:** REQ-D02, REQ-A01, and REQ-A02 are deliberately uncovered to provide detectable coverage gaps for QA framework evaluation.
