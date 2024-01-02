from src.infra.db.repositories.users_repository import UsersRepository
from src.data.use_cases.user_authenticate import UserAuthenticate
from src.presentation.controllers.user_authenticate_controller import UserAuthenticateController
from src.main.services.auth_service import Authenticator


def user_authenticate_composer():
    repository = UsersRepository()
    authenticator = Authenticator(repository)
    use_case = UserAuthenticate(repository, authenticator)
    controller = UserAuthenticateController(use_case)

    return controller.handle
