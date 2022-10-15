from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from src.Application.Tamanyos.Commands.commands import CrearTamanyoCommand
from src.Domain.Tamanyos.tamanyo import Tamanyo
from src.Infrastructure.SQLAlchemy import secrets

class TamanyosRepository():
    def __init__(self):
        engine = create_engine(secrets.CONNECTIONSTRING)
        SessionMaker = sessionmaker(engine)
        SessionMaker.configure()
        
        self.session = SessionMaker()
        
    def CargarTodos(self):
        consulta = self.session.query(Tamanyo).all()
        return consulta
    
    def CargarPorId(self,primaryKey):
        consulta = self.session.query(Tamanyo).get((primaryKey,))
        return consulta
    
    def Eliminar(self,tamanyo: Tamanyo):
        self.session.delete(tamanyo)
    
    def Existe(self,tamanyo: str):
        consulta = self.session.query(exists().where(Tamanyo.Tamanyo == tamanyo)).scalar()
        return consulta