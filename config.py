"""
config.py

Central configuration file for the Corporate CRAG Platform.

Responsibilities
----------------
1. Load environment variables
2. Store application configuration
3. Provide constants used across the project
"""

import os
from dotenv import load_dotenv

# ==========================================================
# Load Environment Variables
# ==========================================================

load_dotenv()

# ==========================================================
# API Keys
# ==========================================================

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# ==========================================================
# MongoDB
# ==========================================================

MONGODB_URI = os.getenv(
    "MONGODB_URI",
    "mongodb://localhost:27017"
)

DATABASE_NAME = os.getenv(
    "DATABASE_NAME",
    "corporate_rag"
)

# ==========================================================
# ChromaDB
# ==========================================================

CHROMA_DB_PATH = os.getenv(
    "CHROMA_DB_PATH",
    "vector_db"
)

# ==========================================================
# Upload Folder
# ==========================================================

UPLOAD_FOLDER = os.getenv(
    "UPLOAD_FOLDER",
    "uploads"
)

# ==========================================================
# Embedding Model
# ==========================================================

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/all-MiniLM-L6-v2"
)

# ==========================================================
# Cross Encoder Model
# ==========================================================

CROSS_ENCODER_MODEL = os.getenv(
    "CROSS_ENCODER_MODEL",
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)

# ==========================================================
# Retrieval Settings
# ==========================================================

TOP_K_RESULTS = int(
    os.getenv("TOP_K_RESULTS", "5")
)

RELEVANCE_THRESHOLD = float(
    os.getenv("RELEVANCE_THRESHOLD", "0.80")
)

# ==========================================================
# Chunking Settings
# ==========================================================

MAX_CHUNK_SIZE = int(
    os.getenv("MAX_CHUNK_SIZE", "500")
)

CHUNK_OVERLAP = int(
    os.getenv("CHUNK_OVERLAP", "100")
)

# ==========================================================
# Web Search Settings
# ==========================================================

WEB_SEARCH_RESULTS = int(
    os.getenv("WEB_SEARCH_RESULTS", "3")
)