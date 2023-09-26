from datetime import datetime
from pydantic import BaseModel


class UserResponseSchema(BaseModel):
    id: str
    name: str
    login: str
    email: str
    created_at: datetime
    updated_at: datetime
