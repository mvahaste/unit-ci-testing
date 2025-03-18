# 📝 Learning Unit Testing & CI Pipelines

This project is a simple FastAPI-based application designed to manage a todo list. I made it to learn FastAPI, testing with pytest, and integrating GitHub Actions for continuous integration (CI).

# Table of contents

1.  [🎨 Features](#🎨-features)
2.  [🗂️ Application Structure](#🗂️-application-structure)
3.  [⚙️ Installation](#⚙️-installation)
4.  [📡 Endpoints](#📡-endpoints)
5.  [🧪 Testing](#🧪-testing)
6.  [🚀 GitHub Actions](#🚀-github-actions)

## 🎨 Features

- **Create a Todo**: Add a new todo item with a title and optional description.
- **Read Todos**: View all todos or a specific todo by its ID.
- **Update a Todo**: Modify the title or description of an existing todo.
- **Delete a Todo**: Remove a todo from the list.
- **Error Handling**: The app provides error responses when a resource is not found or when required data is missing.

## 🗂️ Application Structure

- `app/main.py`: Contains the FastAPI application and its routes.
- `tests/test_main.py`: Contains tests for the application using `pytest` and FastAPI's test client.

## ⚙️ Installation

To run the project locally, follow these steps:

1. Clone the repository:

```
git clone https://github.com/mvahaste/unit-ci-testing
cd unit-ci-testing
```

2. Create a virtual environment (optional but recommended):

```
python3 -m venv venv
source venv/bin/activate
```

3. Install the dependencies:

```
python3 -m pip install -r requirements.txt
```

4. Run the application:

```
uvicorn app.main:app --reload
```

Your FastAPI app will be running at http://127.0.0.1:8000.

## 📡 Endpoints

- GET /: Returns a greeting message.
- GET /todos: Returns all todos.
- GET /todos/{todo_id}: Returns a specific todo by ID.
- POST /todos: Creates a new todo.
- PUT /todos/{todo_id}: Updates an existing todo.
- DELETE /todos/{todo_id}: Deletes a todo by ID.

## 🧪 Testing

This project includes tests to ensure the functionality of the application. Tests are written using pytest and FastAPI’s test client.

To run the tests, use the following command:

```
pytest -v --tb=short --disable-warnings
```

## 🚀 GitHub Actions

This project includes GitHub Actions for continuous integration. It automatically runs tests whenever changes are pushed to the repository.
