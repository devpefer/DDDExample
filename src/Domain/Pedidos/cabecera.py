from dataclasses import dataclass
from src.Application.Pedidos.Commands.commands import CrearCabeceraCommand
from src.Infrastructure.SQLAlchemy.base import Base
from sqlalchemy import Column, String, DECIMAL,DATETIME, INTEGER

class PedidoCabecera(Base):
    __tablename__ = 'PEDIDOS_CABECERAS'
    CodigoPedido = Column(String, primary_key=True)
    Cliente = Column(String)
    FechaPedido = Column(DATETIME)
    FechaEntrega = Column(DATETIME)
    Estado = Column(String)
    Importe = Column(DECIMAL)
    Observaciones = Column(String)
    Lineas = []
    
    def __init__(self,codigoPedido, cliente, fechaPedido, fechaEntrega, estado, importe, observaciones):
        self.CodigoPedido = codigoPedido
        self.Cliente = cliente
        self.FechaPedido = fechaPedido
        self.FechaEntrega = fechaEntrega
        self.Estado = estado
        self.Importe = importe
        self.Observaciones = observaciones
    
    def __repr__(self):
        return f"PedidoCabecera({self.CodigoPedido}, {self.Cliente}, {self.FechaPedido}, {self.FechaEntrega}, {self.Estado}, {self.Importe}, {self.Observaciones}, {self.Lineas})"
        
    def __str__(self):
        return self.CodigoPedido
        
    def CrearCabecera(self,cabecera: CrearCabeceraCommand):
        nuevaCabecera = PedidoCabecera(cabecera.CodigoPedido,cabecera.Cliente,cabecera.FechaPedido,cabecera.FechaEntrega,cabecera.Estado,cabecera.Importe,cabecera.Observaciones)
        self.session.add(nuevaCabecera)