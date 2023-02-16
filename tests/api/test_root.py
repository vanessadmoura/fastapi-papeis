from fastapi.testclient import TestClient


def test_get_root(client: TestClient) -> None:
    response = client.get("/")
    body = response.json()
    assert response.status_code == 200
    assert body["mensagem"] == "api de papeis"


# def test_get_error_root(client: TestClient) -> None:
#     response = client.get("/errado")
#     assert response.status_code == 404


