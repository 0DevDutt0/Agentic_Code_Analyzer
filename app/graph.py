from langgraph.graph import StateGraph
from app.schemas import AgentState
from app.agents import planner, analyzer, fixer, reviewer

graph = StateGraph(AgentState)

graph.add_node("planner", planner.run)
graph.add_node("analyzer", analyzer.run)
graph.add_node("fixer", fixer.run)
graph.add_node("reviewer", reviewer.run)

graph.set_entry_point("planner")
graph.add_edge("planner", "analyzer")
graph.add_edge("analyzer", "fixer")
graph.add_edge("fixer", "reviewer")

app = graph.compile()
