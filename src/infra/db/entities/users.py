import uuid
import bcrypt
from sqlalchemy import Column, String, UUID
from src.infra.db.settings.base import Base


class Users(Base):
    __tablename__ = "USERS"

    uuid = Column(UUID, primary_key=True, default=uuid.uuid4)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

    def set_password(self, password):
        self.password = bcrypt.hashpw(
            password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    def __repr__(self):
        return f"Users [id={self.uuid}, username={self.username}]"
