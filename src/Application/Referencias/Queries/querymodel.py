from decimal import Decimal
from pydantic import BaseModel

class ObtenerReferenciasQueryModel(BaseModel):
    IdModelo: int
    IdTamanyo: int