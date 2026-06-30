from backend.rag.citation import CitationGenerator

answer = "Employees receive 20 annual leaves."

chunks = [

    {

        "section":"Leave Policy",

        "page":4

    },

    {

        "section":"Attendance",

        "page":7

    }

]

citation = CitationGenerator()

result = citation.generate(
    answer,
    chunks
)

print()

print(citation.format_for_display(result))