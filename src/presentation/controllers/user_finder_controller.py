from src.presentation.interfaces.controller_interface import ControllerInterface
from src.data.use_cases.user_finder import UserFinder as UserFinderInterface
from src.presentation.http_types.http_requests import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


class UserFinderController(ControllerInterface):
    def __init__(self, use_case: UserFinderInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        username = http_request.query_params["username"]
        response = self.__use_case.find(username)

        return HttpResponse(
            status_code=200,
            body={"data": response}
        )
