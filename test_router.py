from backend.graph.router import retrieval_router

state = {
    "retrieval_passed": True
}

print(retrieval_router(state))

state = {
    "retrieval_passed": False
}

print(retrieval_router(state))