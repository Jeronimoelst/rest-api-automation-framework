from utils.api_client import put_request
import pytest


def test_update_post():
    
    payload = {
        "id": 5,
        "title": "Post actualizado",
        "body": "Actualización mediante PUT",
        "userId": 1
    }
    response = put_request("/posts/5", payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert data["id"] == payload["id"]