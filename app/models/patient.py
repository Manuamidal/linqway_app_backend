from sqlalchemy import Column, Integer, String
from app.db.database import Base


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    phone_no = Column(String, nullable=False)
    symptoms = Column(String, nullable=True)
    address = Column(String, nullable=True)