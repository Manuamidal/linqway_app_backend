from pydantic import BaseModel


class DocumentBase(BaseModel):
    prescription_id: int
    file_name: str
    file_url: str


class DocumentCreate(DocumentBase):
    pass


class DocumentItem(BaseModel):
    """Single document item inside a bulk request."""
    file_name: str
    file_url: str


class DocumentBulkCreate(BaseModel):
    """Attach multiple documents to one prescription at once."""
    prescription_id: int
    documents: list[DocumentItem]


class DocumentResponse(DocumentBase):
    id: int

    class Config:
        from_attributes = True