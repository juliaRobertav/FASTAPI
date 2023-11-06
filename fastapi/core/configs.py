from pydantic.v1 import BaseSettings
from sqlalchemy.orm import declarative_base

class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """

    API_V1_STR: str = '/api/v1' # não precisar inserir via hard coding
    DB_URL: str = "mysql+asyncmy://root@127.0.0.1:3306/etscursos" #ideal -> user:password

    DBBaseModel = declarative_base() # models herdam todos os reursos do sqlalchemy

    class Config:
        case_sensitive = True


settings = Settings() # declarando variável aqui 
# assim qualquer lugar que importar terá acesso a essas configurações