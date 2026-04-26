from typing import TypedDict, Annotated
import operator
from langchain_core.messages import BaseMessage, AIMessage, SystemMessage
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
# Import tools
from tools.math_tools import MATH_TOOLS
from tools.string_tools import STRING_TOOLS
from config.settings import MODEL_NAME, TEMPERATURE
from data.prompts.system_prompt import SYSTEM_PROMPT

# Combine all tools
tools = MATH_TOOLS + STRING_TOOLS


# Agent State
class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], operator.add]

# LLM Setup
llm = ChatOllama(
    model=MODEL_NAME,
    temperature=TEMPERATURE
)

# Bind tools
llm_with_tools = llm.bind_tools(tools)


# LLM Node
def llm_node(state: AgentState):
    messages = state["messages"]

    # Ensure system prompt is always present as first message
    if not any(isinstance(msg, SystemMessage) for msg in messages):
        messages = [SystemMessage(content=SYSTEM_PROMPT)] + messages

    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}

# Tool Node
tool_node = ToolNode(tools)


# Router
def should_continue(state: AgentState):
    last_message = state["messages"][-1]

    if isinstance(last_message, AIMessage) and last_message.tool_calls:
        return "tools"
    return "end"


# Build Graph
def build_graph():
    builder = StateGraph(AgentState)

    builder.add_node("llm", llm_node)
    builder.add_node("tools", tool_node)

    builder.set_entry_point("llm")

    builder.add_conditional_edges(
        "llm",
        should_continue,
        {
            "tools": "tools",
            "end": END
        }
    )

    builder.add_edge("tools", "llm")

    return builder.compile()