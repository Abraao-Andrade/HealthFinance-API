# pylint: disable=E0401:import-error

from sqlalchemy import Column, String, DateTime
from src.infra.db.settings.base import Base


class Patients(Base):
    __tablename__ = "PATIENTS"

    uuid = Column(String, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    date_of_birth = Column(DateTime, nullable=False)

    def __repr__(self):
        return (
            f"Patients [uuid={self.uuid}, first_name={self.first_name}, "
            f"last_name={self.last_name}, date_of_birth={self.date_of_birth}]"
        )
