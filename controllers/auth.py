from constants.http_statuses import OK, CREATED
from flask import request


def login(body):
    return None, CREATED
    

def logout(path, body):
    id = path.id
        
    return None, OK
