from src.presentation.controllers.patient_finder_controller import PatientFinderController
from src.data.tests.patient_finder import PatientFinderSpy
from src.presentation.http_types.http_response import HttpResponse


class HttpRequestMock():
    def __init__(self) -> None:
        self.query_params = {"first_name": "teste"}


def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = PatientFinderSpy()
    patient_finder_controller = PatientFinderController(use_case)

    response = patient_finder_controller.handle(http_request_mock)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body['data'] is not None
