from cerberus import Validator
from src.errors.types import HttpUnprocessableEntityError


def patient_finder_validator(requests: any):
    query_validator = Validator(
        {
            "first_name": {"type": "string", "required": True, "empty": False},
        }
    )

    response = query_validator.validate(requests.args)

    if response is False:
        raise HttpUnprocessableEntityError(query_validator.errors)
