from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    prescription_id = Column(Integer, ForeignKey("prescriptions.id", ondelete="CASCADE"), nullable=False)
    file_name = Column(String, nullable=False)   # e.g. "CBC_report.pdf"
    file_url = Column(String, nullable=False)    # URL to the stored PDF

    prescription = relationship("Prescription", backref="documents")