#!/bin/bash
# 📋 Regression Agent - Execution Script

echo "📋 Regression Agent Starting..."

SESSION=$(sessions_spawn \
  --runtime subagent \
  --mode session \
  --label "Regression Agent" \
  --agent-id regression-agent \
  --task "Run regression tests and compare with baseline" \
  --stream-to parent \
)

echo "Session created: $SESSION"

sleep 30

echo "✅ Regression Agent completed"
