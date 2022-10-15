from decimal import Decimal
from pydantic import BaseModel

class CrearTamanyoCommand(BaseModel):
    Tamanyo: str