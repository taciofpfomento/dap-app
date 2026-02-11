from functools import cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class ServiceSettings(BaseSettings):
  model_config = SettingsConfigDict(env_prefix='SERVICE_SETTING_', env_file=(".env",".env.prod") , env_file_encoding='utf-8')

  environment: str
  postgres_password: str

@cache
def get_settings() -> ServiceSettings:
  return ServiceSettings()
