import ast
import json

from langchain_core.messages import ToolMessage, convert_to_messages
from pprint import pp

def print_response(response):
    for message in response["messages"]:
        print(type(message).__name__)
        print(message.content)

        if(hasattr(message, 'tool_calls')):
            print("tool call: ", message.tool_calls)

        if (isinstance(message, ToolMessage)):
             print("tool name: ", message.name)
             print("tool id: ", message.tool_call_id)

        print("\n" + "-"*50 + "\n")

    # print the structured response if available
    if "structured_response" in response:
        print("Structured Response:")
        pp(response["structured_response"])
#%% md
## 建立物料代理人 Material Agent
