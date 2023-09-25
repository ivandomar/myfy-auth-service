from datetime import datetime
from pydantic import BaseModel


class AuthResponseSchema(BaseModel):
    user_id: str
    user_name: str
    token: str|None
