from pydantic import BaseModel
from decimal import Decimal

class InsertarAcabadoCommand(BaseModel):
    Acabado: str
    Descripcion: str
    Precio: Decimal
    
class ModificarAcabadoDescripcionCommand(BaseModel):
    Acabado: str
    NuevaDescripcion: str
    
class ModificarAcabadoPrecioCommand(BaseModel):
    Acabado: str
    NuevoPrecio: Decimal