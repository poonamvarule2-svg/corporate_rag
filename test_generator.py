from backend.rag.retriever import Retriever
from backend.rag.grader import Grader
from backend.rag.generator import Generator

query = "How many annual leaves are employees entitled to?"

retriever = Retriever()

chunks = retriever.retrieve(query)

grader = Grader()

graded_chunks = grader.grade(query, chunks)

generator = Generator()

result = generator.generate(
    query,
    graded_chunks
)

print("=" * 80)

print(result["answer"])