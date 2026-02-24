from functools import cache
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class ServiceSettings(BaseSettings):
  __dotenv_dir = os.path.dirname(__file__)

  model_config = SettingsConfigDict(
    env_prefix='SERVICE_SETTING_', 
    env_file=(f"{__dotenv_dir}/.env",f"{__dotenv_dir}/.env.prod") , 
    env_file_encoding='utf-8'
    )

  environment: str
  flight_db_dsn: PostgresDsn

@cache
def get_settings() -> ServiceSettings:
  return ServiceSettings()