from typing import List
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.transactions import Transactions as TransactionsEntity
from src.data.interfaces.transactions_repository import TransactionsRepositoryInterface
from src.domain.models.transactions import Transactions


class TransactionsRepository(TransactionsRepositoryInterface):

    @classmethod
    def select_transaction(cls, uuid: str) -> List[Transactions]:
        with DBConnectionHandler() as database:
            try:
                transactions = (
                    database.session.query(TransactionsEntity)
                    .filter(TransactionsEntity.uuid == uuid)
                    .all()
                )
                return transactions
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def select_pharmacy_transactions(cls, pharmacy_uuid: str) -> List[Transactions]:
        with DBConnectionHandler() as database:
            try:
                transactions = (
                    database.session.query(TransactionsEntity)
                    .filter(TransactionsEntity.pharmacy_uuid == pharmacy_uuid)
                    .all()
                )
                return transactions
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def select_patient_transactions(cls, patient_uuid: str) -> List[Transactions]:
        with DBConnectionHandler() as database:
            try:
                transactions = (
                    database.session.query(TransactionsEntity)
                    .filter(TransactionsEntity.patient_uuid == patient_uuid)
                    .all()
                )
                return transactions
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def select_all_transactions(cls) -> List[Transactions]:
        with DBConnectionHandler() as database:
            try:
                transactions = (
                    database.session.query(TransactionsEntity)
                    .all()
                )
                return transactions
            except Exception as exception:
                database.session.rollback()
                raise exception
