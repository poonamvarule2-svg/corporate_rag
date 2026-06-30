from backend.database.logger import WorkflowLogger

logger = WorkflowLogger()

logger.clear_logs()

logger.log(

    step="Retriever",

    message="Retrieved 5 chunks."

)

logger.log(

    step="Grader",

    message="Average relevance score = 0.94"

)

logger.log(

    step="Generator",

    message="Generated final answer."

)

logs = logger.get_logs()

print()

for log in logs:

    print(log)