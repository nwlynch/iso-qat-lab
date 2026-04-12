# ISO-QA-Lab: Security Scanner Agent

## 🛡️ Agent Purpose

Scans code, requirements, and test cases for security vulnerabilities and best practice compliance.

**ISO 12207:2017 Clauses:**
- 12207.7.1 (Test Analysis) - Security test case generation
- 12207.8.1 (Quality Audit) - Security audit evidence

---

## 🎯 Agent Responsibilities

### **Core Tasks:**
- Scan code for OWASP Top 10 vulnerabilities
- Generate fuzzing test cases for security testing
- Check for common security misconfigurations
- Review dependencies for known vulnerabilities
- Generate security audit reports

### **Output Formats:**
- SAST (Static Application Security Testing) reports
- Fuzzing test cases
- Security audit evidence
- Remediation recommendations

---

## 🔒 Vulnerability Coverage

### **OWASP Top 10:**
- **A01: Broken Access Control** → Unauthorized access detection
- **A02: Cryptographic Failures** → Weak encryption detection
- **A03: Injection** → SQL/XSS injection detection
- **A04: Insecure Design** → Design flaws detection
- **A05: Security Misconfiguration** → Config issues detection
- **A06: Vulnerable Components** → Deprecated libraries
- **A07: Auth Failures** → Authentication bypass detection
- **A08: Data Integrity** → Data corruption detection
- **A09: Security Logging** → Logging gaps detection
- **A10: SSRF** → Server-side request forgery detection

### **Additional Checks:**
- **CWE Top 25** → Common Weakness Enumeration
- **SANS Top 20** → Common vulnerabilities and exposures
- **NIST CSF** → Cybersecurity framework compliance

---

## 📦 Deliverables

### **1. SAST Report (JSON)**
```json
{
  "scan_id": "SEC-20260412-001",
  "timestamp": "2026-04-12T18:57:00Z",
  "target": "src/login.py",
  "findings": [
    {
      "id": "VULN-001",
      "type": "Injection",
      "cwe": "CWE-89",
      "owasp": "A03: Injection",
      "severity": "High",
      "location": "src/login.py:45",
      "code": "execute(sql_query(user_input))",
      "remediation": "Use parameterized queries",
      "test_case": "TC-SQL-INJ-001"
    }
  ],
  "summary": {
    "total_findings": 3,
    "critical": 0,
    "high": 1,
    "medium": 2,
    "low": 0
  }
}
```

### **2. Fuzzing Test Cases (YAML)**
```yaml
fuzzing_tests:
  - target: "login_endpoint"
    parameter: "username"
    test_vectors:
      - type: "SQL_Injection"
        inputs:
          - "' OR '1'='1"
          - "' UNION SELECT * FROM users"
          - "'; DROP TABLE users;--"
        expected: "No data leakage"
      - type: "XSS"
        inputs:
          - "<script>alert('XSS')</script>"
          - "<img src=x onerror=alert(1)>"
        expected: "Script blocked"
```

### **3. Security Report (Markdown)**
```markdown
# Security Audit Report

**Scan ID:** SEC-20260412-001  
**Date:** 2026-04-12  
**Target:** src/

## Summary
- Critical: 0
- High: 1
- Medium: 2
- Low: 0

## Findings
### 🔴 HIGH: SQL Injection
**Location:** src/login.py:45  
**Remediation:** Use parameterized queries

---

## Recommendations
1. Review all database queries
2. Implement input validation
3. Add rate limiting
```

---

## 🔄 Workflow Integration

```
12207.3.1 (Requirements) → Security Scanner → Security Test Cases → 12207.7.1 (Verification) → 12207.8.1 (QA Audit)
```

### **Integration Points:**
1. **Input:** Receives code, requirements, test cases
2. **Process:** Runs security analysis
3. **Output:** Security test cases, audit reports

---

## 📝 Input Format

```json
{
  "target": {
    "type": "code",
    "path": "src/login.py",
    "language": "python"
  },
  "context": {
    "requirement": "REQ-LOGIN",
    "test_cases": "tc-login.yaml"
  },
  "options": {
    "sast_enabled": true,
    "dependency_scan": true,
    "output_dir": "results/security/"
  }
}
```

---

## 📝 Output Format

```json
{
  "scan_id": "SEC-20260412-001",
  "status": "completed",
  "timestamp": "2026-04-12T18:57:00Z",
  "target": "src/login.py",
  "findings": [
    {
      "id": "VULN-001",
      "type": "SQL Injection",
      "cwe": "CWE-89",
      "owasp": "A03: Injection",
      "severity": "High",
      "location": "src/login.py:45",
      "code_snippet": "execute(sql_query(user_input))",
      "description": "Direct user input to database query",
      "remediation": "Use parameterized queries or ORM",
      "test_case": {
        "id": "TC-SQL-INJ-001",
        "framework": "playwright",
        "steps": [
          "Navigate to /login",
          "Enter username: ' OR '1'='1",
          "Enter password: anything",
          "Click login"
        ],
        "expected": "SQL error or sanitized error"
      }
    }
  ],
  "summary": {
    "total": 3,
    "critical": 0,
    "high": 1,
    "medium": 2,
    "low": 0
  },
  "recommendations": [
    "Review all database queries",
    "Implement input validation",
    "Add rate limiting"
  ]
}
```

---

## 🚀 Implementation Plan

**Phase 1: Core Logic (Week 1)**
1. Create agent directory structure
2. Implement basic vulnerability detection
3. Add OWASP Top 10 checks
4. Generate test cases

**Phase 2: Tool Integration (Week 2)**
5. Add SAST tool integration (Bandit, Semgrep)
6. Add dependency scanning
7. Add configuration auditing

**Phase 3: Reporting (Week 3)**
8. Add security report generation
9. Add audit evidence collection
10. Add remediation templates

**Phase 4: Advanced (Week 4+)**
11. Add fuzzing generation
12. Add vulnerability scoring
13. Add compliance mapping (PCI, GDPR, HIPAA)

---

## 📦 Files to Create

```
agents/
└── sec-security-scanner/
    ├── agent.py                # Core agent logic
    ├── prompts.yaml            # System prompts
    ├── config.yaml             # Configuration
    ├── schemas/
    │   ├── security-finding.json
    │   ├── test-case.json
    │   └── audit-report.yaml
    └── output/
        ├── findings.json
        ├── fuzzing-tests.yaml
        └── audit-report.md
```

---

## 🧪 Example Scan

**Input:**
```json
{
  "target": {
    "path": "src/login.py",
    "language": "python"
  },
  "sast_enabled": true
}
```

**Output:**
```json
{
  "scan_id": "SEC-20260412-001",
  "findings": [
    {
      "id": "VULN-001",
      "type": "SQL Injection",
      "severity": "High",
      "location": "src/login.py:45",
      "remediation": "Use parameterized queries"
    }
  ]
}
```

---

## 🛠️ Vulnerability Detection Methods

### **1. Static Analysis (SAST)**
- Pattern matching for common vulnerabilities
- Code flow analysis
- Data flow tracking

### **2. Dependency Scanning**
- Check for known CVEs
- Outdated library warnings
- License compliance

### **3. Configuration Auditing**
- Insecure default configurations
- Misconfigured security settings
- Incomplete security policies

### **4. Test Case Generation**
- Attack simulation test cases
- Boundary condition fuzzing
- Error handling validation

---

## 📊 Metrics Tracking

- Vulnerabilities found: X
- Test cases generated: X
- Audit reports created: X
- Security score: X/100

---

**Status:** ✅ Ready for implementation  
**Next:** Create the core agent files!
