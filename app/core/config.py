from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "csc"
   
    Backend_URL: str
    Frontend_URL: str

    #database
    DATABASE_URL: str

    # load config from .env file
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
        )

settings = Settings()
