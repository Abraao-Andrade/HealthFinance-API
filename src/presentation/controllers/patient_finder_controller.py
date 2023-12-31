from src.presentation.interfaces.controller_interface import ControllerInterface
from src.data.use_cases.patient_finder import PatientFinder as PatientFinderInterface
from src.presentation.http_types.http_requests import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


class PatientFinderController(ControllerInterface):
    def __init__(self, use_case: PatientFinderInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        first_name = http_request.query_params.get("first_name")

        if first_name is not None:
            response = self.__use_case.find(first_name)
        else:
            response = self.__use_case.find()

        return HttpResponse(
            status_code=200,
            body={"data": response}
        )
