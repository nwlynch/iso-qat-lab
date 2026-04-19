# TaskFlow — Bug Backlog

| Field   | Value             |
|---------|-------------------|
| Project | TaskFlow          |
| Date    | 2026-04-17        |
| Status  | Active Sprint     |

---

## BUG-001 — Task creation fails with special characters in title

| Field       | Value                |
|-------------|----------------------|
| Severity    | High                 |
| Priority    | P1                   |
| Status      | Open                 |
| Linked Req  | REQ-F01              |

**Repro Steps:**
1. Navigate to Create Task.
2. Enter title: `Test <script>`.
3. Click Save.
4. Observe 500 error.

---

## BUG-002 — Email notification not sent for bulk assignments

| Field       | Value                |
|-------------|----------------------|
| Severity    | Medium               |
| Priority    | P2                   |
| Status      | Open                 |
| Linked Req  | REQ-F03              |

**Repro Steps:**
1. Select 5 tasks.
2. Bulk assign to user.
3. Check user inbox.
4. No email received.

---

## BUG-003 — Filter by assignee returns stale results after reassignment

| Field       | Value                |
|-------------|----------------------|
| Severity    | Medium               |
| Priority    | P2                   |
| Status      | In Progress          |
| Linked Req  | REQ-F02              |

**Repro Steps:**
1. Assign Task-A to User-X.
2. Reassign Task-A to User-Y.
3. Filter by User-Y.
4. Task-A not shown.

---

## BUG-004 — Page load exceeds 5s with 300+ tasks on board

| Field       | Value                |
|-------------|----------------------|
| Severity    | High                 |
| Priority    | P1                   |
| Status      | Open                 |
| Linked Req  | REQ-NF01             |

**Repro Steps:**
1. Seed board with 350 tasks.
2. Navigate to board view.
3. Measure load time.
4. Observed: 5.2 s.

---

## BUG-005 — OAuth token refresh silently fails causing 401

| Field       | Value                |
|-------------|----------------------|
| Severity    | Critical             |
| Priority    | P1                   |
| Status      | Open                 |
| Linked Req  | REQ-NF02             |

**Repro Steps:**
1. Authenticate.
2. Wait for token expiry (60 min).
3. Perform any API call.
4. 401 Unauthorized returned, no refresh attempt.
