from pydantic import BaseModel
from typing import Literal
from app.schemas.document import DocumentResponse


class PrescriptionBase(BaseModel):
    patient_id: int
    doctor_id: int
    date: str
    title: Literal["Prescription", "Report"]
    detail: str
    doctor_name: str


class PrescriptionCreate(PrescriptionBase):
    pass


class PrescriptionResponse(PrescriptionBase):
    id: int
    documents: list[DocumentResponse] = []

    class Config:
        from_attributes = True