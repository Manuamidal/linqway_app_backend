from pydantic import BaseModel


class PatientBase(BaseModel):
    name: str
    age: int
    phone_no: str
    symptoms: str | None = None
    address: str | None = None


class PatientCreate(PatientBase):
    pass


class PatientUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    phone_no: str | None = None
    symptoms: str | None = None
    address: str | None = None


class PatientResponse(PatientBase):
    id: int

    class Config:
        from_attributes = True