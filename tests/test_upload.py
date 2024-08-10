from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_upload_file():
    with open("tests/test_file.txt", "wb") as f:
        f.write(b"Test file content")

    with open("tests/test_file.txt", "rb") as f:
        response = client.post("/upload/", files={"file": f})

    assert response.status_code == 200
    assert "uid" in response.json()
