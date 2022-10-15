from dataclasses import dataclass
from decimal import Decimal

@dataclass
class ObtenerReferenciasReadModel():
    Serie: str
    Tamanyo: str
    Referencia: str
    Precio: Decimal