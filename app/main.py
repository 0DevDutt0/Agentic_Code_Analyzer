from app.graph import app


def main():
    print("Agentic Code Analyzer")
    print("---------------------")

    project_path = input(
        "Enter the path to the codebase you want to analyze: "
    ).strip()

    if not project_path:
        print("No path provided. Exiting.")
        return

    result = app.invoke({
        "project_path": project_path,
        "plan": "",
        "issues": "",
        "fixes": "",
        "review": ""
    })

    print("\n===== PLAN =====\n")
    print(result["plan"])

    print("\n===== ISSUES =====\n")
    print(result["issues"])

    print("\n===== FIXES =====\n")
    print(result["fixes"])

    print("\n===== REVIEW =====\n")
    print(result["review"])


if __name__ == "__main__":
    main()
