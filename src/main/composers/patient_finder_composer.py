from src.infra.db.repositories.patients_repository import PatientsRepository
from src.data.use_cases.patient_finder import PatientFinder
from src.presentation.controllers.patient_finder_controller import PatientFinderController


def patient_finder_composer():
    repository = PatientsRepository()
    use_case = PatientFinder(repository)
    controller = PatientFinderController(use_case)

    return controller.handle
