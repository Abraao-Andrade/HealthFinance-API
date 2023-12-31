from .pharmacie_finder_validator import pharmacie_finder_validator


class MockRequest:
    def __init__(self) -> None:
        self.args = None


def test_pharmacie_finder_validator():
    request = MockRequest()
    request.args = {
        "name": "test",
    }

    pharmacie_finder_validator(request)
