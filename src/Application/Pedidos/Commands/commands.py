from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel

class CrearPedidoCommand(BaseModel):
    CodigoPedido: str
    Cliente: str
    FechaPedido: datetime
    FechaEntrega: datetime
    Estado: str
    Importe: Decimal
    Observaciones: str
    
class CrearCabeceraCommand(BaseModel):
    CodigoPedido: str
    Cliente: str
    FechaPedido: datetime
    FechaEntrega: datetime
    Estado: str
    Importe: Decimal
    Observaciones: str
    
class CrearLineaCommand(BaseModel):
    CodigoPedido: str
    Referencia: str
    Banyo: str
    Acabado: str
    Descuento: str
    Unidades: int