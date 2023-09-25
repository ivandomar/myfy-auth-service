from pydantic import BaseModel


class CreateUserRequestSchema(BaseModel):
    name: str
    email: str
    login: str
    password: str

class RemoveUserRequestSchema(BaseModel):
    id: int

class GetUserRequestSchema(BaseModel):
    id: int

class UpdateUserIdRequestSchema(BaseModel):
    id: int

class UpdateUserRequestSchema(BaseModel):
    name: str = None
    email: str = None
    login: str = None
    password: str = None
