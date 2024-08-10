from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_file():
    uid = "existing-file-uid"
    response = client.get(f"/file/{uid}/")

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/octet-stream"
