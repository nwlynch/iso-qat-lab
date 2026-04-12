# AGENTS.md - Multi-Agent QA Migration Lab

## Mission
Build a multi-agent local AI lab with Ollama-based LLMs to help a Quality Assurance company migrate from manual testing to AI-assisted enterprise workflows.

## Goal
Enable smooth migration from manual testing (with some automation) to AI-assisted enterprise where the current team becomes much more efficient.

---

## 🧪 QA Agent Architecture

### 1. 🧬 Test Generator Agent
**Purpose:** Creates test cases from requirements/specs
**Tasks:**
- Parse user stories and acceptance criteria
- Generate comprehensive test cases
- Create edge case scenarios
- Output in preferred test framework format (Selenium/Playwright/Jest)

### 2. 🤖 Test Executor Agent  
**Purpose:** Runs tests and captures results
**Tasks:**
- Execute test cases
- Capture screenshots and logs
- Record test durations and metrics
- Generate test execution reports

### 3. 📊 Analytics Agent
**Purpose:** Analyzes test results and generates insights
**Tasks:**
- Parse test execution results
- Calculate pass/fail rates
- Identify flaky tests
- Generate trend reports
- Suggest improvements

### 4. 🔍 Code Review Agent
**Purpose:** Reviews code changes and suggests improvements
**Tasks:**
- Review PRs and code changes
- Identify potential bugs
- Suggest test improvements
- Check for security vulnerabilities
- Review performance concerns

### 5. 🐛 Bug Hunter Agent
**Purpose:** Actively searches for issues and edge cases
**Tasks:**
- Generate fuzzing test cases
- Try unusual input combinations
- Find boundary condition failures
- Explore state machines
- Identify race conditions

### 6. 📋 Regression Agent
**Purpose:** Runs regression tests automatically
**Tasks:**
- Run full regression suite
- Detect new regressions
- Update baseline tests
- Compare against previous versions
- Report breaking changes

### 7. 📝 Documentation Agent
**Purpose:** Maintains test documentation and knowledge
**Tasks:**
- Generate test documentation
- Create test run reports
- Update test wikis
- Document test strategies
- Track test coverage

---

## 💬 Communication & Orchestration

### Agent Communication Pattern
- Agents communicate via shared artifacts in workspace
- Results stored in structured format (JSON/YAML)
- Central orchestration via cron/sessions
- Human-in-the-loop for critical decisions

### Workspace Organization
```
/qa-lab/
├── agents/
│   ├── test-generator/
│   ├── test-executor/
│   ├── analytics/
│   ├── code-review/
│   ├── bug-hunter/
│   ├── regression/
│   └── documentation/
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── e2e/
│   └── regression/
├── results/
│   ├── reports/
│   ├── logs/
│   └── metrics/
├── config/
│   ├── models/
│   └── frameworks/
└── docs/
```

---

## 🚀 Current Status

- **Models:** qwen3.5:9b (base model for all agents)
- **Status:** Lab setup in progress
- **Next Steps:**
  1. Set up agent scaffolding
  2. Define test framework integration
  3. Configure model parameters
  4. Build orchestration pipelines
  5. Train agents on test data

---

## 📚 Tech Stack

- **Orchestration:** Ollama + Local LLMs
- **Test Frameworks:** Selenium/Playwright (to be determined)
- **CI/CD:** Local git workflows + optional GitHub/GitLab integration
- **Storage:** Local file system for test artifacts
- **Reporting:** Markdown + HTML reports

---

## 🎯 Success Metrics

- **Efficiency:** 50%+ reduction in manual testing time
- **Coverage:** Automated test coverage >80%
- **Speed:** Test execution time reduced 3x
- **Quality:** Bug detection rate improved
- **Team:** Training on AI tools completed
