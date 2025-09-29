from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database
    DB_CONNECTION: str
    DB_HOST: str
    DB_PORT: str
    DB_DATABASE: str
    DB_USERNAME: str
    DB_PASSWORD: str
    
    # Email (optional nếu không dùng)
    MAIL_USERNAME: str = ""
    MAIL_PASSWORD: str = ""
    MAIL_FROM: str = ""
    MAIL_PORT: str = "587"
    MAIL_SERVER: str = ""
    MAIL_TLS: str = "True"
    MAIL_SSL: str = "False"
    USE_CREDENTIALS: str = "True"

    model_config = {
        "env_file": "api/.env",
        "env_file_encoding": "utf-8"
    }