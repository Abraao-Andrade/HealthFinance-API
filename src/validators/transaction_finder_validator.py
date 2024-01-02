from cerberus import Validator
from src.errors.types import HttpUnprocessableEntityError


def transaction_finder_validator(requests: any):
    query_validator = Validator(
        {
            "uuid": {"type": "string", "required": True, "empty": True},
            "patient_uuid": {"type": "string", "required": True, "empty": True},
            "pharmacy_uuid": {"type": "string", "required": True, "empty": True},

        }
    )

    response = query_validator.validate(requests.args)

    if response is False:
        raise HttpUnprocessableEntityError(query_validator.errors)
