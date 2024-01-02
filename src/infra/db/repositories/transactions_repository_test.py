import pytest
from src.infra.db.settings.connection import DBConnectionHandler
from .transactions_repository import TransactionsRepository

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()


@pytest.mark.skip(reason="Sensitive test")
def test_select_transaction():
    mocked_uuid = 'TRAN0001'

    transaction_repository = TransactionsRepository()

    response = transaction_repository.select_transaction(mocked_uuid)

    assert response[0].uuid == mocked_uuid


@pytest.mark.skip(reason="Sensitive test")
def test_select_pharmacy_transactions():
    mocked_pharmacy_uuid = 'PHARM0008'

    transaction_repository = TransactionsRepository()

    response = transaction_repository.select_pharmacy_transactions(
        mocked_pharmacy_uuid)

    assert response[0].pharmacy_uuid == mocked_pharmacy_uuid


@pytest.mark.skip(reason="Sensitive test")
def test_select_patient_transactions():
    mocked_patient_uuid = 'PATIENT0045'

    transaction_repository = TransactionsRepository()

    response = transaction_repository.select_patient_transactions(
        mocked_patient_uuid)

    assert response[0].patient_uuid == mocked_patient_uuid
