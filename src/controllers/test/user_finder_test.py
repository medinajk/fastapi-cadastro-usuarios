import pytest
from src.controllers.user_finder import UserFinder

class UserRepositoryMock:
    def __init__(self):
        self.get_users_by_name_att = {}  # método construtor para armazenar os dados de busca simulados

    async def get_users_by_name(self, user_name: str) -> list[dict]:
        self.get_users_by_name_att["user_name"] = user_name  # Simula a busca de dados no banco de dados
        return [{"first_name": "Ola"}, {"last_name": "Mundo"}]

@pytest.mark.asyncio
async def test_find_user_by_name():
    user_repo = UserRepositoryMock()
    user_finder = UserFinder(user_repo)
    user_name = "Bianca"

    response = await user_finder.find_user_by_name(user_name)

    assert user_repo.get_users_by_name_att["user_name"] == user_name

    assert response["type"] == "USERS"
    assert response["count"] == 2
    assert "attributes" in response
    # verifica se retorna uma lista
    assert isinstance(response["attributes"], list)