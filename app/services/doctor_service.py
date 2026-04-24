from sqlalchemy.orm import Session
from app.models.doctor import Doctor
from app.schemas.doctor import DoctorCreate, DoctorUpdate


def get_all_doctors(db: Session) -> list[Doctor]:
    return db.query(Doctor).order_by(Doctor.name.asc()).all()


def get_doctor_by_id(db: Session, doctor_id: str) -> Doctor | None:
    return db.query(Doctor).filter(Doctor.id == doctor_id).first()


def create_doctor(db: Session, data: DoctorCreate) -> Doctor:
    doctor = Doctor(**data.model_dump())
    db.add(doctor)
    db.commit()
    db.refresh(doctor)
    return doctor


def update_doctor(db: Session, doctor_id: str, data: DoctorUpdate) -> Doctor | None:
    doctor = get_doctor_by_id(db, doctor_id)
    if not doctor:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(doctor, field, value)
    db.commit()
    db.refresh(doctor)
    return doctor


def delete_doctor(db: Session, doctor_id: str) -> bool:
    doctor = get_doctor_by_id(db, doctor_id)
    if not doctor:
        return False
    db.delete(doctor)
    db.commit()
    return True