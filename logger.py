"""
logger.py

Purpose
-------
Stores workflow logs in MongoDB.

Every important step of the CRAG workflow
creates a log entry.

These logs are later displayed in the
frontend's Agent Evaluation panel.
"""

from backend.database.mongodb import mongo
from backend.database.models import Models


class WorkflowLogger:

    def __init__(self):

        self.collection = mongo.get_collection(
            "interaction_logs"
        )

    def log(
        self,
        step,
        message,
        status="SUCCESS"
    ):
        """
        Store a workflow log.
        """

        log_document = Models.create_log(

            step=step,

            message=message,

            status=status

        )

        self.collection.insert_one(
            log_document
        )

        print(
            f"[{status}] {step} : {message}"
        )

    def get_logs(self):
        """
        Return all workflow logs.
        """

        return list(

            self.collection.find(

                {},

                {
                    "_id": 0
                }

            )

        )

    def clear_logs(self):
        """
        Delete all logs.
        """

        self.collection.delete_many({})

        print("Workflow logs cleared.")