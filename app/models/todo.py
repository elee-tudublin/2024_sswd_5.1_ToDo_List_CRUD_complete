# A model class for ToDo items
# See https://docs.pydantic.dev/latest/concepts/models/
from pydantic import BaseModel

class ToDo(BaseModel):
    id: int
    details: str
    completed: bool = False
    userId: int = 0