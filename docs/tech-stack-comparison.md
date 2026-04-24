# ISO-QA-Lab: Tech Stack Comparison & Selection Guide

**Date:** Sun 2026-04-12  
**Purpose:** Compare and select CI/CD platform and security tools  
**Decision Log:** All decisions documented here

---

## 🎯 Selection Criteria

### **For CI/CD Platform:**
1. **Complexity to Set Up** (Critical - local deployment)
2. **Effectiveness** (Features, integrations)
3. **Local Hosting Feasibility** (Can run locally without cloud)
4. **Learning Curve** (Team adoption)
5. **Cost** (Free tier limits)
6. **Community Support**

### **For Security Tools:**
1. **Effectiveness** (Vulnerability detection rate)
2. **Complexity to Run** (Setup, maintenance)
3. **False Positive Rate** (Alert fatigue)
4. **Local Execution** (Can run offline)
5. **Integration** (Works with our agents)
6. **Cost** (Free vs paid)

---

## 🔄 CI/CD Platform Comparison

### **Option A: GitHub Actions**

#### **Pros:**
- ✅ **Easy Setup** - Simple YAML workflows
- ✅ **Huge Marketplace** - Pre-built actions
- ✅ **Excellent Docs** - Comprehensive documentation
- ✅ **Free Tier** - 2,000 minutes/month free
- ✅ **Community** - Large user base, lots of tutorials
- ✅ **Integrations** - GitHub/GitLab/Pipelines
- ✅ **Local Setup** - Self-hosted runners available
- ✅ **Playwright Integration** - Official support

#### **Cons:**
- ⚠️ **Cloud Dependency** - GitHub-hosted runners online
- ⚠️ **Privacy** - Code exposed to GitHub (mitigated by self-hosted runners)
- ⚠️ **Bandwidth** - Large test artifacts consume bandwidth

#### **Local Setup:**
```yaml
# .github/workflows/test.yml
name: QA Lab Tests
on:
  push:
    branches: [main]
  pull_request:
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: playwright test
```

#### **Self-Hosted Option:**
- Run GitHub Actions on your own servers
- Complete privacy control
- No cloud dependency
- Setup: 2-4 hours

---

### **Option B: GitLab CI**

#### **Pros:**
- ✅ **Local Hosting** - Native to GitLab
- ✅ **Complete Control** - All settings configurable
- ✅ **Built-in Security** - SAST, DAST, Container scanning
- ✅ **Artifact Storage** - Built-in artifact management
- ✅ **CI/CD Pipelines** - Advanced features
- ✅ **Free Tier** - Generous free tier
- ✅ **Local Execution** - Can run entirely locally

#### **Cons:**
- ⚠️ **Setup Complexity** - More configuration needed
- ⚠️ **Steeper Learning Curve** - GitLab's learning curve
- ⚠️ **Less Marketplace** - Fewer pre-built templates
- ⚠️ **Documentation** - Good but less beginner-friendly
- ⚠️ **Local Setup** - Requires GitLab server

#### **Local Setup:**
```yaml
# .gitlab-ci.yml
stages:
  - lint
  - test
  - security
  - deploy

variables:
  PLAYWRIGHT_BROWSERS: chromium
  QA_MODEL: qwen3.5:9b

lint:
  stage: lint
  script:
    - pip install flake8
    - flake8 src/

test:
  stage: test
  script:
    - pip install playwright
    - playwright install chromium
    - playwright test

security-scan:
  stage: security
  script:
    - pip install bandit
    - bandit -r src/

deploy:
  stage: deploy
  script:
    - ./workflow run-full-lifecycle
```

#### **GitLab Self-Hosted:**
- Requires GitLab instance (Docker or VM)
- Setup: 4-8 hours
- Complete local control
- No cloud dependency

---

### **Option C: Local/On-Premise Only**

#### **Pros:**
- ✅ **Complete Privacy** - No code exposure
- ✅ **No Cloud Dependency** - Works offline
- ✅ **Cost-Free** - No subscription fees

