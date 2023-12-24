from uuid import UUID


class Users:
    def __init__(self, uuid: UUID, username: str, password: str) -> None:
        self.uuid = uuid
        self.username = username
        self.password = password
