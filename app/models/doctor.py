from sqlalchemy import Column, String, Float, Integer, Time
from app.db.database import Base


class Doctor(Base):
    __tablename__ = "doctors"

    id             = Column(String,  primary_key=True, index=True)
    name           = Column(String,  nullable=False)
    specialization = Column(String,  nullable=False)
    experience_years = Column(Float, nullable=False, default=0)
    rating         = Column(Float,   nullable=False, default=0)
    recommendation = Column(Integer, nullable=False, default=0)  # 0-100 (%)
    clinic         = Column(String,  nullable=False, default="")
    initials       = Column(String,  nullable=False, default="")
    email          = Column(String,  nullable=False, default="")
    available_from = Column(Time,    nullable=False)
    available_to   = Column(Time,    nullable=False)