from pydantic import BaseModel
from decimal import Decimal

class InsertarDescuentoCommand(BaseModel):
    Descuento: str
    Descripcion: str
    Precio: Decimal
    
class ModificarDescuentoDescripcionCommand(BaseModel):
    Descuento: str
    NuevaDescripcion: str
    
class ModificarDescuentoPrecioCommand(BaseModel):
    Descuento: str
    NuevoPrecio: Decimal