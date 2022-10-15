from decimal import Decimal
from pydantic import BaseModel
    
class CrearReferenciaCommand(BaseModel):
    Serie: str
    Tamanyo: str
    Referencia: str
    Precio: Decimal
    
class ModificarReferenciaPrecioCommand(BaseModel):
    Referencia: str
    Precio: Decimal