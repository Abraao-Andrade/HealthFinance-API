from datetime import datetime


class Patients:
    def __init__(self, uuid: str, first_name: str, last_name: str, date_of_birth: datetime) -> None:
        self.uuid = uuid
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
