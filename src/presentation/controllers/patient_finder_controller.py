from src.presentation.interfaces.controller_interface import ControllerInterface
from src.data.use_cases.patient_finder import PatientFinder as PatientFinderInterface
from src.presentation.http_types.http_requests import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


# class PatientFinderController(ControllerInterface):
#    def __init__(self, use_case: PatientFinderInterface) -> None:
#        self.__use_case = use_case
#
#    def handle(self, http_request: HttpRequest) -> HttpResponse:
#        first_name = http_request.query_params["first_name"]
#        response = self.__use_case.find(first_name)
#
#        return HttpResponse(
#            status_code=200,
#            body={"data": response}
#        )

class PatientFinderController(ControllerInterface):
    def __init__(self, use_case: PatientFinderInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        # Usando get() para obter o valor opcionalmente
        first_name = http_request.query_params.get("first_name")

        # Verifica se o first_name existe e não é None
        if first_name is not None:
            response = self.__use_case.find(first_name)
        else:
            # Se first_name não foi fornecido, chama o use_case sem parâmetros
            response = self.__use_case.find()

        return HttpResponse(
            status_code=200,
            body={"data": response}
        )
