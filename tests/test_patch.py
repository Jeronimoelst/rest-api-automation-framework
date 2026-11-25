from utils.api_client import patch_request

def test_patch_post():
    payload = {
    "title": "Título modificado mediante PATCH"
}
    response = patch_request("/posts/5", payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == payload["title"]
    
