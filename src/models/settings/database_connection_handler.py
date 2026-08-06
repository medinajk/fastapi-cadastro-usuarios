from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

CONNECTION_STRING = "sqlite+aiosqlite:///schema.db" # onde está o banco de dados

# mecanismo de comunicação com o banco de dados
engine = create_async_engine(
    CONNECTION_STRING,
    echo=False,
    pool_size=2, # não criar mais do que 2 conexões simultâneas com o banco de dados
    max_overflow=0,
    pool_timeout=30
    )

# cria uma sessão para interagir com o banco de dados
async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

class DBConnectionHandler:
    def __init__(self) -> None: # construtor que inicializa a sessão com o banco de dados
        self.session: Optional[AsyncSession] = None

    # cria uma nova sessão    
    async def __aenter__(self):
        self.session = async_session()
        return self
    
    # fecha a sessão com o banco de dados
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()