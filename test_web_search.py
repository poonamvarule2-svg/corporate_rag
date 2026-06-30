from backend.rag.web_search import WebSearch

search = WebSearch()

results = search.search(
    "What is India's maternity leave policy?"
)

for result in results:

    print("=" * 80)

    print("Title")

    print(result["title"])

    print()

    print("Content")

    print(result["content"])

    print()

    print("URL")

    print(result["url"])