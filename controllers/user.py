from constants.error_messages import DUPLICATED_ELEMENT, ELEMENT_NOT_FOUND, FOLDER_NOT_FOUND, GENERAL_ERROR, REQUIRED_CONTENT
from constants.http_statuses import OK, CREATED, SEMANTIC_ERROR, SYNTAX_ERROR
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
