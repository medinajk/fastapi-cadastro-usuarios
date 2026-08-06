import pytest 
from ..users_repository import UsersRepository

@pytest.mark.asyncio
@pytest.mark.skip(reason="Inserting a user into the database") # -> Pula o teste
async def test_insert_users():
    new_user = {
        "user_name": "test_user",
        "age": 25,
        "uf": "SP"
    }

    repo = UsersRepository()
    await repo.insert_users(new_user)

@pytest.mark.asyncio
@pytest.mark.skip(reason="Getting users by name from the database") # -> Pula o teste
async def test_get_users_by_name():
    repo = UsersRepository()
    response = await repo.get_users_by_name("test_user")
    print(response)