from pydantic import BaseModel


class CreateUserRequestSchema(BaseModel):
    name: str
    email: str
    login: str
    password: str

class RemoveUserRequestSchema(BaseModel):
    id: str

class CheckUserRequestSchema(BaseModel):
    login: str
    token: str

class UpdateUserIdRequestSchema(BaseModel):
    id: str

class UpdateUserRequestSchema(BaseModel):
    name: str|None = None
    email: str|None = None
    login: str|None = None
    password: str|None = None
