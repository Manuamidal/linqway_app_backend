from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.document import DocumentCreate, DocumentResponse, DocumentBulkCreate
from app.services import document_service

router = APIRouter(prefix="/documents", tags=["Documents"])


@router.get("/prescription/{prescription_id}", response_model=list[DocumentResponse])
def list_by_prescription(prescription_id: int, db: Session = Depends(get_db)):
    return document_service.get_documents_by_prescription(db, prescription_id)


@router.post("/", response_model=DocumentResponse, status_code=status.HTTP_201_CREATED)
def create_document(data: DocumentCreate, db: Session = Depends(get_db)):
    return document_service.create_document(db, data)


@router.post("/bulk", response_model=list[DocumentResponse], status_code=status.HTTP_201_CREATED)
def create_documents_bulk(data: DocumentBulkCreate, db: Session = Depends(get_db)):
    """Attach multiple documents to a prescription in one request."""
    return document_service.create_documents_bulk(db, data)


@router.delete("/{document_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_document(document_id: int, db: Session = Depends(get_db)):
    deleted = document_service.delete_document(db, document_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Document not found")