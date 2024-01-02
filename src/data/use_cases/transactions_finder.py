# pylint: disable=W0719:broad-exception-raised

from typing import Dict, List
from src.domain.use_cases.transaction_finder import TransactionFinder as TransactionFinderInterface
from src.data.interfaces.transactions_repository import TransactionsRepositoryInterface
from src.domain.models.transactions import Transactions
from src.errors.types import HttpNotFoundError


class TransactionFinder(TransactionFinderInterface):
    def __init__(self, transactions_repository: TransactionsRepositoryInterface) -> None:
        self.__transactions_repository = transactions_repository

    def find(self, uuid: str) -> Dict:

        transactions = self.__search_transaction(uuid)
        response = self.__format_response(transactions)

        return response

    def find_by_patient(self, patient_uuid: str) -> Dict:
        transactions = self.__search_patient_transaction(patient_uuid)
        response = self.__format_response(transactions)

        return response

    def find_by_pharmacy(self, pharmacy_uuid: str) -> Dict:
        transactions = self.__search_pharmacy_transaction(pharmacy_uuid)
        response = self.__format_response(transactions)

        return response

    def list_all_transactions(self) -> Dict:
        transactions = self.__list_transactions()
        response = self.__format_response(transactions)

        return response

    def __search_transaction(self, uuid: str) -> List[Transactions]:
        transactions = self.__transactions_repository.select_transaction(uuid)
        if transactions == []:
            raise HttpNotFoundError('Transação não encontrada.')
        return transactions

    def __search_patient_transaction(self, patient_uuid: str) -> List[Transactions]:
        transactions = self.__transactions_repository.select_patient_transactions(
            patient_uuid)
        if transactions == []:
            raise HttpNotFoundError(
                'Nenhuma transação encontrada para o paciente.')
        return transactions

    def __search_pharmacy_transaction(self, pharmacy_uuid: str) -> List[Transactions]:
        transactions = self.__transactions_repository.select_pharmacy_transactions(
            pharmacy_uuid)
        if transactions == []:
            raise HttpNotFoundError(
                'Nenhuma transação encontrada para a farmacia.')
        return transactions

    def __list_transactions(self) -> List[Transactions]:
        transactions = self.__transactions_repository.select_all_transactions()
        if transactions == []:
            raise HttpNotFoundError('Nenhuma transação encontrada.')
        return transactions

    @classmethod
    def __format_response(cls, transactions: List[Transactions]) -> Dict:
        attributes = []

        for transaction in transactions:
            attributes.append(
                {
                    'id': transaction.uuid,
                    'patient_uuid': transaction.patient_uuid,
                    'pharmacy_uuid': transaction.pharmacy_uuid,
                    'amount': transaction.amount,
                    'timestamp': transaction.timestamp,
                }
            )

        response = {
            "type": "Transactions",
            "count": len(transactions),
            "attributes": attributes
        }

        return response
