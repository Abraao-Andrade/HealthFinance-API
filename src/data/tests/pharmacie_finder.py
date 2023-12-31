from typing import Dict


class PharmacieFinderSpy:
    def __init__(self) -> None:
        self.find_attributes = {}

    def find(self, name: str) -> Dict:
        self.find_attributes["name"] = name

        return {
            "type": "Pharmacies",
            "count": 1,
            "attributes": [
                {'id': "UUID(abscld-dr12345-shfg)",
                 "name": name, "city": "city test"}
            ]
        }
