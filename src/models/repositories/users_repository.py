from sqlalchemy import insert
from src.models.settings.database_connection_handler import DBConnectionHandler
from src.models.entities.users import Users

class UsersRepository:
    async def insert_users(self, user_infos: dict ) -> None:
        query = insert(Users).values(user_infos)