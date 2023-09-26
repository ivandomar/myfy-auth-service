from models.user import User

def format_user_response(user: User):
    return {
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'login': user.login,
        'created_at': user.created_at,
        'updated_at': user.updated_at,
    }