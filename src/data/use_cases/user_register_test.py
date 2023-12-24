from src.infra.db.tests.users_repository import UsersRepositorySpy
from .user_register import UserRegister


def test_register_user():
    username = 'teste@teste.com'
    password = 'admin@123'

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    response = user_register.register(username, password)

    assert repo.insert_user_attributes['username'] == username
    assert repo.insert_user_attributes['password'] == password

    assert response["type"] == "Users"
    assert response["count"] == 1
    assert response["attributes"]


def test_register_username_error():
    username = 'teste.teste.com'
    password = 'admin@123'

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    try:
        user_register.register(username, password)
        assert False
    except Exception as exception:
        assert str(exception) == 'Email invalido para cadastro.'
