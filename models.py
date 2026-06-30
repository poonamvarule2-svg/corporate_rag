"""
models.py

Purpose
-------
Defines the structure of documents stored
in MongoDB.

Although MongoDB is schema-less, using
helper functions ensures every document
has a consistent format.
"""

from datetime import datetime
from uuid import uuid4


class Models:

    @staticmethod
    def create_user(name, email):
        """
        Create a user document.
        """

        return {

            "user_id": str(uuid4()),

            "name": name,

            "email": email,

            "created_at": datetime.utcnow()

        }


    @staticmethod
    def create_document(
        filename,
        total_pages,
        total_chunks
    ):
        """
        Store uploaded document information.
        """

        return {

            "document_id": str(uuid4()),

            "filename": filename,

            "total_pages": total_pages,

            "total_chunks": total_chunks,

            "uploaded_at": datetime.utcnow()

        }


    @staticmethod
    def create_chat(
        user_id,
        question,
        answer,
        citations
    ):
        """
        Store chat history.
        """

        return {

            "chat_id": str(uuid4()),

            "user_id": user_id,

            "question": question,

            "answer": answer,

            "citations": citations,

            "created_at": datetime.utcnow()

        }


    @staticmethod
    def create_log(
        step,
        message,
        status
    ):
        """
        Store workflow logs.
        """

        return {

            "log_id": str(uuid4()),

            "step": step,

            "message": message,

            "status": status,

            "timestamp": datetime.utcnow()

        }


    @staticmethod
    def create_metadata(
        filename,
        embedding_model,
        chunk_size,
        overlap
    ):
        """
        Store document metadata.
        """

        return {

            "metadata_id": str(uuid4()),

            "filename": filename,

            "embedding_model": embedding_model,

            "chunk_size": chunk_size,

            "chunk_overlap": overlap,

            "created_at": datetime.utcnow()

        }