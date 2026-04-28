# Model Selection Rules (Configuration)

## Goal
To ensure optimal performance, agents must select the best-suited LLM model for their specific task, rather than defaulting to a single model.

## Model Hierarchy
1.  **Primary Model (Default):** `qwen3.5:9b` (Assumed to be the best general-purpose LLM for the lab).
2.  **Fallback Model:** `gemma4:e4b` (Used only if the primary model fails, times out, or is unavailable).

## Task-Specific Model Guidelines (Guidance for Agents)
This section details which model capability is best for which agent's role.

| Agent | Primary Task | Suggested Model Capability | Notes |
| :--- | :--- | :--- | :--- |
| **Test Generator** | Creative requirement parsing, generating varied test logic. | Highly creative/Contextual LLM (e.g., GPT-4, if available, otherwise stick to Primary) | Needs strong understanding of natural language specs. |
| **Test Executor** | Test execution control flow, environment interaction. | N/A (This agent primarily *runs* code, not generating text/logic). | Needs external tooling integration (Playwright bindings). |
| **Analytics Agent** | Data parsing (JSON/YAML), statistical reporting, trend identification. | Strong reasoning/Data processing LLM. | Needs high accuracy in interpretation. |
| **Code Review Agent** | Code analysis, security checks, performance suggestions. | Code-specialized LLM (e.g., Gemini Code, specialized model). | Best performance comes from models fine-tuned on code. |
| **Bug Hunter Agent** | Fuzzing, boundary condition exploration, lateral thinking. | Highly creative/Adversarial LLM. | Needs to think outside the direct scope of the requirement. |
| **Regression Agent** | Systematic execution, baseline comparison. | Reliable, deterministic LLM. | Consistency is key. |
| **Documentation Agent** | Synthesis, report writing, knowledge base updating. | Excellent natural language generation (NLG) LLM. | Needs to write cleanly and formally. |

**Fallback Logic:** If the primary model fails for any reason, attempt the fallback model (`gemma4:e4b`). If the fallback fails, report the failure and halt the process gracefully.