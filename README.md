# 🧠 LangGraph Tool-Based Agent (Math + String Operations)

This project implements a **tool-using AI agent** using **LangGraph + LangChain + Ollama (local LLM)**.

The agent can:

* Perform **math operations** (addition, subtraction, multiplication, division)
* Perform **string operations** (uppercase, lowercase, reverse, count etc.)
* Show **step-by-step solutions for math problems**

---

## 🚀 Tech Stack

* Python 3.10+
* LangChain ≥ 1.2.x
* LangGraph ≥ 1.1.x
* Ollama (local LLM runtime)
* Model: `llama3-groq-tool-us`

---

## 📁 Project Structure

```
project/src
│
├── config/
│   └── settings.py        # Central config (model, temperature)
│
├── tools/
│   ├── math_tools.py      # Math tools with steps
│   └── string_tools.py    # String transformation tools
│
├── agents/
│   └── graph_agent.py     # LangGraph agent definition
│
├── docs/
│   └── assumptions.md     # Project assumptions and Improvements
│   └── design_approach.md  # Project design decisions
└── main.py                # CLI entry point
```

---

## ⚙️ Setup Instructions

### 1. Install dependencies

```bash
pip install langchain langgraph langchain-community
```

---

### 2. Install and run Ollama

Download: https://ollama.com

Run the model:

```bash
ollama run llama3-groq-tool-use
```

---

### 3. Configure model (optional)

Edit:

```
config/settings.py
```

```python
MODEL_NAME = "llama3-groq-tool-use"
TEMPERATURE = 0
```

---

### 4. Run the application

```bash
python main.py
```

---

## 💬 Example Inputs

```
Add 5 and 3
Multiply 4 and 6
Subtract 10 from 25

Convert "hello" to uppercase
Reverse "LangGraph"
```

---

## 🧾 Example Output

```
Steps:
1. Take first number = 5
2. Take second number = 3
3. Add them → 5 + 3 = 8

Final Answer: 8
```

---

## ⚠️ Notes

* This agent **strictly uses tools** (no direct LLM computation)
* Step-by-step output comes from tool responses
* Tool calling reliability depends on the LLM (Ollama models may vary)

---

## 📌 Future Improvements

* Add advanced math
* Add memory (conversation history)
* Build REST API (FastAPI)
* Guardrails for prompt Input and LLM output
* Add UI (React)

---
