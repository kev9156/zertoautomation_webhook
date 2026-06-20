from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

#This loads your .env variables and validates them into a typed object.
class Settings(BaseSettings):
    environment: str = Field(default="production")
    debug: bool = Field(default=False)
    
    vc_host: str
    vc_user: str
    vc_pass: str

    # Directs Pydantic to read the local .env file
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()