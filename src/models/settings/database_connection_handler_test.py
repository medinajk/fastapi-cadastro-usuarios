import pytest
from .database_connection_handler import DBConnectionHandler

# Teste unitário
@pytest.mark.asyncio
@pytest.mark.asyncio(reason="Connecting to the database") # -> Pula o teste 
async def test_database_connection():
    async with DBConnectionHandler() as db_handler:
        print(db_handler.session)
        assert db_handler.session is not None

        