import pytest
from fastapi.testclient import TestClient

from app.main import app, todos

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_todos():
    todos.clear()
    todos.update(
        {
            1: {
                "title": "TITLE",
                "description": "DESCRIPTION",
                "created_at": "2021-01-01T12:00:00",
            }
        }
    )


def test_get_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_get_todos():
    response = client.get("/todos")

    assert response.status_code == 200

    todos_response = response.json()

    assert len(todos_response) == 1
    assert "1" in todos_response
    assert todos_response["1"]["title"] == "TITLE"
    assert todos_response["1"]["description"] == "DESCRIPTION"


def test_get_todo():
    response = client.get("/todos/1")

    assert response.status_code == 200

    todo = response.json()

    assert todo["title"] == "TITLE"
    assert todo["description"] == "DESCRIPTION"


def test_get_todo_not_found():
    response = client.get("/todos/2")

    assert response.status_code == 404
    assert response.json() == {"detail": "Todo with ID 2 not found"}


def test_create_todo():
    response = client.post(
        "/todos",
        json={
            "title": "NEW TITLE",
            "description": "NEW DESCRIPTION",
        },
    )

    assert response.status_code == 200

    todo = response.json()

    assert todo["title"] == "NEW TITLE"
    assert todo["description"] == "NEW DESCRIPTION"


def test_update_todo():
    response = client.put(
        "/todos/1",
        json={
            "title": "UPDATED TITLE",
            "description": "UPDATED DESCRIPTION",
        },
    )

    assert response.status_code == 200

    todo = response.json()

    assert todo["title"] == "UPDATED TITLE"
    assert todo["description"] == "UPDATED DESCRIPTION"


def test_update_todo_not_found():
    response = client.put(
        "/todos/2",
        json={
            "title": "UPDATED TITLE",
            "description": "UPDATED DESCRIPTION",
        },
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Todo with ID 2 not found"}


def test_delete_todo():
    response = client.delete("/todos/1")
    assert response.status_code == 200

    todo = response.json()

    assert todo["title"] == "TITLE"
    assert todo["description"] == "DESCRIPTION"

    response = client.get("/todos")

    assert response.status_code == 200
    assert response.json() == {}
