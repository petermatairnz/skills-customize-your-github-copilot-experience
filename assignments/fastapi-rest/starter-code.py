from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# TODO: Create the Book model class here

app = FastAPI(
    title="Book Management API",
    description="A simple REST API for managing books",
    version="1.0.0"
)

# In-memory storage for books
books = []

# TODO: Implement the following endpoints:
# GET /books
# GET /books/{book_id}
# POST /books
# PUT /books/{book_id}
# DELETE /books/{book_id}

@app.get("/")
def read_root():
    """Root endpoint to verify API is running"""
    return {"message": "Welcome to the Book Management API"}

# Add your endpoints here...