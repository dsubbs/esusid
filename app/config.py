from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Telegram Bot Token
    telegram_bot_token: str

    # Database connection details
    database_url: str

    class Config:
        # Assuming your .env file is in the same directory as this config.py,
        # or specify the path with env_file = "path/to/.env"
        env_file = "../.env"
        env_file_encoding = 'utf-8'


# Create a settings instance to be imported in other modules
settings = Settings()
