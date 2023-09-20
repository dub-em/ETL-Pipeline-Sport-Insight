from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    host: str
    port: str
    database: str
    user: str
    password: str


    class Config:
        env_file = ".env"

settings = Settings()