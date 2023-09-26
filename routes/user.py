from flask_openapi3 import APIBlueprint, Tag

from constants.http_statuses import OK, SEMANTIC_ERROR, SYNTAX_ERROR
from controllers.user import create, delete, check, update
from schemas.responses.user import UserResponseSchema
from schemas.responses.general import ErrorResponseSchema

user_blueprint = APIBlueprint("user", __name__, url_prefix="/user")

user_tag = Tag(name="User", description="User management edpoints")

user_blueprint.post(
    '/',
    tags=[user_tag],
    summary='Creates new user',
    responses={
        str(OK): UserResponseSchema,
        str(SEMANTIC_ERROR): ErrorResponseSchema,
        str(SYNTAX_ERROR): ErrorResponseSchema
        }
)(create)

user_blueprint.delete(
    '/<user_id>',
    tags=[user_tag],
    summary='Removes specified user',
    responses={
        str(OK): UserResponseSchema,
        str(SEMANTIC_ERROR): ErrorResponseSchema,
        str(SYNTAX_ERROR): ErrorResponseSchema
        }
)(delete)

user_blueprint.get(
    '/<user_id>/<token>',
    tags=[user_tag],
    summary='Gets specified user',
    responses={
        str(OK): UserResponseSchema,
        str(SEMANTIC_ERROR): ErrorResponseSchema,
        str(SYNTAX_ERROR): ErrorResponseSchema
        }
)(check)

user_blueprint.put(
    '/<user_id>',
    tags=[user_tag],
    summary='Updates data of specified user',
    responses={
        str(OK): UserResponseSchema,
        str(SEMANTIC_ERROR): ErrorResponseSchema,
        str(SYNTAX_ERROR): ErrorResponseSchema
        }
)(update)
