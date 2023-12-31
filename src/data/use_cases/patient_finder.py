# pylint: disable=W0719:broad-exception-raised
from typing import Dict, List, Optional
from src.domain.use_cases.patient_finder import PatientFinder as PatientFinderInterface
from src.data.interfaces.patients_repository import PatientsRepositoryInterface
from src.domain.models.patients import Patients
from src.errors.types import HttpBadRequestError, HttpNotFoundError


class PatientFinder(PatientFinderInterface):
    def __init__(self, patient_repository: PatientsRepositoryInterface) -> None:
        self.__patients_repository = patient_repository

    def find(self, first_name: Optional[str] = None) -> Dict:

        if first_name:
            self.__validate_name(first_name)

        users = self.__search_patient(first_name)
        response = self.__format_response(users)

        return response

    @classmethod
    def __validate_name(cls, first_name: str) -> None:
        if not first_name.isalpha():
            raise HttpBadRequestError('Nome invalido para a busca')

        if len(first_name) > 18:
            raise HttpBadRequestError('Nome muito grande para busca')

    def __search_patient(self, first_name: Optional[str] = None) -> List[Patients]:
        patients = []

        if first_name:
            patients = self.__patients_repository.select_patient(first_name)
        else:
            patients = self.__patients_repository.select_all_patients()

        if patients == []:
            raise HttpNotFoundError('Paciente não encontrado.')
        return patients

    @classmethod
    def __format_response(cls, patients: List[Patients]) -> Dict:
        attributes = []

        for patient in patients:
            attributes.append(
                {'id': patient.uuid, 'first_name': patient.first_name,
                    'last_name': patient.last_name, 'date_of_birth': patient.date_of_birth}
            )

        response = {
            "type": "Patients",
            "count": len(patients),
            "attributes": attributes
        }

        return response
