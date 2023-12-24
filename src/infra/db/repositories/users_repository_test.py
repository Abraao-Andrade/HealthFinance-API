from .users_repository import UsersRepository


def test_insert_user():
    mocked_username = 'username@username.com'
    mocked_password = 'admin123'

    users_repository = UsersRepository()
    users_repository.insert_user(mocked_username, mocked_password)
