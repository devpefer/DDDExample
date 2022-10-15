from dataclasses import dataclass
from src.Application.Descuentos.Commands.commands import InsertarDescuentoCommand
from src.Infrastructure.SQLAlchemy.base import Base
from sqlalchemy import Column, String, DECIMAL

class Descuento(Base):
    __tablename__ = 'PEINETAS_DESCUENTOS'
    Descuento = Column(String, primary_key=True)
    Descripcion = Column(String)
    Precio = Column(DECIMAL)
    
    def __init__(self,descuento, descripcion, precio):
        self.Descuento = descuento
        self.Descripcion = descripcion
        self.Precio = precio
    
    def __repr__(self):
        return f"Descuento({self.Descuento}, {self.Descripcion}, {self.Precio})"
        
    def __str__(self):
        return self.Descuento
    
    def Crear(self,descuentoCommand: InsertarDescuentoCommand):
        nuevoDescuento = Descuento(descuentoCommand.Descuento,descuentoCommand.Descripcion,descuentoCommand.Precio)
        return nuevoDescuento
    
    def ModificarDescripcion(self, descripcion):
        self.Descripcion = descripcion
        
    def ModificarPrecio(self, precio):
        self.Descripcion = precio