"""
main.py

Entry point of the Corporate CRAG Backend.

Responsibilities:
1. Create FastAPI application
2. Enable CORS
3. Create Upload Folder automatically
4. Include all API Routes
5. Register WebSocket routes
6. Start backend server
"""

import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.config import UPLOAD_FOLDER

# API Routes
from backend.routes.upload import router as upload_router
from backend.routes.chat import router as chat_router
from backend.routes.documents import router as documents_router
from backend.routes.history import router as history_router

# WebSocket Route
from backend.websocket.events import router as websocket_router


# -----------------------------------------------------
# Create Upload Folder
# -----------------------------------------------------

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# -----------------------------------------------------
# Create FastAPI App
# -----------------------------------------------------

app = FastAPI(
    title="Corporate Policy Intelligence Platform",
    description="Corrective RAG (CRAG) using LangGraph",
    version="1.0.0"
)


# -----------------------------------------------------
# Enable CORS
# -----------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------------------------------
# Home Route
# -----------------------------------------------------

@app.get("/")
def home():
    return {
        "project": "Corporate Policy Intelligence Platform",
        "backend": "FastAPI",
        "status": "Running"
    }


# -----------------------------------------------------
# Health Check
# -----------------------------------------------------

@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }


# -----------------------------------------------------
# Register API Routes
# -----------------------------------------------------

app.include_router(upload_router)
app.include_router(chat_router)
app.include_router(documents_router)
app.include_router(history_router)


# -----------------------------------------------------
# Register WebSocket Routes
# -----------------------------------------------------

app.include_router(websocket_router)


# -----------------------------------------------------
# Run with:
#
# uvicorn backend.main:app --reload
# -----------------------------------------------------