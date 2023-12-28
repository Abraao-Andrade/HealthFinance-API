from .user_finder_validator import user_finder_validator


class MockRequest:
    def __init__(self) -> None:
        self.args = None


def test_user_finder_validator():
    request = MockRequest()
    request.args = {
        "username": "test@test.com",
    }

    user_finder_validator(request)
