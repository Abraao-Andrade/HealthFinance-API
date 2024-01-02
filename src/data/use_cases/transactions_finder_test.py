from src.infra.db.tests.transactions_repository import TransactionsRepositorySpy
from .transactions_finder import TransactionFinder


def test_list_all_transactions():
    repo = TransactionsRepositorySpy()
    transaction_finder = TransactionFinder(repo)

    response = transaction_finder.list_all_transactions()

    assert response["type"] == "Transactions"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"]


def test_find():
    uuid = 'UUIDTRANSACTION'

    repo = TransactionsRepositorySpy()
    transaction_finder = TransactionFinder(repo)

    response = transaction_finder.find(uuid)

    assert repo.select_transaction_attributes["uuid"] == uuid

    assert response["type"] == "Transactions"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"]


def test_find_by_patient():
    patient_uuid = 'UUIDPATIENT'

    repo = TransactionsRepositorySpy()
    transaction_finder = TransactionFinder(repo)

    response = transaction_finder.find_by_patient(patient_uuid)

    assert repo.select_transaction_attributes["patient_uuid"] == patient_uuid

    assert response["type"] == "Transactions"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"]


def test_find_by_pharmacy():
    pharmacy_uuid = 'UUIDPHARMACY'

    repo = TransactionsRepositorySpy()
    transaction_finder = TransactionFinder(repo)

    response = transaction_finder.find_by_pharmacy(pharmacy_uuid)

    assert repo.select_transaction_attributes["pharmacy_uuid"] == pharmacy_uuid

    assert response["type"] == "Transactions"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"]


def test_find_error_transaction_not_found():
    class TransactionsRepositoryError(TransactionsRepositorySpy):
        def select_transaction(self, uuid: str):
            return []

    uuid = 'UUIDTRANSACTION'

    repo = TransactionsRepositoryError()
    transaction_finder = TransactionFinder(repo)

    try:
        transaction_finder.find(uuid)
        assert False
    except Exception as expection:
        assert str(expection) == "Transação não encontrada."
