# AI Integration Guidelines

## How AI is Used
The Smart Task Manager uses AI to automatically suggest task priorities (`LOW`, `MEDIUM`, `HIGH`) based on the natural language description provided by the user. This reduces cognitive load when planning tasks.

## Prompt Design
*(If integrated with an LLM like Gemini or OpenAI)*
System Prompt: "You are a task prioritization assistant. Read the following task description and output ONLY one of the following words based on urgency and importance: LOW, MEDIUM, HIGH."

## Constraints and Risks
- **Hallucination Risk:** The AI might return an invalid priority string.
- **Latency Risk:** Calling an external API can be slow or time out.
- **Cost Risk:** High volume of task creations could spike API costs.

## Validation Strategy & Fallback
To ensure the system remains robust:
1. **Input Validation:** The AI response is evaluated and assigned ONLY if it matches strict enums (`["LOW", "MEDIUM", "HIGH"]`).
2. **Fallback Mechanism:** If the AI call fails, times out, or returns an invalid string, the system safely catches the exception and falls back to saving the task with `LOW` priority instead of breaking the flow.
3. **Mock Implementation:** Currently, to demonstrate the architecture without external dependencies, a safe mock (`backend/utils/ai.py`) uses heuristic keyword matching ('urgent', 'soon'). This ensures the core application never breaks while simulating the AI integration.
