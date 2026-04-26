Design Approach (Explanation)

1. Separation of Concerns
tools/ → pure business logic (deterministic)
agents/ → orchestration (LangGraph)
config/ → environment control
main.py → interface layer

This keeps your system modular and extensible


2. LLM as Orchestrator, Not Executor

Instead of letting the LLM compute:

LLM decides what to do
Tools perform actual work

This avoids:

hallucinations
incorrect math
inconsistent outputs


3. LangGraph over Traditional Agents

You used:

explicit nodes (llm, tools)
conditional routing (should_continue)

This gives:

deterministic execution flow
debuggability
production readiness


4. Tool-Based Step Generation

Steps are deterministic
No hallucinated reasoning
Fully controllable output


5. Config-Driven Model Selection

Using config/settings.py:

Enables:

easy model switching
environment flexibility

