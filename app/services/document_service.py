from sqlalchemy.orm import Session
from app.models.document import Document
from app.schemas.document import DocumentCreate, DocumentBulkCreate


def get_documents_by_prescription(db: Session, prescription_id: int) -> list[Document]:
    return db.query(Document).filter(Document.prescription_id == prescription_id).all()


def create_document(db: Session, data: DocumentCreate) -> Document:
    doc = Document(**data.model_dump())
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc


def create_documents_bulk(db: Session, data: DocumentBulkCreate) -> list[Document]:
    """Insert multiple documents for one prescription in a single transaction."""
    docs = [
        Document(
            prescription_id=data.prescription_id,
            file_name=item.file_name,
            file_url=item.file_url,
        )
        for item in data.documents
    ]
    db.add_all(docs)
    db.commit()
    for doc in docs:
        db.refresh(doc)
    return docs


def delete_document(db: Session, document_id: int) -> bool:
    doc = db.query(Document).filter(Document.id == document_id).first()
    if not doc:
        return False
    db.delete(doc)
    db.commit()
    return True