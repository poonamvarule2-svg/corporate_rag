from backend.rag.pdf_loader import PDFLoader
from backend.rag.structure_parser import StructureParser
from backend.rag.chunker import Chunker
from backend.rag.embedder import Embedder

loader = PDFLoader("uploads/policy.pdf")

pages = loader.extract_text()

parser = StructureParser(pages)

sections = parser.parse()

chunker = Chunker()

chunks = chunker.chunk_sections(sections)

embedder = Embedder()

embedded_chunks = embedder.embed_chunks(chunks)

print("=" * 80)

print("Number of Chunks:", len(embedded_chunks))

print("=" * 80)

print("First Chunk")

print(embedded_chunks[0]["text"])

print("=" * 80)

print("Embedding Length")

print(len(embedded_chunks[0]["embedding"]))