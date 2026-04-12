# ISO-QA-Lab: Test Generator Agent

## 🧬 Agent Purpose

Creates comprehensive test cases from requirements and specifications.

**ISO 12207:2017 Clause:** 12207.7.1 (Test Analysis)

---

## 🎯 Agent Responsibilities

- Parse user stories and acceptance criteria
- Generate comprehensive test cases
- Create edge case scenarios
- Output test cases in preferred framework format (Selenium/Playwright/Jest)
- Map tests to ISO 12207 requirements

---

## 📦 Deliverables

### **Test Cases (JSON/YAML)**
```yaml
test_cases:
  - id: TC-001
    description: "User can login with valid credentials"
    prerequisites:
      - User account exists
      - Login page accessible
    test_steps:
      - Navigate to login page
      - Enter valid username
      - Enter valid password
      - Click login button
    expected_result: "Redirect to dashboard"
    severity: "Critical"
    framework: "playwright"
  - id: TC-002
    description: "User can login with invalid credentials"
    test_steps:
      - Navigate to login page
      - Enter invalid username
      - Enter invalid password
      - Click login button
    expected_result: "Display error message"
    severity: "High"
    framework: "playwright"
```

### **Test Report (Markdown)**
```markdown
# Test Report - TC-001 to TC-010

| ID | Status | Duration | Timestamp |
|-----|--------|----------|------------|
| TC-001 | PASSED | 2.3s | 2026-04-12T17:40:00Z |

**Summary:** 10 tests, 9 passed, 1 failed
```

---

## 🔄 Workflow Integration

```
12207.3.1 (Requirements) → test-generator → 12207.7.1 (Test Analysis) → ver-test-executor → 12207.7.2 (Test Execution)
```

---

## 📝 Example Input

```json
{
  "requirement_id": "REQ-001",
  "title": "User Authentication",
  "description": "Users can login to the system with valid credentials",
  "acceptance_criteria": [
    "User can enter username and password",
    "System validates credentials",
    "Success redirects to dashboard",
    "Failure displays error message"
  ],
  "edge_cases": [
    "Empty username",
    "Empty password",
    "SQL injection attempt",
    "Special characters in username"
  ],
  "browser_support": ["chrome", "firefox", "safari", "edge"],
  "framework": "playwright"
}
```

---

## 📝 Example Output

```json
{
  "test_id": "TC-{REQ_ID}-001",
  "title": "User Authentication",
  "test_cases": [
    {
      "id": "TC-{REQ_ID}-001",
      "title": "Valid credentials",
      "steps": ["Navigate to /login", "Enter username", "Enter password", "Click login"],
      "expected": "Redirect to dashboard",
      "framework": "playwright"
    }
  ]
}
```

---

## 🚀 Implementation Plan

**Phase 1: Core Logic (Week 1)**
1. Create agent directory structure
2. Implement basic test generation logic
3. Add requirement parser
4. Generate test cases in YAML/JSON

**Phase 2: Framework Support (Week 2)**
5. Add Selenium/Playwright/Jest output formats
6. Add edge case generation
7. Add test data generation

**Phase 3: Integration (Week 3)**
8. Connect to 12207.3.1 requirements
9. Connect to 12207.7.2 test execution
10. Add logging and metrics

**Phase 4: Advanced (Week 4+)**
11. Add test optimization
12. Add parallel execution support
13. Add coverage reporting

---

## 📦 Files to Create

```
agents/
└── ver-test-generator/
    ├── agent.py               # Core agent logic
    ├── prompts.yaml           # System prompts
    ├── config.yaml            # Configuration
    ├── schemas/
    │   ├── test-case.json     # Test case schema
    │   └── edge-case.json     # Edge case schema
    └── output/
        ├── test-cases.yaml
        └── test-report.md
```

---

## 🧪 Example Test Generation

**Input:**
```json
{
  "requirement_id": "REQ-LOGIN",
  "title": "User Login",
  "acceptance": [
    "Valid credentials redirect to dashboard",
    "Invalid credentials show error",
    "Account lockout after 5 failed attempts"
  ]
}
```

**Output:**
```yaml
test_cases:
  - id: TC-LOGIN-001
    title: "Valid credentials"
    framework: "playwright"
    steps:
      - "Navigate to /login"
      - "Enter valid username"
      - "Enter valid password"
      - "Click login button"
    expected: "Redirect to dashboard"
    assertions:
      - "URL contains /dashboard"
      - "No error message"
  
  - id: TC-LOGIN-002
    title: "Invalid credentials"
    framework: "playwright"
    steps:
      - "Navigate to /login"
      - "Enter valid username"
      - "Enter invalid password"
      - "Click login button"
    expected: "Show error message"
    assertions:
      - "Error message visible"
      - "URL stays at /login"
  
  - id: TC-LOGIN-003
    title: "Account lockout"
    framework: "playwright"
    steps:
      - "Navigate to /login"
      - "Enter valid username"
      - "Enter invalid password"
      - "Click login button"
      - "Repeat 5 times"
    expected: "Account locked"
    assertions:
      - "Account locked message shown"
      - "Login disabled for 15 minutes"
```

---

**Status:** ✅ Ready for implementation  
**Next:** I'll create the `agents/ver-test-generator/` directory structure and implement the core agent logic!
