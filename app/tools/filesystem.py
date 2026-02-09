from pathlib import Path

def list_files(path: str) -> list[str]:
    base = Path(path)
    if not base.exists():
        return []
    return [str(p) for p in base.rglob("*") if p.is_file()]

def read_file(path: str) -> str:
    try:
        return Path(path).read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        return f"ERROR: {e}"
