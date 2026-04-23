from pydantic import BaseModel


class DoctorBase(BaseModel):
    name: str
    specialization: str
    experience: int


class DoctorCreate(DoctorBase):
    pass


class DoctorUpdate(BaseModel):
    name: str | None = None
    specialization: str | None = None
    experience: int | None = None


class DoctorResponse(DoctorBase):
    id: int

    class Config:
        from_attributes = True