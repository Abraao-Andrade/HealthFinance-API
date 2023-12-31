from src.presentation.interfaces.controller_interface import ControllerInterface
from src.data.use_cases.pharmacies_finder import PharmacieFinder as PharmacieFinderInterface
from src.presentation.http_types.http_requests import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


class PharmacieFinderController(ControllerInterface):
    def __init__(self, use_case: PharmacieFinderInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        name = http_request.query_params.get("name")

        if name is not None:
            response = self.__use_case.find(name)
        else:
            response = self.__use_case.find()

        return HttpResponse(
            status_code=200,
            body={"data": response}
        )
