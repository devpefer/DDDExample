from dataclasses import dataclass
from src.Application.Tamanyos.Commands.commands import CrearTamanyoCommand
from src.Infrastructure.SQLAlchemy.base import Base
from sqlalchemy import Column, Integer, String

class Tamanyo(Base):
    __tablename__ = 'PEINETAS_TAMANYOS'
    Tamanyo = Column(String, primary_key=True)
    
    def __init__(self,tamanyo):
        self.Tamanyo = tamanyo
    
    def __repr__(self):
        return f"Tamanyo({self.Tamanyo})"
        
    def __str__(self):
        return self.Tamanyo
    
    def Crear(self,commandTamanyo: CrearTamanyoCommand):
        nuevoTamanyo = Tamanyo(commandTamanyo.Tamanyo)
        return nuevoTamanyo