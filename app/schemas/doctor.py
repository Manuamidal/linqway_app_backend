from datetime import time
from pydantic import BaseModel


class DoctorBase(BaseModel):
    name:             str
    specialization:   str
    experience_years: float
    rating:           float
    recommendation:   int
    clinic:           str
    initials:         str
    email:            str
    available_from:   time
    available_to:     time


class DoctorCreate(DoctorBase):
    id: str  # provided manually e.g. "doc-1"


class DoctorUpdate(BaseModel):
    name:             str   | None = None
    specialization:   str   | None = None
    experience_years: float | None = None
    rating:           float | None = None
    recommendation:   int   | None = None
    clinic:           str   | None = None
    initials:         str   | None = None
    email:            str   | None = None
    available_from:   time  | None = None
    available_to:     time  | None = None


class DoctorResponse(DoctorBase):
    id: str

    class Config:
        from_attributes = True