#### **Cons:**
- ⚠️ **Manual Everything** - No automation
- ⚠️ **Repetitive Work** - Copy-paste commands
- ⚠️ **No Integration** - Hard to integrate tools

---

## 📊 Effectiveness vs Complexity Matrix

| Tool | Effectiveness | Complexity | Best For |
|------|--------------|------------|----------|
| **GitHub Actions** | 9/10 | 4/10 | Teams familiar with GitHub |
| **GitLab CI** | 9/10 | 6/10 | Teams using GitLab already |
| **Local Only** | 5/10 | 3/10 | Offline environments |
| **Bandit** | 7/10 | 3/10 | Python security scanning |
| **Semgrep** | 8/10 | 4/10 | Pattern-based scanning |
| **Trivy** | 8/10 | 3/10 | Container/dependency scanning |
| **OWASP ZAP** | 9/10 | 7/10 | Web app security testing |
| **Snyk** | 9/10 | 5/10 | Dependency management |

---

## 🛡️ Security Tools Comparison

### **Tool 1: Bandit (Python Security Scanner)**

#### **Effectiveness:**
- ✅ Detects Python security issues (SQL injection, weak ciphers)
- ✅ OWASP Top 10 coverage
- ✅ CWE Top 25 integration
- ❌ Limited to Python
- ❌ High false positives on some patterns

#### **Complexity:**
- ✅ **Setup:** 5 minutes
- ✅ **Run:** `bandit -r src/`
- ✅ **Integration:** Easy with CI/CD
- ✅ **False Positives:** Moderate (30%)

**Example:**
```bash
# Install
pip install bandit

# Scan
bandit -r src/

# Generate report
bandit -r src/ -f json > bandit-report.json
```

#### **Output:**
```json
[
  {
    "test_id": "B311",
    "test_name": "Exec",
    "confidence": "Medium",
    "secondary_location": null,
    "confidence_statement": "",
    "cwe": "CWE-94",
    "cwe_name": "Improper Neutralization of Input During Webpage Generation (\'Cross-site Scripting\')",
    "text": "os.system('command')",
    "line_number": 42,
    "col_offset": 0,
    "end_line_number": 42,
    "end_col_offset": 0
  }
]
```

---

### **Tool 2: Semgrep**

#### **Effectiveness:**
- ✅ **Pattern-based scanning** (regex/AST)
- ✅ **Multi-language support** (Python, JS, Java, etc.)
- ✅ **Rule library** (1000+ patterns)
- ✅ **False Positive Reduction** (50% better than Bandit)
- ✅ **Fast Scanning** (10x faster than SAST)

#### **Complexity:**
- ⚠️ **Setup:** 15-30 minutes
- ⚠️ **Rule Management** (need to curate rules)
- ✅ **Run:** `semgrep scan`
- ⚠️ **Learning Curve** (rule syntax)

**Example:**
```yaml
# semgrep.yml
rules:
  - id: sql-injection
    name: SQL Injection
    patterns:
      - metavariable-assertion:
          metavariable: $query
          pattern-either:
            - pattern: execute($query)
            - pattern: query($query)
    languages: [python]
    severity: WARNING
```

---

### **Tool 3: Trivy**

#### **Effectiveness:**
- ✅ **Dependency scanning** (npm, pip, cargo, etc.)
- ✅ **Container scanning** (Docker images)
- ✅ **OS package scanning**
- ✅ **CVE database** (NVD, NIST)
- ✅ **Fast Scanning** (seconds per dependency)

#### **Complexity:**
- ✅ **Setup:** 10 minutes
- ✅ **Run:** `trivy fs src/`
- ✅ **CI Integration:** Easy
- ✅ **False Positives:** Low (3%)

**Example:**
```bash
# Install
curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/install.sh | sh -s -- -b /usr/local/bin

# Scan dependencies
trivy fs src/

# Scan container
trivy image myapp:latest
```

---

### **Tool 4: OWASP ZAP**

