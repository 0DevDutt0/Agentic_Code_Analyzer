from app.llms import reviewer_llm


def run(state):
    print("\n[Reviewer] Reviewing proposed fixes...")

    fixes = state.get("fixes", "")

    prompt = f"""
You are a strict code reviewer.

Review the following proposed fixes:
{fixes}

Validate:
- Correctness
- Potential side effects
- Risks or regressions
- Trade-offs

Provide a final verdict and recommendations.
"""

    review = reviewer_llm.invoke(prompt)

    print("[Reviewer] Review completed.")

    return {
        **state,
        "review": review
    }
