from typing import Optional
from pydantic import BaseModel
# import uuid

class Curso(BaseModel): #ja herda várias coisas, como validação de dados
    id: Optional[int] = None
    nome: str
    aulas: int
    horas: int
    instrutor: str
