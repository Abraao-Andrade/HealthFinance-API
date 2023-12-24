import uuid
from typing import List
from src.domain.models.users import Users


class UsersRepositorySpy:

    def __init__(self) -> None:
        self.insert_user_attributes = {}
        self.select_user_attributes = {}

    def insert_user(self, username: str, password: str) -> None:
        self.insert_user_attributes["username"] = username
        self.insert_user_attributes["password"] = password

    def select_user(self, username: str) -> List[Users]:
        self.select_user_attributes["username"] = username
        return [
            Users(uuid.uuid4, username, "admin@123"),
        ]
