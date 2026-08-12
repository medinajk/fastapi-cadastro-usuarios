import pytest
from src.views.user_finder_view import UserFinderView
from src.views.http_types.http_request import HttpRequest

# Testa se a view recebe o HTTP request, passa para o controller e devolve um HTTP response com o status code correto.

class UserFinderControllerMock:
    def __init__(self):
        self.find_user_by_name_att = {}

    async def find_user_by_name(self, user_name: str):
        self.find_user_by_name_att["user_name"] = user_name
        return {"type": "USERS", "count": 1, "attributes": [{"user_name": user_name}]}

@pytest.mark.asyncio
async def test_find_user_by_name():
    controller = UserFinderControllerMock()
    view = UserFinderView(controller)

    http_request = HttpRequest(path_params={"user_name": "John Doe"})

    response = await view.handle_find_user_by_name(http_request)

    assert controller.find_user_by_name_att["user_name"] == "John Doe"
    assert response.status_code == 200
    assert response.body["type"] == "USERS"
