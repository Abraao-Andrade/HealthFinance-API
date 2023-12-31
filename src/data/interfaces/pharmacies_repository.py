from typing import List
from abc import ABC, abstractmethod
from src.domain.models.pharmacies import Pharmacies


class PharmaciesRepositoryInterface(ABC):

    @abstractmethod
    def select_pharmacie(self, name: str) -> List[Pharmacies]: pass

    @abstractmethod
    def select_all_pharmacies(self) -> List[Pharmacies]: pass
