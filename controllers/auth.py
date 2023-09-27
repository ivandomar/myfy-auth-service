import hashlib

from constants.error_messages import NOT_FOUND, GENERAL_ERROR, WRONG_CREDENTIALS
from constants.http_statuses import OK, CREATED, SEMANTIC_ERROR, SYNTAX_ERROR, AUTH_ERROR
from database import Session
from datetime import datetime
from formatters.auth import format_auth_response
from schemas.requests.auth import LoginRequestSchema, LogoutRequestSchema
from models import User, Token


def login(body: LoginRequestSchema):
    login = body.login
    password = body.password

    try:
        session = Session()

        matching_element = session.query(User).filter(
            User.login == login,
            User.deleted_at == None
        ).one_or_none()

        if matching_element is None:
            raise AttributeError(NOT_FOUND)
        
        hash = hashlib.md5()
        hash.update(bytes(password, encoding='utf-8'))
        hashedPassword = hash.hexdigest()

        if matching_element.password != hashedPassword:
            raise ChildProcessError(WRONG_CREDENTIALS)
        
        new_token = Token(matching_element.id)

        session.add(new_token)
        session.commit()
        session.close()
        
        return format_auth_response(matching_element, new_token), CREATED
    except AttributeError as e:
        return {"message": str(e)}, SEMANTIC_ERROR
    except ChildProcessError as e:
        return {"message": str(e)}, AUTH_ERROR
    except Exception as e:
        return {"message": str(e)}, SYNTAX_ERROR
    

def logout(path: LogoutRequestSchema):
    id = path.id

    try:
        session = Session()

        matching_element = session.query(User).filter(
            User.id == id,
            User.deleted_at == None
        ).one_or_none()

        if matching_element is None:
            raise AttributeError(NOT_FOUND)
        
        session.query(Token).filter(
            Token.user_id == matching_element.id,
            Token.deleted_at == None
        ).update({'deleted_at': datetime.now()})

        session.commit()
        session.close()
        
        return '', OK
    except AttributeError as e:
        return {"message": str(e)}, SEMANTIC_ERROR
    except Exception as e:
        return {"message": GENERAL_ERROR}, SYNTAX_ERROR
