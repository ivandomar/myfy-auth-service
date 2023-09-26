from constants.http_statuses import OK, CREATED
from flask import request


def create(body):
    return None, CREATED
    

def delete(path, body):
    id = path.id
        
    return None, OK

def get(path):
    id = path.id
        
    return None, OK

def update(path, body):
    id = path.id
        
    return None, OK
