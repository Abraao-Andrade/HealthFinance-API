from typing import Dict


class UserFinderSpy:
    def __init__(self) -> None:
        self.find_attributes = {}

    def find(self, username: str) -> Dict:
        self.find_attributes["username"] = username

        return {
            "type": "Users",
            "count": 1,
            "attributes": [
                {"username": username, 'id': "UUID(abscld-dr12345-shfg)"}
            ]
        }
