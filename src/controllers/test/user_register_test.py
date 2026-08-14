import pytest
from src.errors.types.http_bad_request_error import HttpBadRequestError
from src.controllers.user_register import UserRegister

# Testa se o controller valida os dados e salva no banco corretamente

class UserRepositoryMock:
    def __init__(self):
        self.insert_users_att = {} # método construtor para armazenar os dados de inserção simulados

    async def insert_users(self, user_data: dict):
        self.insert_users_att["user_data"] = user_data  # Simula a inserção de dados no banco de dados

@pytest.mark.asyncio
async def test_register_user():
    user_repository = UserRepositoryMock()
    user_register = UserRegister(user_repository)

    user_data = {
        "user_name": "John Doe",
        "age": 30,
        "uf": "MG"
    }

    response = await user_register.register_user(user_data)
    print(response)

    assert user_repository.insert_users_att["user_data"] == user_data

    assert response["type"] == "USERS"
    assert response["count"] == 1
    assert response["attributes"] == user_data

@pytest.mark.asyncio
async def test_register_user_error_uf():
    user_repository = UserRepositoryMock()
    user_register = UserRegister(user_repository)

    user_data = {
        "user_name": "John Doe",
        "age": 30,
        "uf": "ES"
    }

    with pytest.raises(HttpBadRequestError) as excinfo:
        await user_register.register_user(user_data)

    # valida se a mensagem de erro lançada é a esperada
    assert str(excinfo.value) == "Estado invalido para cadastro"

    assert user_repository.insert_users_att == {}  # Verifica se não houve inserção de dados no banco de dados

    @pytest.mark.asyncio
    async def test_register_user_error_age():
        user_repository = UserRepositoryMock()
        user_register = UserRegister(user_repository)

        user_data = {
            "user_name": "John Doe",
            "age": 130,
            "uf": "MG"
        }

        with pytest.raises(HttpBadRequestError) as excinfo:
            await user_register.register_user(user_data)

        assert str(excinfo.value) == "Idade invalida para cadastro"