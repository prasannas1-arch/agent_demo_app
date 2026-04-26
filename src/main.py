from langchain_core.messages import HumanMessage
from agents.graph_agent import build_graph

def run():
    graph = build_graph()

    print("Agent is ready! Type 'exit' to quit.\n")

    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break

        result = graph.invoke({
            "messages": [HumanMessage(content=user_input)]
        })

        last_msg = result["messages"][-1]

        # Tool output is usually inside content or additional_kwargs
        print("\n--- RESULT ---")

        if isinstance(last_msg.content, dict):
            data = last_msg.content
        else:
            data = last_msg.additional_kwargs.get("tool_output", {})

        if isinstance(data, dict) and "steps" in data:
            print("Steps:")
            for step in data["steps"]:
                print(step)
            print("Final Answer:", data["result"])
        else:
            print("AI:", last_msg.content)


if __name__ == "__main__":
    run()