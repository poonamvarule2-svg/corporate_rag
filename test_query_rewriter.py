from backend.rag.query_rewriter import QueryRewriter

rewriter = QueryRewriter()

query = "Vacation rules?"

new_query = rewriter.rewrite(query)

print()

print("Original")

print(query)

print()

print("Rewritten")

print(new_query)