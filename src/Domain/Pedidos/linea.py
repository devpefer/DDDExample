from dataclasses import dataclass
from src.Application.Pedidos.Commands.commands import CrearLineaCommand
from src.Infrastructure.SQLAlchemy.base import Base
from sqlalchemy import Column, String, DECIMAL,DATETIME, INTEGER

class PedidoLinea(Base):
    __tablename__ = 'PEDIDOS_LINEAS'
    CodigoPedido = Column(String, primary_key=True)
    Referencia = Column(String, primary_key=True)
    Serie = Column(String, primary_key=True)
    Tamanyo = Column(String, primary_key=True)
    Banyo = Column(String, primary_key=True)
    Acabado = Column(String, primary_key=True)
    Descuento = Column(String)
    Unidades = Column(INTEGER)
    Precio = Column(DECIMAL)
    Subtotal = Column(DECIMAL)
    
    def __init__(self,codigoPedido, referencia, serie, tamanyo, banyo, acabado, descuento, unidades, precio, subtotal):
        self.CodigoPedido = codigoPedido
        self.Referencia = referencia
        self.Serie = serie
        self.Tamanyo = tamanyo
        self.Banyo = banyo
        self.Acabado = acabado
        self.Descuento = descuento
        self.Unidades = unidades
        self.Precio = precio
        self.Subtotal = subtotal
    
    def __repr__(self):
        return f"PedidoLinea({self.CodigoPedido}, {self.Referencia}, {self.Serie}, {self.Tamanyo}, {self.Banyo}, {self.Acabado}, {self.Descuento}, {self.Unidades}, {self.Precio}, {self.Subtotal})"
        
    def __str__(self):
        return self.Referencia
    
    def CrearLinea(self,linea: CrearLineaCommand, serie, tamanyo, precio, subtotal):
        nuevaLinea = PedidoLinea(linea.CodigoPedido,linea.Referencia,serie,tamanyo,linea.Banyo,linea.Acabado,linea.Descuento,linea.Unidades,precio,subtotal)
        return nuevaLinea