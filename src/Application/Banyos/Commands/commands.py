from pydantic import BaseModel
from decimal import Decimal

class InsertarBanyosCommand(BaseModel):
    Banyo: str
    Descripcion: str
    Precio: Decimal
    
class ModificarBanyosDescripcionCommand(BaseModel):
    Banyo: str
    NuevaDescripcion: str
    
class ModificarBanyosPrecioCommand(BaseModel):
    Banyo: str
    NuevoPrecio: Decimal