from cerberus import Validator
from src.errors.types import HttpUnprocessableEntityError


def user_finder_validator(requests: any):
    query_validator = Validator(
        {
            "username": {"type": "string", "required": True, "empty": False},
        }
    )

    response = query_validator.validate(requests.args)

    if response is False:
        raise HttpUnprocessableEntityError(query_validator.errors)
