from src.presentation.interfaces.controller_interface import ControllerInterface
from src.data.use_cases.transactions_finder import TransactionFinder as TransactionFinderInterface
from src.presentation.http_types.http_requests import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


class TransactionFinderController(ControllerInterface):
    def __init__(self, use_case: TransactionFinderInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        uuid = http_request.query_params.get("uuid")
        patient_uuid = http_request.query_params.get("patient_uuid")
        pharmacy_uuid = http_request.query_params.get("pharmacy_uuid")

        if uuid is not None:
            response = self.__use_case.find(uuid)
        elif patient_uuid is not None:
            response = self.__use_case.find_by_patient(patient_uuid)
        elif pharmacy_uuid is not None:
            response = self.__use_case.find_by_pharmacy(pharmacy_uuid)
        else:
            response = self.__use_case.list_all_transactions()

        return HttpResponse(
            status_code=200,
            body={"data": response}
        )
