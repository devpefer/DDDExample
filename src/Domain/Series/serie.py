from dataclasses import dataclass
from src.Application.Series.Commands.commands import CrearSerieCommand
from src.Infrastructure.SQLAlchemy.base import Base
from sqlalchemy import Column, Integer, String

class Serie(Base):
    __tablename__ = 'PEINETAS_SERIES'
    Serie = Column(String, primary_key=True)
    Titulo = Column(String)
    Descripcion = Column(String)
    
    def __init__(self, serie, titulo, descripcion):
        self.Serie = serie
        self.Titulo = titulo
        self.Descripcion = descripcion
    
    def __repr__(self):
        return f"Serie({self.Serie}, {self.Titulo}, {self.Descripcion})"
        
    def __str__(self):
        return self.Serie
    
    def Crear(self,serieCommand: CrearSerieCommand):
        nuevaSerie = Serie(serieCommand.Serie,serieCommand.Titulo,serieCommand.Descripcion)
        return nuevaSerie
        
    def ModificarTitulo(self, titulo):
        self.Titulo = titulo
    
    def ModificarDescripcion(self, descripcion):
        self.Descripcion = descripcion