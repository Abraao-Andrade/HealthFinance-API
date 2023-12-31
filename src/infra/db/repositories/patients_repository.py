from typing import List
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.patients import Patients as PatiestsEntity
from src.data.interfaces.patients_repository import PatientsRepositoryInterface
from src.domain.models.patients import Patients


class PatientsRepository(PatientsRepositoryInterface):

    @classmethod
    def select_patient(cls, first_name: str) -> List[Patients]:
        with DBConnectionHandler() as database:
            try:
                patients = (
                    database.session.query(PatiestsEntity)
                    .filter(PatiestsEntity.first_name == first_name)
                    .all()
                )
                return patients
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def select_all_patients(cls) -> List[Patients]:
        with DBConnectionHandler() as database:
            try:
                patients = (
                    database.session.query(PatiestsEntity)
                    .all()
                )
                return patients
            except Exception as exception:
                database.session.rollback()
                raise exception
