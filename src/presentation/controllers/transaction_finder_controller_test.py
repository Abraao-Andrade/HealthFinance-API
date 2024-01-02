from src.presentation.controllers.transaction_finder_controller import TransactionFinderController
from src.data.tests.transaction_finder import TransactionFinderSpy
from src.presentation.http_types.http_response import HttpResponse


class HttpRequestMock():
    def __init__(self) -> None:
        self.query_params = {"uuid": "UUIDTRANSACTION"}


def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = TransactionFinderSpy()
    transaction_finder_controller = TransactionFinderController(use_case)

    response = transaction_finder_controller.handle(http_request_mock)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body['data'] is not None
