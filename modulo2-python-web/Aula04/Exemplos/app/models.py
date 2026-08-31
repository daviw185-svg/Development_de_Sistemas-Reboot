from pydantic import BaseModel, field_validator
from typing import Optional
from enum import Enum

# Enum: Define os valores aceitos para o campo cargo
# Aparece como dropdown no swagger(a página da API no Chrome) automaticamente

class CargoEnum(str, Enum):
    engMec = 'Engenheiro Mecânico'
    ti = 'TI'
    devrh = 'Desenvolvedor Red Hat'
    cine = 'Cinema'

# Schema de entrada: o que o cliente envia (SEM ID)
class UsuarioEntrada (BaseModel):

    cargo: str
    ativo: bool = True
    salario: Optional[float] = None

    @field_validator('nome')
    @classmethod
    def validar_nome(cls, valor: str) -> str:
        valor = valor.strip()
        if len(valor) < 3:
            raise ValueError('Mínimo 3 caracteres')
        return valor.title()

# Schema de saída: o que o servidor retorn (COM ID)
class UsuarioSaida(BaseModel):
    id: int
    nome: str
    email: str
    cargo: CargoEnum
    ativo: bool
    salario: Optional[float] = None