from dataclasses import dataclass
from decimal import Decimal
from src.Application.Acabados.Commands.commands import InsertarAcabadoCommand
from src.Infrastructure.SQLAlchemy.base import Base
from sqlalchemy import Column, String, DECIMAL

class Acabado(Base):
    __tablename__ = 'PEINETAS_ACABADOS'
    Acabado = Column(String, primary_key=True)
    Descripcion = Column(String)
    Precio = Column(DECIMAL)
    
    def __init__(self,acabado, descripcion, precio):
        self.Acabado = acabado
        self.Descripcion = descripcion
        self.Precio = precio
    
    def __repr__(self):
        return f"Acabado({self.Acabado}, {self.Descripcion}, {self.Precio})"
        
    def __str__(self):
        return self.Acabado
    
    def Crear(self,acabadoCommand: InsertarAcabadoCommand):
        nuevoAcabado = Acabado(acabadoCommand.Acabado,acabadoCommand.Descripcion, acabadoCommand.Precio)
        return nuevoAcabado
    
    def ModificarDescripcion(self, descripcion: str):
        self.Descripcion = descripcion
        
    def ModificarPrecio(self, precio: Decimal):
        self.Precio = precio