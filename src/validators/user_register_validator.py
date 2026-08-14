from pydantic import BaseModel, Field

class UserInput(BaseModel):
    user_name: str = Field(..., min_length=1)
    age: int = Field(..., gt=0)
    uf: str

