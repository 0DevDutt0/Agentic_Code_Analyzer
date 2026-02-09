from app.llms import analyzer_llm
from app.tools.filesystem import list_files, read_file
from pathlib import Path

ALLOWED_EXTENSIONS = {".py", ".js", ".ts", ".java", ".cpp", ".c", ".cs"}
IGNORE_DIRS = {"__pycache__", ".git", ".venv", "node_modules"}
MAX_FILES = 40
MAX_CHARS_PER_FILE = 4000


def run(state):
    print("\n[Analyzer] Reading project files...")

    project_path = Path(state["project_path"])
    all_files = list_files(str(project_path))

    filtered_files = []
    for f in all_files:
        path = Path(f)

        if any(part in IGNORE_DIRS for part in path.parts):
            continue

        if path.suffix not in ALLOWED_EXTENSIONS:
            continue

        filtered_files.append(path)

        if len(filtered_files) >= MAX_FILES:
            break

    print(f"[Analyzer] Analyzing {len(filtered_files)} source files...")

    combined = []
    for path in filtered_files:
        content = read_file(str(path))[:MAX_CHARS_PER_FILE]
        combined.append(f"\nFILE: {path}\n{content}")

    code_context = "\n".join(combined)

    prompt = f"""
You are a senior code analysis agent.

Analyze the following codebase:

{code_context}

Identify:
- Bugs
- Code smells
- Performance issues
- Design problems

Reference filenames where applicable.
"""

    issues = analyzer_llm.invoke(prompt)

    return {
        **state,
        "issues": issues
    }
