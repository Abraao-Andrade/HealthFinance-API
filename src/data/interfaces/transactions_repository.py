from typing import List
from abc import ABC, abstractmethod
from src.domain.models.transactions import Transactions


class TransactionsRepositoryInterface(ABC):

    @abstractmethod
    def select_transaction(self, uuid: str) -> List[Transactions]: pass

    @abstractmethod
    def select_pharmacy_transactions(
        self, pharmacy_uuid: str) -> List[Transactions]: pass

    @abstractmethod
    def select_patient_transactions(
        self, patient_uuid: str) -> List[Transactions]: pass

    @abstractmethod
    def select_all_transactions(self) -> List[Transactions]: pass
