# pylint: disable=E0401:import-error

from sqlalchemy import Column, String, Float, DateTime
from src.infra.db.settings.base import Base


class Transactions(Base):
    __tablename__ = "TRANSACTIONS"

    uuid = Column(String, primary_key=True)
    patient_uuid = Column(String, nullable=False)
    pharmacy_uuid = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=False)

    def __repr__(self):
        return (
            f"Transactions [uuid={self.uuid}, patient_uuid={self.patient_uuid}, "
            f"pharmacy_uuid={self.pharmacy_uuid}, amount={self.amount},timestamp={self.timestamp}]"
        )
