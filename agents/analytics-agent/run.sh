#!/bin/bash
# 📊 Analytics Agent - Execution Script

echo "📊 Analytics Agent Starting..."

SESSION=$(sessions_spawn \
  --runtime subagent \
  --mode session \
  --label "Analytics Agent" \
  --agent-id analytics-agent \
  --task "Analyze test results and generate insights" \
  --stream-to parent \
)

echo "Session created: $SESSION"

sleep 30

echo "✅ Analytics Agent completed"
