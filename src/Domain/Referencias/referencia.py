from src.Application.Referencias.Commands.commands import CrearReferenciaCommand
from src.Infrastructure.SQLAlchemy.base import Base
from sqlalchemy import Column, String, DECIMAL

class Referencia(Base):
    __tablename__ = 'PEINETAS_REFERENCIAS'
    Serie = Column(String, primary_key=True)
    Tamanyo = Column(String, primary_key=True)
    Referencia = Column(String, primary_key=True)
    Precio = Column(DECIMAL)
    
    def __init__(self,Serie, Tamanyo, Referencia, Precio):
        self.Serie = Serie
        self.Tamanyo = Tamanyo
        self.Referencia = Referencia
        self.Precio = Precio
    
    def __repr__(self):
        return f"Referencia({self.Serie}, {self.Tamanyo}, {self.Referencia}, {self.Precio})"
        
    def __str__(self):
        return self.Referencia
    
    def Crear(self,commandReferencia: CrearReferenciaCommand):
        nuevaReferencia = Referencia(commandReferencia.Serie,commandReferencia.Tamanyo,commandReferencia.Referencia, commandReferencia.Precio)
        return nuevaReferencia
        
    def ModificarPrecio(self, precio):
        self.Precio = precio