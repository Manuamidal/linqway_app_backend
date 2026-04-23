from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.db.database import Base, engine
from app.controllers import doctor_controller, patient_controller,prescription_controller, document_controller

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(doctor_controller.router, prefix="/api/v1")
app.include_router(patient_controller.router, prefix="/api/v1")
app.include_router(prescription_controller.router, prefix="/api/v1")
app.include_router(document_controller.router, prefix="/api/v1")


@app.get("/")
def health_check():
    return {"status": "ok", "app": settings.APP_NAME}

