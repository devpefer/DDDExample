from dataclasses import dataclass
from decimal import Decimal
from src.Application.Banyos.Commands.commands import InsertarBanyosCommand
from src.Infrastructure.SQLAlchemy.base import Base
from sqlalchemy import Column, String, DECIMAL

class Banyo(Base):
    __tablename__ = 'PEINETAS_BANYOS'
    Banyo = Column(String, primary_key=True)
    Descripcion = Column(String)
    Precio = Column(DECIMAL)
    
    def __init__(self,banyo, descripcion, precio):
        self.Banyo = banyo
        self.Descripcion = descripcion
        self.Precio = precio
    
    def __repr__(self):
        return f"Banyo({self.Banyo}, {self.Descripcion}, {self.Precio})"
        
    def __str__(self):
        return self.Banyo
    
    def Crear(self,banyoCommand: InsertarBanyosCommand):
        nuevoBanyo = Banyo(banyoCommand.Banyo,banyoCommand.Descripcion, banyoCommand.Precio)
        return nuevoBanyo
    
    def ModificarDescripcion(self, descripcion: str):
        self.Descripcion = descripcion
        
    def ModificarPrecio(self, precio: Decimal):
        self.Precio = precio