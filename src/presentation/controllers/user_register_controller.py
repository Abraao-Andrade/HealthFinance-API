from src.presentation.interfaces.controller_interface import ControllerInterface
from src.data.use_cases.user_register import UserRegister as UserRegisterInterface
from src.presentation.http_types.http_requests import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


class UserRegisterController(ControllerInterface):
    def __init__(self, use_case: UserRegisterInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        username = http_request.body["username"]
        password = http_request.body["password"]

        response = self.__use_case.register(username, password)

        return HttpResponse(
            status_code=201,
            body={"data": response}
        )
