import json
from pathlib import Path
import requests

from fastapi import status


def request_params(body):

    ip = "localhost"
    port = ":8080"

    url = "http://%s%s/2015-03-31/functions/function/invocations" % (ip, port)

    payload = {
        "resource": "/image",
        "path": "/image",
        "httpMethod": "POST",
        "requestContext": {},
        "body": json.dumps(body),
    }

    headers = {"content-type": "application/json"}

    return {
        "url": url,
        "json": payload,
        "headers": headers,
    }


test_image_path = Path(
    "tests", "test_data", "Starr_080731-9572_Monstera_deliciosa.jpeg"
)

with open(test_image_path, "rb") as f:
    decoded_image = f.read().decode("ISO-8859-1")


def test_api():

    body = {"decoded_image": decoded_image}

    response = requests.post(**request_params(body))
    assert response.status_code == status.HTTP_200_OK
    response_json = response.json()
    assert response_json["statusCode"] == status.HTTP_200_OK
    assert json.loads(response_json["body"]) == "Monstera deliciosa"


def test_api_empty_body():
    body = {}

    response = requests.post(**request_params(body))
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["statusCode"] == status.HTTP_422_UNPROCESSABLE_ENTITY
