import pytest
from src.infra.db.settings.connection import DBConnectionHandler
from .patients_repository import PatientsRepository

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()


@pytest.mark.skip(reason="Sensitive test")
def test_select_patient():
    mocked_first_name = 'JOANA'

    patients_repository = PatientsRepository()

    response = patients_repository.select_patient(mocked_first_name)

    assert response[0].first_name == mocked_first_name
