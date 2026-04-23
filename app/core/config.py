from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:1234@localhost:5432/hospital_db"
    APP_NAME: str = "Liqway Medical API"
    DEBUG: bool = False

    class Config:
        env_file = ".env"


settings = Settings()