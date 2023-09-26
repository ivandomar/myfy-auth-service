import hashlib

from constants.error_messages import DUPLICATED_ELEMENT, GENERAL_ERROR, NOT_FOUND
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
    
    try:
        session = Session()

        user = session.query(User).filter(
            User.id == id,
            User.deleted_at == None
        ).one_or_none()

        session.close()

        if user is None:
            raise ValueError(NOT_FOUND)

        return format_user_response(user), OK
        
    except ValueError as e:
        return {"mesage": str(e)}, SEMANTIC_ERROR
    except Exception as e:        
        return {"mesage": str(e)}, SYNTAX_ERROR

def update(path: UpdateUserIdRequestSchema, body: UpdateUserRequestSchema):
    id = path.id
        
    try:
        session = Session()

        user = session.query(User).filter(User.id == id).one_or_none()

        if user is None:
            raise ValueError(NOT_FOUND)

        new_name = body.name or user.name
        new_email = body.email or user.email
        new_login = body.login or user.login
        new_pasword = body.password or user.password

        if new_login != user.login:
            matching_element = session.query(User).filter(
                User.login == user.login,
                User.deleted_at == None,
                User.id != user.id
            ).one_or_none()

            if matching_element is not None:
                raise AttributeError(DUPLICATED_ELEMENT)
            
        if new_email != user.email:
            matching_element = session.query(User).filter(
                User.email == user.email,
                User.deleted_at == None,
                User.id != user.id
            ).one_or_none()

            if matching_element is not None:
                raise AttributeError(DUPLICATED_ELEMENT)
            
        hash = hashlib.md5()
        hashlib.update(bytes(new_pasword))

        hashed_new_password = hash.hexdigest()
        
        new_data = {
            'name': new_name,
            'email': new_email,
            'login': new_login,
            'password': hashed_new_password,
            'updated_at': datetime.now()
        }

        session.query(User).filter(User.id == id).update(new_data)

        new_element = session.query(User).filter(User.id == id).one_or_none()

        session.commit()
        session.close()
        
        return format_user_response(new_element), OK

    except(AttributeError, ValueError) as e:
        return {"mesage": str(e)}, SEMANTIC_ERROR
    except Exception as e:        
        return {"mesage": GENERAL_ERROR}, SYNTAX_ERROR
