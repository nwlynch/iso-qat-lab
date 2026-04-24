# 🛡️ Sandbox Safety Notice

## Environment Status
We are running in a **sandbox environment** to protect against external attacks. This is by design! 🔒

## What This Means

### ✅ Safe Operations
- **Local AI infrastructure** - Ollama models running locally
- **File system access** - Full workspace access
- **Model inference** - Using inference.local/v1
- **Local file operations** - Create, read, modify files
- **No external network** - Restricted to prevent data exfiltration

### ⚠️ Known Limitations
- Some CLI commands may not be directly accessible
- Need to use sessions/subagents for complex tasks
- Network access restricted
- Direct HTTP API calls may be blocked

### 🚀 Workarounds
- Use `sessions_spawn` to run agent sessions
- Use gateway for model inference
- Work within the available file system
- Use available tools (web_fetch, browser if available)

## Safety Guidelines

1. **Don't try to bypass sandbox** - It's there for a reason!
2. **Use available tools** - Sessions, gateway, file operations
3. **Document everything** - Use MEMORY.md, AGENTS.md
4. **Respect constraints** - Work with what we have

## Current Environment
- **Sandbox:** Active (for safety)
- **Gateway:** inference.local/v1
- **Model:** qwen3.5:9b (default)
- **Access:** Local file system only

---

See `README.md` for project overview and `AGENTS.md` for agent descriptions.
