from typing import Dict


class UserRegisterSpy:
    def __init__(self) -> None:
        self.register_attributes = {}

    def register(self, username: str, password: str) -> Dict:
        self.register_attributes["username"] = username
        self.register_attributes["password"] = password

        return {
            "type": "Users",
            "count": 1,
            "attributes": {
                'id': "UUID(abscld-dr12345-shfg)",
                'username': username
            }
        }
