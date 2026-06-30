"""
mongodb.py

Purpose
-------
Creates a reusable MongoDB connection.

Every part of the project uses this file
instead of creating new MongoDB connections.
"""

from pymongo import MongoClient

from backend.config import (
    MONGO_URI,
    DATABASE_NAME
)


class MongoDB:

    def __init__(self):

        self.client = MongoClient(MONGO_URI)

        self.db = self.client[DATABASE_NAME]

        print("MongoDB Connected Successfully.")

    def get_database(self):
        """
        Return database object.
        """

        return self.db

    def get_collection(self, collection_name):
        """
        Return a collection object.
        """

        return self.db[collection_name]


# Singleton instance
mongo = MongoDB()

db = mongo.get_database()