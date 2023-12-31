import uuid
from typing import List
from src.domain.models.patients import Patients


class PatientsRepositorySpy:

    def __init__(self) -> None:
        self.select_patient_attributes = {}

    def select_patient(self, first_name: str) -> List[Patients]:
        self.select_patient_attributes["first_name"] = first_name
        return [
            Patients(
                uuid.uuid4,
                first_name,
                "last_name",
                "1996-10-25 00:00:00.000000"
            ),
        ]

    def select_all_patients(self) -> List[Patients]:
        return [
            Patients(
                uuid.uuid4,
                "first_name",
                "last_name",
                "1996-10-25 00:00:00.000000"
            ),
        ]
