from app.llms import fixer_llm


def run(state):
    print("\n[Fixer] Generating fixes and improvements...")

    issues = state.get("issues", "")

    prompt = f"""
You are a senior software engineer and refactoring agent.

Given the following identified issues:
{issues}

Propose:
- Concrete fixes
- Refactored code suggestions
- Better design patterns (if applicable)
- Performance improvements

Explain each fix briefly and clearly.
"""

    fixes = fixer_llm.invoke(prompt)

    print("[Fixer] Fix generation completed.")

    return {
        **state,
        "fixes": fixes
    }
