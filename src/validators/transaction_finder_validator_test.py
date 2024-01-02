from .transaction_finder_validator import transaction_finder_validator


class MockRequest:
    def __init__(self) -> None:
        self.args = None


def test_pharmacie_finder_validator():
    request = MockRequest()
    request.args = {
        "uuid": "",
        "patient_uuid": "",
        "pharmacy_uuid": "",
    }

    transaction_finder_validator(request)
