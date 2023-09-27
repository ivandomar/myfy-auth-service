from models import User, Token

def format_auth_response(user: User, token: Token):
    return {
        'user_id': user.id,
        'user_name': user.name,
        'token': token.content
    }