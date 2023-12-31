from typing import Dict


class PatientFinderSpy:
    def __init__(self) -> None:
        self.find_attributes = {}

    def find(self, first_name: str) -> Dict:
        self.find_attributes["first_name"] = first_name

        return {
            "type": "Patients",
            "count": 1,
            "attributes": [
                {'id': "UUID(abscld-dr12345-shfg)", "first_name": first_name,
                 "last_name": "last_name_test", "date_of_birth": "1996-10-25 00:00:00.000000"}
            ]
        }
