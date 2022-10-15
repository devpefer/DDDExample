from datetime import datetime
from decimal import Decimal

class ObtenerPedidosReadModel():
    CodigoPedido: str
    Cliente: str
    FechaPedido: datetime
    FechaEntrega: datetime
    Estado: str
    Importe: Decimal
    Observaciones: str
    Lineas: list
    
class ObtenerUltimoCodigoPedidoReadModel():
    CodigoPedido: str