from .patient_finder_validator import patient_finder_validator


class MockRequest:
    def __init__(self) -> None:
        self.args = None


def test_patient_finder_validator():
    request = MockRequest()
    request.args = {
        "first_name": "test",
    }

    patient_finder_validator(request)
