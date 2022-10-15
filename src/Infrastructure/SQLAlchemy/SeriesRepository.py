from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from src.Application.Series.Commands.commands import CrearSerieCommand
from src.Domain.Series.serie import Serie
from src.Infrastructure.SQLAlchemy import secrets

class SeriesRepository():
    def __init__(self):
        engine = create_engine(secrets.CONNECTIONSTRING)
        SessionMaker = sessionmaker(engine)
        SessionMaker.configure()
        
        self.session = SessionMaker()
        
    def Cargar(self,primaryKey: str) -> Serie:
        consulta = self.session.query(Serie).get((primaryKey,))
        return consulta
        
    def CargarTodas(self):
        consulta = self.session.query(Serie).all()
        return consulta
        
    def Existe(self,serie: str):
        consulta = self.session.query(exists().where(Serie.Serie == serie)).scalar()
        return consulta
        
    def Eliminar(self,serie: Serie):
        self.session.delete(serie)