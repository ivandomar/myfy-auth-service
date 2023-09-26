from constants.http_statuses import OK, CREATED
from flask import request
from schemas.requests.user import CreateUserRequestSchema, RemoveUserRequestSchema, UpdateUserIdRequestSchema, UpdateUserRequestSchema, GetUserRequestSchema


def create(body: CreateUserRequestSchema):
    return None, CREATED
    

def delete(path: RemoveUserRequestSchema):
    id = path.id
        
    return None, OK

def get(path: GetUserRequestSchema):
    id = path.id
        
    return None, OK

def update(path: UpdateUserIdRequestSchema, body: UpdateUserRequestSchema):
    id = path.id
        
    return None, OK