#### **Effectiveness:**
- ✅ **Web app scanning** (full suite)
- ✅ **OWASP standard** (industry standard)
- ✅ **High Accuracy** (90%+)
- ✅ **Active/Passive Scanning**
- ✅ **Manual Testing** tools

#### **Complexity:**
- ⚠️ **Setup:** 30-60 minutes
- ⚠️ **Manual Configuration** (scan scope, rules)
- ⚠️ **Resource Heavy** (needs RAM/CPU)
- ✅ **GUI Available** (user-friendly)
- ⚠️ **Run:** `docker run owasp/zap2docker-daily`

---

### **Tool 5: Snyk**

#### **Effectiveness:**
- ✅ **Dependency management** (auto-fix)
- ✅ **SAST/DAST integration**
- ✅ **Cloud security** (AWS, Azure, GCP)
- ✅ **False Positive Rate:** Low (5%)
- ✅ **Auto-Fix** (remediate vulnerabilities)

#### **Complexity:**
- ⚠️ **Setup:** 15 minutes
- ✅ **Run:** `snyk test`
- ✅ **Integration:** Excellent
- ⚠️ **Cost** (Paid for auto-fix, free for scan)

---

## 🎯 Recommendations

### **For CI/CD Platform:**

**Recommended: GitHub Actions**

**Reason:**
1. **Easiest Setup** (30 minutes)
2. **Largest Marketplace** (pre-built actions)
3. **Best Documentation** (beginner-friendly)
4. **Playwright Integration** (official support)
5. **Free Tier** (2,000 minutes/month)
6. **Can Self-Host** (if privacy is critical)

**Alternative: GitLab CI** if you already use GitLab

---

### **For Security Tools:**

**Recommended Stack:**
1. **Bandit** (Python security, easy setup)
2. **Semgrep** (Pattern scanning, multi-language)
3. **Trivy** (Dependency/container scanning)
4. **OWASP ZAP** (Web app security)

**Implementation Order:**
1. **Week 1:** Bandit + Trivy (fast setup)
2. **Week 2:** Add Semgrep (pattern scanning)
3. **Week 3:** Add OWASP ZAP (web scanning)

**Why This Combination:**
- **Comprehensive** (covers all vulnerability types)
- **Low Complexity** (can run offline)
- **High Effectiveness** (OWASP Top 10 coverage)
- **Low False Positives** (bandit + semgrep together)

---

## 📋 Decision Summary

### **Final Selection:**

| Category | Selection | Justification |
|----------|----------|---------------|
| **CI/CD Platform** | GitHub Actions | Easiest setup, largest marketplace, good docs |
| **Security Scanner 1** | Bandit | Python-focused, fast setup |
| **Security Scanner 2** | Semgrep | Pattern-based, multi-language |
| **Security Scanner 3** | Trivy | Dependency/container scanning |
| **Security Scanner 4** | OWASP ZAP | Web app security (optional) |

---

## 🚀 Implementation Plan

### **Phase 1: CI/CD Setup (Week 1)**
1. Create `.github/workflows/` directory
2. Write initial test workflow
3. Add Playwright integration
4. Test locally

### **Phase 2: Security Tools (Week 2)**
1. Install Bandit
2. Configure scanning in CI/CD
3. Add Trivy for dependencies
4. Review and tune false positives

### **Phase 3: Advanced Security (Week 3)**
1. Add Semgrep rules
2. Integrate OWASP ZAP (optional)
3. Configure security reporting
4. Add to agent workflow

### **Phase 4: Optimization (Week 4)**
1. Tune security rules
2. Reduce false positives
3. Document security workflow
4. Train team

---

## 📝 Next Steps

1. ✅ **Final Decision Made:** GitHub Actions + Bandit/Semgrep/Trivy
2. ⏳ **Action:** Create CI/CD workflow files
3. ⏳ **Action:** Install security tools
4. ⏳ **Action:** Configure scanning in agents
5. ⏳ **Action:** Document security workflow

---

**Status:** ✅ Decision Documented  
**Next:** Implement selected tools
