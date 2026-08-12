import pytest
from src.views.user_register_view import UserRegisterView
from src.views.http_types.http_request import HttpRequest

# Testa se a view recebe o HTTP request, passa para o controller e devolve um HTTP response com o status code correto.

class UserRegisterControllerMock:
    def __init__(self):
        self.register_user_att = {}

    async def register_user(self, user_data: dict):
        self.register_user_att["user_data"] = user_data
        return {"type": "USERS", "count": 1, "attributes": user_data}

@pytest.mark.asyncio
async def test_register_user():
    controller = UserRegisterControllerMock()
    view = UserRegisterView(controller)

    user_data = {"user_name": "John Doe", "age": 30, "uf": "MG"}
    http_request = HttpRequest(body=user_data)

    response = await view.handle_register_user(http_request)

    assert controller.register_user_att["user_data"] == user_data
    assert response.status_code == 201
    assert response.body["type"] == "USERS"