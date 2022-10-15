from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from src.Application.Referencias.Commands.commands import CrearReferenciaCommand
from src.Domain.Referencias.referencia import Referencia
from src.Infrastructure.SQLAlchemy import secrets

class ReferenciasRepository():
    def __init__(self):
        engine = create_engine(secrets.CONNECTIONSTRING)
        SessionMaker = sessionmaker(engine)
        SessionMaker.configure()
        
        self.session = SessionMaker()
        
    def CargarTodas(self):
        consulta = self.session.query(Referencia).order_by(Referencia.Referencia).all()
        return consulta
    
    def Cargar(self,referencia: str) -> Referencia:
        consulta = self.session.query(Referencia).filter(Referencia.Referencia == referencia)
        return consulta[0]
    
    def CargarPorSerie(self,serie: str):
        consulta = self.session.query(Referencia).filter(Referencia.Serie == serie).order_by(Referencia.Referencia)
        return consulta
    
    def CargarPorTamanyo(self,tamanyo: str):
        consulta = self.session.query(Referencia).filter(Referencia.Tamanyo == tamanyo)
        return consulta
    
    def CargarPorSerieYTamanyo(self,serie: str, tamanyo: str):
        consulta = self.session.query(Referencia).filter(Referencia.Serie == serie, Referencia.Tamanyo == tamanyo)
        return consulta
    
    def Eliminar(self,referencia: Referencia):
        self.session.delete(referencia)
    
    def Existe(self,referencia: str):
        consulta = self.session.query(exists().where(Referencia.Referencia == referencia)).scalar()
        return consulta