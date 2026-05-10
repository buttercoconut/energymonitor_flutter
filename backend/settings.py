# Settings for the application
# Use pydantic BaseSettings for environment variables
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Energy Monitor API"
    debug: bool = False
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()
