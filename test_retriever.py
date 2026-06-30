from backend.rag.retriever import Retriever

retriever = Retriever()

query = "How many annual leaves are allowed?"

results = retriever.retrieve(query)

print("=" * 80)

print("Retrieved Chunks")

print("=" * 80)

for result in results:

    print()

    print("Chunk ID :", result["chunk_id"])

    print("Section :", result["section"])

    print("Page :", result["page"])

    print("Distance :", result["distance"])

    print()

    print(result["text"])