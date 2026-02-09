from langchain_ollama import OllamaLLM
import os

OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://host.docker.internal:11434"
)

planner_llm = OllamaLLM(
    model="deepseek-r1:32b",
    temperature=0.2,
    base_url=OLLAMA_BASE_URL
)

analyzer_llm = OllamaLLM(
    model="qwen3-coder:30b",
    temperature=0.1,
    base_url=OLLAMA_BASE_URL
)

fixer_llm = OllamaLLM(
    model="qwen3-coder:30b",
    temperature=0.1,
    base_url=OLLAMA_BASE_URL
)

reviewer_llm = OllamaLLM(
    model="llama3.1:8b",
    temperature=0.2,
    base_url=OLLAMA_BASE_URL
)