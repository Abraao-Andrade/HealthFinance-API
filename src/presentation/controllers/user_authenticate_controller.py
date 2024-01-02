from src.presentation.interfaces.controller_interface import ControllerInterface
from src.data.use_cases.user_authenticate import UserAuthenticate as UserAuthenticateInterface
from src.presentation.http_types.http_requests import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


class UserAuthenticateController(ControllerInterface):
    def __init__(self, use_case: UserAuthenticateInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        username = http_request.body["username"]
        password = http_request.body["password"]

        response = self.__use_case.authenticate(username, password)

        return HttpResponse(
            status_code=200,
            body={"data": response}
        )
