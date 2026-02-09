from typing import TypedDict

class AgentState(TypedDict):
    project_path: str
    plan: str
    issues: str
    fixes: str
    review: str
