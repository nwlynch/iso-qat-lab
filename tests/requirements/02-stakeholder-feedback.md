# TaskFlow — Stakeholder Feedback Dossier

| Field       | Value                                |
|-------------|--------------------------------------|
| Version     | 1.0                                  |
| Date        | 2026-04-17                           |
| Compiled by | QA Framework Team                    |
| Project     | TaskFlow (Project Management Web App)|

---

## 1. Stakeholder Registry

| Name          | Role             | Department        |
|---------------|------------------|-------------------|
| Priya Sharma  | Product Owner    | Product           |
| Marcus Chen   | Engineering Lead | Engineering       |
| Anya Petrov   | UX Designer      | Design            |
| David Okafor  | QA Manager       | Quality Assurance |

## 2. Categorized Feedback

### Feature Requests

- **Priya Sharma:** *"We need a drag-and-drop board view for sprint planning."* `[REQ-F02 adjacent]`
- **Marcus Chen:** *"Add webhook support for CI/CD pipeline triggers on task status change."* `[New requirement]`

### Usability Concerns

- **Anya Petrov:** *"The filter panel is buried — users miss it entirely. Needs prominent placement."* `[REQ-F02]`
- **Anya Petrov:** *"Error messages on task creation are too technical for end users."* `[REQ-F01]`

### Performance Concerns

- **Marcus Chen:** *"We're already seeing slowdowns at 200 concurrent users — the 500-user target in REQ-NF01 seems unrealistic without caching."* `[REQ-NF01]`

### Security Concerns

- **David Okafor:** *"OAuth token refresh has a silent failure mode. Needs explicit error handling and alerting."* `[REQ-NF02, BUG-005]`

### Quality / Testing

- **David Okafor:** *"We lack negative test coverage for special characters in task fields. See BUG-001."* `[REQ-F01, BUG-001]`

## 3. Raw Feedback Log

| Date       | Stakeholder   | Channel      | Verbatim Feedback |
|------------|---------------|--------------|-------------------|
| 2026-04-03 | Priya Sharma  | Sprint Retro | "Sprint planning would be far more intuitive with a visual board. The current list view forces too many clicks to re-prioritize." |
| 2026-04-07 | Marcus Chen   | Slack        | "Our CI pipeline can't react to TaskFlow status changes. We need outbound webhooks — polling the API isn't sustainable." |
| 2026-04-10 | Anya Petrov   | Email        | "Three out of five usability test participants could not locate the filter panel. It needs to be surfaced in the main toolbar." |
| 2026-04-14 | David Okafor  | JIRA Comment | "BUG-001 is reproducible: pasting emoji or angle brackets into the task title field causes a 500 error. No client-side validation exists." |
| 2026-04-16 | Marcus Chen   | 1:1 Meeting  | "Load tests plateau at ~200 users. Response times breach the 2-second SLA beyond that. We need a Redis caching layer before launch." |
