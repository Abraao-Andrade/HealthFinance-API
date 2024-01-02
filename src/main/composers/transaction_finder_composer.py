from src.infra.db.repositories.transactions_repository import TransactionsRepository
from src.data.use_cases.transactions_finder import TransactionFinder
from src.presentation.controllers.transaction_finder_controller import TransactionFinderController


def transaction_finder_composer():
    repository = TransactionsRepository()
    use_case = TransactionFinder(repository)
    controller = TransactionFinderController(use_case)

    return controller.handle
