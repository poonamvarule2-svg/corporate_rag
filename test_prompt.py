from backend.rag.prompt import PromptBuilder

builder = PromptBuilder()

chunks = [
    {
        "section": "Leave Policy",
        "page": 3,
        "text": "Employees receive 20 annual leaves."
    }
]

web = [
    {
        "title": "Leave Law",
        "content": "Annual leave varies by company.",
        "url": "https://example.com"
    }
]

prompt = builder.build_prompt(
    query="How many annual leaves?",
    document_chunks=chunks,
    web_results=web
)

print(prompt)