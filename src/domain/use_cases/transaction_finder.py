from abc import ABC, abstractmethod
from typing import Dict


class TransactionFinder(ABC):

    @abstractmethod
    def find(self, uuid: str) -> Dict: pass

    @abstractmethod
    def find_by_pharmacy(self, pharmacy_uuid: str) -> Dict: pass

    @abstractmethod
    def find_by_patient(self, patient_uuid: str) -> Dict: pass

    @abstractmethod
    def list_all_transactions(self) -> Dict: pass
