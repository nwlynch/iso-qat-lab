# TaskFlow — Test Case Suite

| Field   | Value             |
|---------|-------------------|
| Project | TaskFlow          |
| Date    | 2026-04-17        |
| Total   | 10 test cases     |

---

## TC-001 — Create task with valid inputs

| Field      | Value            |
|------------|------------------|
| Type       | Positive         |
| Linked Req | REQ-F01          |
| Status     | Not Run          |

**Preconditions:** User is logged in.

**Steps:**
1. Click Create Task.
2. Fill all fields with valid data.
3. Click Save.

**Expected Result:** Task is created and appears on board.

---

## TC-002 — Create task with empty title

| Field      | Value            |
|------------|------------------|
| Type       | Negative         |
| Linked Req | REQ-F01, REQ-D01 |
| Status     | Not Run          |

**Preconditions:** User is logged in.

**Steps:**
1. Click Create Task.
2. Leave title blank.
3. Click Save.

**Expected Result:** Validation error is displayed; task is not created.

---

## TC-003 — Create task with 200-char title

| Field      | Value            |
|------------|------------------|
| Type       | Boundary         |
| Linked Req | REQ-D01          |
| Status     | Not Run          |

**Preconditions:** User is logged in.

**Steps:**
1. Click Create Task.
2. Enter exactly 200-character title.
3. Click Save.

**Expected Result:** Task is created successfully.

---

## TC-004 — Create task with 201-char title

| Field      | Value            |
|------------|------------------|
| Type       | Boundary         |
| Linked Req | REQ-D01          |
| Status     | Not Run          |

**Preconditions:** User is logged in.

**Steps:**
1. Click Create Task.
2. Enter 201-character title.
3. Click Save.

**Expected Result:** Validation error: title exceeds max length.

---

## TC-005 — Filter by single status

| Field      | Value            |
|------------|------------------|
| Type       | Positive         |
| Linked Req | REQ-F02          |
| Status     | Not Run          |

**Preconditions:** Board has tasks in multiple statuses.

**Steps:**
1. Open filter panel.
2. Select status "In Progress".
3. Apply.

**Expected Result:** Only "In Progress" tasks are displayed.

---

## TC-006 — Filter with no matching results

| Field      | Value            |
|------------|------------------|
| Type       | Negative         |
| Linked Req | REQ-F02          |
| Status     | Not Run          |

**Preconditions:** Board has tasks, none with status "Blocked".

**Steps:**
1. Open filter panel.
2. Select status "Blocked".
3. Apply.

**Expected Result:** Empty state message is displayed.

---

## TC-007 — Verify email on task assignment

| Field      | Value            |
|------------|------------------|
| Type       | Positive         |
| Linked Req | REQ-F03          |
| Status     | Not Run          |

**Preconditions:** SMTP configured; user has valid email.

**Steps:**
1. Create a task.
2. Assign to User-X.
3. Check User-X inbox.

**Expected Result:** Assignment notification email received within 60 s.

---

## TC-008 — No email on self-assignment

| Field      | Value            |
|------------|------------------|
| Type       | Equivalence      |
| Linked Req | REQ-F03          |
| Status     | Not Run          |

**Preconditions:** User logged in as User-X.

**Steps:**
1. Create a task.
2. Assign to self (User-X).
3. Check inbox.

**Expected Result:** No notification email sent (self-assignment suppressed).

---

## TC-009 — Page load under 500 concurrent users

| Field      | Value            |
|------------|------------------|
| Type       | Positive         |
| Linked Req | REQ-NF01         |
| Status     | Not Run          |

**Preconditions:** Load test environment configured.

**Steps:**
1. Simulate 500 concurrent users.
2. Each user loads board view.
3. Measure p95 load time.

**Expected Result:** p95 load time is under 2 seconds.

---

## TC-010 — API call without auth token

| Field      | Value            |
|------------|------------------|
| Type       | Negative         |
| Linked Req | REQ-NF02         |
| Status     | Not Run          |

**Preconditions:** No auth header.

**Steps:**
1. Send `GET /api/tasks` without Authorization header.
2. Observe response.

**Expected Result:** 401 Unauthorized returned.
