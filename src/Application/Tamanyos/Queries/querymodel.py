from decimal import Decimal
from pydantic import BaseModel

class ObtenerTamanyosQueryModel(BaseModel):
    Tamanyo: str