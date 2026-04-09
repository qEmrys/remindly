from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "Remindly"
    APP_VERSION: str = "1.0.0"
    DATABASE_URL_SYNC: str
    DATABASE_URL_ASYNC: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()