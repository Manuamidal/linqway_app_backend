from sqlalchemy.orm import Session
from app.models.prescription import Prescription
from app.schemas.prescription import PrescriptionCreate


def get_all_prescriptions(db: Session) -> list[Prescription]:
    return db.query(Prescription).order_by(Prescription.id.desc()).all()


def get_prescriptions_by_patient(db: Session, patient_id: int) -> list[Prescription]:
    return (
        db.query(Prescription)
        .filter(Prescription.patient_id == patient_id)
        .order_by(Prescription.id.desc())
        .all()
    )


def create_prescription(db: Session, data: PrescriptionCreate) -> Prescription:
    prescription = Prescription(**data.model_dump())
    db.add(prescription)
    db.commit()
    db.refresh(prescription)
    return prescription


def delete_prescription(db: Session, prescription_id: int) -> bool:
    prescription = db.query(Prescription).filter(Prescription.id == prescription_id).first()
    if not prescription:
        return False
    db.delete(prescription)
    db.commit()
    return True