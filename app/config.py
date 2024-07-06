from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    #OTHER
    SECRET_KEY: str
    CIPHER: str
    #BD
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL(self):
        user = f'{self.DB_USER}:{self.DB_PASS}'
        database = f'localhost:{self.DB_PORT}/{self.DB_NAME}'

        return f'postgresql+asyncpg://{user}@{database}'

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
