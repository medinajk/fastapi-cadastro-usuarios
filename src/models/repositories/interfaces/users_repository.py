from abc import ABC, abstractmethod

class UsersRepositoryInterface(ABC):
    @abstractmethod
    async def insert_users(self, user_infos: dict ) -> None: pass

    @abstractmethod
    async def get_users_by_name(self, name: str) -> list[dict]: pass