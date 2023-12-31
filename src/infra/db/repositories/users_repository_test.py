import pytest
from sqlalchemy import text
from src.infra.db.settings.connection import DBConnectionHandler
from .users_repository import UsersRepository

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()


@pytest.mark.skip(reason="Sensitive test")
def test_insert_user():
    mocked_username = 'username@username.com'
    mocked_password = 'admin123'

    users_repository = UsersRepository()
    users_repository.insert_user(mocked_username, mocked_password)

    sql = '''
        SELECT * FROM USERS
        WHERE USERNAME = '{}'
    '''.format(mocked_username)
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.USERNAME == mocked_username

    sql = '''
        DELETE FROM USERS
        WHERE UUID = '{}'
    '''.format(registry.UUID)
    response = connection.execute(text(sql))

    connection.commit()


@pytest.mark.skip(reason="Sensitive test")
def test_select_user():
    mocked_username = 'username@username.com'
    mocked_password = 'admin123'

    users_repository = UsersRepository()
    users_repository.insert_user(mocked_username, mocked_password)

    response = users_repository.select_user(mocked_username)

    assert response[0].username == mocked_username

    sql = '''
        DELETE FROM USERS
        WHERE UUID = '{}'
    '''.format(str(response[0].uuid).replace("-", ""))
    response = connection.execute(text(sql))

    connection.commit()
