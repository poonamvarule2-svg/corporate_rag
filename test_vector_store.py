from backend.rag.pdf_loader import PDFLoader
from backend.rag.structure_parser import StructureParser
from backend.rag.chunker import Chunker
from backend.rag.embedder import Embedder
from backend.rag.vector_store import VectorStore

loader = PDFLoader("uploads/policy.pdf")

pages = loader.extract_text()

parser = StructureParser(pages)

sections = parser.parse()

chunker = Chunker()

chunks = chunker.chunk_sections(sections)

embedder = Embedder()

embedded_chunks = embedder.embed_chunks(chunks)

store = VectorStore()

store.delete_collection()

store.add_documents(embedded_chunks)

print()

print("Stored Documents")

print(store.count_documents())