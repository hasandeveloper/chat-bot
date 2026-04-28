from langgraph.graph import StateGraph, START, END
from graph.state import State

from graph.nodes.load_memory import load_memory
from graph.nodes.retrieve_context import retrieve_context
from graph.nodes.generate_answer import generate_answer
from graph.nodes.store_memory import store_memory
from graph.nodes.summarize import summarize

def build_graph():
    graph = StateGraph(State)

    graph.add_node("load_memory", load_memory)
    graph.add_node("retrieve_context", retrieve_context)
    graph.add_node("generate_answer", generate_answer)
    graph.add_node("store_memory", store_memory)
    graph.add_node("summarize", summarize)

    graph.add_edge(START, "load_memory")
    graph.add_edge("load_memory", "retrieve_context")
    graph.add_edge("retrieve_context", "generate_answer")
    graph.add_edge("generate_answer", "store_memory")
    graph.add_edge("store_memory", "summarize")
    graph.add_edge("summarize", END)

    return graph.compile()