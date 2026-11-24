from utils.api_client import get_request
import pytest

@pytest.mark.parametrize('post_id' , [1,2,3,4,5])

def test_get_posts(post_id):
    response = get_request(f"/posts/{post_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == post_id
    assert isinstance(data["userId"], int)
    assert data["title"] != ""
    assert isinstance(data["title"], str)

def test_get_post_not_found():
    response = get_request("/posts/9999")

    assert response.status_code == 404

