#!/bin/bash
# 📝 Documentation Agent - Execution Script

echo "📝 Documentation Agent Starting..."

SESSION=$(sessions_spawn \
  --runtime subagent \
  --mode session \
  --label "Documentation Agent" \
  --agent-id documentation-agent \
  --task "Generate test documentation and reports" \
  --stream-to parent \
)

echo "Session created: $SESSION"

sleep 30

echo "✅ Documentation Agent completed"
