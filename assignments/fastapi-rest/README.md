# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective
Create a modern REST API using the FastAPI framework to build a simple book management system. This assignment will teach you how to design and implement API endpoints, handle different HTTP methods, work with data models, and document your API automatically.

## 📝 Tasks

### 🛠️ Task 1: API Setup and Basic Endpoints

#### Description
Set up a FastAPI application and implement basic CRUD operations for managing books.

#### Requirements
Completed program should:
- Initialize a FastAPI application
- Create a Book data model using Pydantic with fields: id, title, author, year, genre
- Implement GET /books endpoint to list all books
- Implement GET /books/{book_id} endpoint to retrieve a specific book
- Add proper type hints and documentation for each endpoint

### 🛠️ Task 2: Advanced API Features

#### Description
Implement create, update, and delete operations with proper validation and error handling.

#### Requirements
Completed program should:
- Implement POST /books endpoint to add a new book
- Implement PUT /books/{book_id} endpoint to update a book
- Implement DELETE /books/{book_id} endpoint to remove a book
- Add input validation for all endpoints
- Implement proper error handling and status codes
- Include query parameters for filtering books by author or genre

### 🛠️ Task 3: API Documentation and Testing

#### Description
Add documentation, implement basic testing, and enhance the API with additional features.

#### Requirements
Completed program should:
- Add detailed API documentation using FastAPI's built-in swagger UI
- Write at least 3 test cases using pytest
- Implement pagination for the GET /books endpoint
- Add a search endpoint that allows searching books by title
- Include proper logging for API requests