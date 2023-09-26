from constants.http_statuses import OK, CREATED
from schemas.requests.auth import LoginRequestSchema, LogoutRequestSchema


def login(body: LoginRequestSchema):
    return None, CREATED
    

def logout(path: LogoutRequestSchema):
    id = path.id
        
    return None, OK
