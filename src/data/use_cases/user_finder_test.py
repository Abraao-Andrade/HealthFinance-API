from src.infra.db.tests.users_repository import UsersRepositorySpy
from .user_finder import UserFinder


def test_find():
    username = 'teste@teste.com'

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    response = user_finder.find(username)

    assert repo.select_user_attributes["username"] == username

    assert response["type"] == "Users"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"]


def test_find_error_in_valid_username():
    username = 'meuNome123'

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(username)
        assert False
    except Exception as expection:
        assert str(expection) == "Email invalido para busca."


def test_find_error_user_not_found():
    class UsersRepositoryError(UsersRepositorySpy):
        def select_user(self, username: str):
            return []

    username = 'teste1@teste.com'

    repo = UsersRepositoryError()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(username)
        assert False
    except Exception as expection:
        assert str(expection) == "Usuario nao encontrado."
