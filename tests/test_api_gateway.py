import os
from pathlib import Path
import requests

from fastapi import status

url = os.environ["API_URL"] + "/image"

headers = {"content-type": "application/json"}

test_image_path = Path(
    "tests", "test_data", "Starr_080731-9572_Monstera_deliciosa.jpeg"
)

with open(test_image_path, "rb") as f:
    decoded_image = f.read().decode("ISO-8859-1")


def test_api():
    response = requests.post(
        url=url,
        json={"decoded_image": decoded_image},
        headers=headers,
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == "Monstera deliciosa"
