from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface
from src.controllers.interfaces.user_finder import UserFinderInterface

class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UsersRepositoryInterface):
        self.users_repository = users_repository

    async def find_user_by_name(self, user_name: str) -> dict:
        users = await self.users_repository.get_users_by_name(user_name)
        return {
            "type": "USERS",
            "count": len(users),
            "attributes": users
        }

        