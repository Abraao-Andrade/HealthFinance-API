from cerberus import Validator
from src.errors.types import HttpUnprocessableEntityError


def user_register_validator(requests: any):
    body_validator = Validator(
        {
            "username": {"type": "string", "required": True, "empty": False},
            "password": {"type": "string", "required": True, "empty": False},
        }
    )

    response = body_validator.validate(requests.json)

    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
