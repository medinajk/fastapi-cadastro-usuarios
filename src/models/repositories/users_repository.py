from sqlalchemy import insert, select, delete, update
from src.models.settings.database_connection_handler import DBConnectionHandler
from src.models.entities.users import Users
from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface

# Conversa diretamente com o banco de dados, cada método faz uma operação SQL.

class UsersRepository(UsersRepositoryInterface):
    async def insert_users(self, user_infos: dict ) -> None:
        async with DBConnectionHandler() as db_connection:
            query = insert(Users).values(user_infos)
            await db_connection.session.execute(query)
            await db_connection.session.commit() # confirma as alterações feitas no banco

    async def get_users_by_name(self, name: str) -> list[dict]:
                async with DBConnectionHandler() as db:
                    query = (
                        select(Users)
                        .where(Users.c.user_name == name)
                    )
                    result = await db.session.execute(query)
                    rows = result.fetchall() # busca todas as linhas

                    # pega cada linha e transforma em um dicionário (rows = linhas)
                    users_list = [dict(row._mapping) for row in rows]
                    return users_list

    async def delete_users_by_name(self, name: str) -> None:
          async with DBConnectionHandler() as db_connection:
                query = delete(Users).where(Users.c.user_name == name)

                await db_connection.session.execute(query)
                await db_connection.session.commit()

    async def update_users_by_name(self, name: str) -> None:
          async with DBConnectionHandler() as db_connection:
                query = (
                    update(Users)
                    .where(Users.c.user_name == name)
                    .values(user_name="Mark")
                )

                await db_connection.session.execute(query)
                await db_connection.session.commit()