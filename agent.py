from typing import Annotated, Sequence, TypedDict
from langchain_core.messages import BaseMessage
from langgraph.graph import add_messages, StateGraph, START


class GraphState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]

def node1(state: GraphState) -> str:
    return {"messages": BaseMessage(content="Hello", name="node1")}

graph_builder = StateGraph(GraphState)
graph_builder.add_node("node1", node1)
graph_builder.add_edge(START, "node1")

graph = graph_builder.compile()
