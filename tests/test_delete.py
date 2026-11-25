from utils.api_client import delete_request

def test_delete_post():
    response = delete_request("/posts/5")
    assert response.status_code in(200,204)