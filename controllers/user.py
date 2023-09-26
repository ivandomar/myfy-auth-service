from constants.error_messages import DUPLICATED_ELEMENT, GENERAL_ERROR
from constants.http_statuses import OK, CREATED, SEMANTIC_ERROR, SYNTAX_ERROR
from database import Session
from datetime import datetime
from flask import request
from formatters.user import format_user_response
from models.user import User
from schemas.requests.user import CreateUserRequestSchema, RemoveUserRequestSchema, UpdateUserIdRequestSchema, UpdateUserRequestSchema, GetUserRequestSchema
from sqlalchemy import or_


def create(body: CreateUserRequestSchema):
    new_user = User(body.name, body.email, body.login, body.password)

    try:
        session = Session()

        matching_element = session.query(User).filter(
            or_(User.login == new_user.login, User.email == new_user.email),
            User.deleted_at == None
        ).one_or_none()

        if matching_element is not None:
            raise AttributeError(DUPLICATED_ELEMENT)

        session.add(new_user)
        session.commit()
        session.close()
        
        return format_user_response(new_user), CREATED
    except AttributeError as e:
        return {"message": str(e)}, SEMANTIC_ERROR
    except Exception as e:
        return {"message": GENERAL_ERROR}, SYNTAX_ERROR
    

def delete(path: RemoveUserRequestSchema):
    id = path.id

    try:
        session = Session()
        session.query(User).filter(User.id == id).update({'deleted_at': datetime.now()})
        session.commit()
        session.close()
        
        return '', OK

    except Exception as e:        
        return {"mesage": GENERAL_ERROR}, SYNTAX_ERROR


def get(path: GetUserRequestSchema):
    id = path.id
        
    return None, OK

def update(path: UpdateUserIdRequestSchema, body: UpdateUserRequestSchema):
    id = path.id
        
    return None, OK
