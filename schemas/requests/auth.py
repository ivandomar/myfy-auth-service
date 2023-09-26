from pydantic import BaseModel

class LoginRequestSchema(BaseModel):
    login: str
    password: str

class LogoutRequestSchema(BaseModel):
    id: str
