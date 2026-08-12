from abc import ABC, abstractmethod

class UserFinderInterface(ABC):

    @abstractmethod
    async def find_user_by_name(self, user_name: str) -> dict: pass