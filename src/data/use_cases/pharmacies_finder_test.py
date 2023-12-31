from src.infra.db.tests.pharmacies_repository import PharmaciesRepositorySpy
from .pharmacies_finder import PharmacieFinder


def test_list_all_pharmacies():
    repo = PharmaciesRepositorySpy()
    pharmacie_finder = PharmacieFinder(repo)

    response = pharmacie_finder.find()

    assert response["type"] == "Pharmacies"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"]


def test_find():
    name = 'teste'

    repo = PharmaciesRepositorySpy()
    pharmacie_finder = PharmacieFinder(repo)

    response = pharmacie_finder.find(name)

    assert repo.select_pharmacie_attributes["name"] == name

    assert response["type"] == "Pharmacies"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"]


def test_find_error_in_valid_name():
    name = 'meuNome123'

    repo = PharmaciesRepositorySpy()
    pharmacie_finder = PharmacieFinder(repo)

    try:
        pharmacie_finder.find(name)
        assert False
    except Exception as expection:
        assert str(expection) == "Nome invalido para a busca"


def test_find_error_in_long_name():
    name = 'meuNomeahlfksjhfsjkalhkfjhsalfkshfkljshalkjsh'

    repo = PharmaciesRepositorySpy()
    pharmacie_finder = PharmacieFinder(repo)

    try:
        pharmacie_finder.find(name)
        assert False
    except Exception as expection:
        assert str(expection) == "Nome muito grande para busca"


def test_find_error_user_not_found():
    class PharmaciesRepositoryError(PharmaciesRepositorySpy):
        def select_pharmacie(self, name: str):
            return []

    name = 'Jaco'

    repo = PharmaciesRepositoryError()
    pharmacie_finder = PharmacieFinder(repo)

    try:
        pharmacie_finder.find(name)
        assert False
    except Exception as expection:
        assert str(expection) == "Farmacia não encontrada."
