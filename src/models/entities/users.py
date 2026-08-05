from sqlalchemy import Table, Column, Integer, String
from src.models.settings.metadata import metadata

Users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_name", String, nullable=False),
    Column("age", Integer),
    Column("uf", String)
)
