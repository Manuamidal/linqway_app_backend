from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.prescription import PrescriptionCreate, PrescriptionResponse
from app.services import prescription_service

router = APIRouter(prefix="/prescriptions", tags=["Prescriptions"])


@router.get("/", response_model=list[PrescriptionResponse])
def list_prescriptions(db: Session = Depends(get_db)):
    return prescription_service.get_all_prescriptions(db)


@router.get("/patient/{patient_id}", response_model=list[PrescriptionResponse])
def list_by_patient(patient_id: int, db: Session = Depends(get_db)):
    return prescription_service.get_prescriptions_by_patient(db, patient_id)


@router.post("/", response_model=PrescriptionResponse, status_code=status.HTTP_201_CREATED)
def create_prescription(data: PrescriptionCreate, db: Session = Depends(get_db)):
    return prescription_service.create_prescription(db, data)


@router.delete("/{prescription_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_prescription(prescription_id: int, db: Session = Depends(get_db)):
    deleted = prescription_service.delete_prescription(db, prescription_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prescription not found")