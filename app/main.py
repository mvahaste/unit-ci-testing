from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime

app = FastAPI()


todos = {}


def error(message: str, status_code: int = 400):
    """
    Helper function to return a simple error response.

    :param message: The error message to be included in the response.
    :param status_code: The HTTP status code (default is 400 for Bad Request).
    :return: A JSONResponse with the error message.
    """
    return JSONResponse(
        content={"detail": message},
        status_code=status_code,
    )


@app.get("/")
def get_root():
    """
    A simple function to return a greeting message.

    :return: A dictionary with a message key.
    """
    return {"message": "Hello, World!"}


@app.get("/todos")
def get_todos():
    """
    A function to return all the todos.

    :return: A dictionary with all the todos.
    """
    return todos


@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    """
    A function to return a specific todo.

    :param todo_id: The ID of the todo to be returned.
    :return: A dictionary with the todo details.
    """
    if todo_id not in todos:
        return error(f"Todo with ID {todo_id} not found", 404)

    return todos[todo_id]


@app.post("/todos")
def create_todo(todo: dict):
    """
    A function to create a new todo.

    :param todo: A dictionary with the todo details.
    :return: A dictionary with the newly created todo details.
    """
    todo_id = max(todos.keys()) + 1

    if "title" not in todo:
        return error("Title is required")

    # Add timestamp in ISO format
    todo["created_at"] = datetime.now().isoformat()

    todos[todo_id] = todo

    return todos[todo_id]


@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: dict):
    """
    A function to update an existing todo.

    :param todo_id: The ID of the todo to be updated.
    :param todo: A dictionary with the updated todo details.
    :return: A dictionary with the updated todo details.
    """
    if todo_id not in todos:
        return error(f"Todo with ID {todo_id} not found", 404)
    elif "title" not in todo:
        return error("Title is required")

    todos[todo_id].update(todo)

    return todos[todo_id]


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    """
    A function to delete a todo.

    :param todo_id: The ID of the todo to be deleted.
    :return: A dictionary with the deleted todo details.
    """
    if todo_id not in todos:
        return error(f"Todo with ID {todo_id} not found", 404)

    todo = todos.pop(todo_id)

    return todo
