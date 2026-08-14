from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface
from src.errors.types.http_bad_request_error import HttpBadRequestError
from src.controllers.interfaces.user_register import UserRegisterInterface

class UserRegister(UserRegisterInterface):
    def __init__(self, users_repository: UsersRepositoryInterface):
        self.users_repository = users_repository

    async def register_user(self, user_data: dict) -> dict:
        self.__validate_user_data(user_data)
        await self.__registry_user(user_data)
        return self.__format_response(user_data)

    def __validate_user_data(self, user_data: dict) -> None:
        age = user_data["age"]
        uf = user_data["uf"].upper()

        if uf not in ["MG", "BA", "CE", "SC", "MT"]:
            raise HttpBadRequestError("Estado invalido para cadastro")

        if age < 0 or age > 120:
            raise HttpBadRequestError("Idade invalida para cadastro")

    async def __registry_user(self, user_data: dict) -> None:
        await self.users_repository.insert_users(user_data)

    def __format_response(self, user_data: dict) -> dict:
        return {
            "type": "USERS",
            "count": 1,
            "attributes": user_data
        }