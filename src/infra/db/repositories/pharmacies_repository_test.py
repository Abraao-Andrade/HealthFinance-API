import pytest
from src.infra.db.settings.connection import DBConnectionHandler
from .pharmacies_repository import PharmaciesRepository

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()


@pytest.mark.skip(reason="Sensitive test")
def test_select_pharmacie():
    mocked_name = 'DROGA MAIS'

    pharmacies_repository = PharmaciesRepository()

    response = pharmacies_repository.select_pharmacie(mocked_name)

    assert response[0].name == mocked_name
