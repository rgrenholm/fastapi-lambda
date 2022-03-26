from pathlib import Path

from fastapi.testclient import TestClient
from fastapi import status

from api import app

client = TestClient(app)

test_image_path = Path(
    "tests", "test_data", "Starr_080731-9572_Monstera_deliciosa.jpeg"
)

with open(test_image_path, "rb") as f:
    decoded_image = f.read().decode("ISO-8859-1")


def test_api():
    response = client.post("/image", json={"decoded_image": decoded_image})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == "Monstera deliciosa"


def test_api_empty_body():
    response = client.post("/image", json={})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "decoded_image"],
                "msg": "field required",
                "type": "value_error.missing",
            }
        ]
    }
