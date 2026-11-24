from utils.api_client import post_request
import pytest


def test_create_post():
    payload = {
        "title": "Mi primer test API",
        "body": "Prueba automatizada con Pytest",
        "userId": 1
    }
    
    response = post_request("/posts", payload)
    assert response.status_code == 201
    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data