from backend.graph.workflow import build_workflow

workflow = build_workflow()

state = {

    "query": "How many annual leaves are employees entitled to?",

    "rewritten_query": "",

    "retrieved_chunks": [],

    "graded_chunks": [],

    "retrieval_passed": False,

    "answer": "",

    "citations": [],

    "response": {}

}

result = workflow.invoke(state)

print()

print("=" * 80)

print(result["response"])