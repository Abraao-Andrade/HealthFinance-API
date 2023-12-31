from typing import List
from abc import ABC, abstractmethod
from src.domain.models.patients import Patients


class PatientsRepositoryInterface(ABC):

    @abstractmethod
    def select_patient(self, first_name: str) -> List[Patients]: pass

    @abstractmethod
    def select_all_patients(self) -> List[Patients]: pass
