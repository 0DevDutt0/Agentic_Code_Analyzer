from app.llms import planner_llm

def run(state):
    print("\n[Planner] Starting planning...")

    prompt = f"""
You are a planning agent.

Create a clear step-by-step plan to analyze the codebase at:
{state['project_path']}
"""
    plan = planner_llm.invoke(prompt)

    print("[Planner] Finished planning.")

    return {**state, "plan": plan}
