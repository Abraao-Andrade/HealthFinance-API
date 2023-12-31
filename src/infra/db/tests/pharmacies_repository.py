import uuid
from typing import List
from src.domain.models.pharmacies import Pharmacies


class PharmaciesRepositorySpy:

    def __init__(self) -> None:
        self.select_pharmacie_attributes = {}

    def select_pharmacie(self, name: str) -> List[Pharmacies]:
        self.select_pharmacie_attributes["name"] = name
        return [
            Pharmacies(
                uuid.uuid4,
                "name",
                "city test"
            ),
        ]

    def select_all_pharmacies(self) -> List[Pharmacies]:
        return [
            Pharmacies(
                uuid.uuid4,
                "name",
                "city test",
            ),
        ]
