from backend.rag.pdf_loader import PDFLoader
from backend.rag.structure_parser import StructureParser
from backend.rag.chunker import Chunker

loader = PDFLoader("uploads/policy.pdf")

pages = loader.extract_text()

parser = StructureParser(pages)

sections = parser.parse()

chunker = Chunker()

chunks = chunker.chunk_sections(sections)

for chunk in chunks:

    print("=" * 60)

    print("Chunk ID :", chunk["chunk_id"])

    print("Section :", chunk["section"])

    print("Page :", chunk["page"])

    print(chunk["text"])