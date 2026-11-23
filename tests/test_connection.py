from utils.api_client import get_request

def test_get_posts():
    response = get_request("/posts/1")
    assert response.status_code == 200


'''
Vamos a modificar test_get_posts() para comprobar tanto la respuesta HTTP como los datos.

Tu objetivo es incorporar estas tres validaciones:
1. Código HTTP igual a 200.
2. Identificador igual a 1.
3. Que el campo title no esté vacío.

'''