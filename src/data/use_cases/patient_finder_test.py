from src.infra.db.tests.patients_repository import PatientsRepositorySpy
from .patient_finder import PatientFinder


def test_list_all_patients():
    repo = PatientsRepositorySpy()
    patient_finder = PatientFinder(repo)

    response = patient_finder.find()

    assert response["type"] == "Patients"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"]


def test_find():
    first_name = 'teste'

    repo = PatientsRepositorySpy()
    patient_finder = PatientFinder(repo)

    response = patient_finder.find(first_name)

    assert repo.select_patient_attributes["first_name"] == first_name

    assert response["type"] == "Patients"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"]


def test_find_error_in_valid_name():
    first_name = 'meuNome123'

    repo = PatientsRepositorySpy()
    patient_finder = PatientFinder(repo)

    try:
        patient_finder.find(first_name)
        assert False
    except Exception as expection:
        assert str(expection) == "Nome invalido para a busca"


def test_find_error_in_long_name():
    first_name = 'meuNomeahlfksjhfsjkalhkfjhsalfkshfkljshalkjsh'

    repo = PatientsRepositorySpy()
    patient_finder = PatientFinder(repo)

    try:
        patient_finder.find(first_name)
        assert False
    except Exception as expection:
        assert str(expection) == "Nome muito grande para busca"


def test_find_error_user_not_found():
    class PatientsRepositoryError(PatientsRepositorySpy):
        def select_patient(self, first_name: str):
            return []

    first_name = 'Jaco'

    repo = PatientsRepositoryError()
    patient_finder = PatientFinder(repo)

    try:
        patient_finder.find(first_name)
        assert False
    except Exception as expection:
        assert str(expection) == "Paciente não encontrado."
