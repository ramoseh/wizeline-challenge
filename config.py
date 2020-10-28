from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Challenge API"
    api_key: str

    class Config:
        env_file = ".env"
