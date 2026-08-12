from abc import ABC, abstractmethod

class UserRegisterInterface(ABC):

    @abstractmethod
    async def register_user(self, user_data: dict) -> dict: pass