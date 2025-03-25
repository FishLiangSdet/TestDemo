import pytest
import allure
from utils.request_handler import APIRequest

api = APIRequest()


@allure.feature("login")
def test_login_success():
    payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = api.send_request("POST", "/api/login", data=payload)

    assert response.status_code == 200
    assert "token" in response.json()
