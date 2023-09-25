from flask_openapi3 import APIBlueprint, Tag

from constants.http_statuses import OK, SEMANTIC_ERROR, SYNTAX_ERROR
from controllers.auth import login, logout
from schemas.responses.auth import AuthResponseSchema
from schemas.responses.general import ErrorResponseSchema

auth_blueprint = APIBlueprint("auth", __name__, url_prefix="/auth")

auth_tag = Tag(name="Auth", description="Authentication edpoints")

auth_blueprint.post(
    '/login',
    tags=[auth_tag],
    summary='Authenticates user by login and password',
    responses={
        str(OK): AuthResponseSchema,
        str(SEMANTIC_ERROR): ErrorResponseSchema,
        str(SYNTAX_ERROR): ErrorResponseSchema
        }
)(login)

auth_blueprint.post(
    '/<user_id>/logout',
    tags=[auth_tag],
    summary='Invalidates specified user authentication token',
    responses={
        str(OK): AuthResponseSchema,
        str(SEMANTIC_ERROR): ErrorResponseSchema,
        str(SYNTAX_ERROR): ErrorResponseSchema
        }
)(logout)
