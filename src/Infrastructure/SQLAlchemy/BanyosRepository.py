from decimal import Decimal
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from src.Application.Banyos.Commands.commands import InsertarBanyosCommand
from src.Domain.Banyos.banyo import Banyo
from src.Infrastructure.SQLAlchemy import secrets

class BanyosRepository():
    def __init__(self):
        engine = create_engine(secrets.CONNECTIONSTRING)
        SessionMaker = sessionmaker(engine)
        SessionMaker.configure()
        
        self.session = SessionMaker()
        
    def Cargar(self,primaryKey: str) -> Banyo:
        consulta = self.session.query(Banyo).get((primaryKey,))
        return consulta
        
    def CargarTodos(self):
        consulta = self.session.query(Banyo).all()
        return consulta
        
    def Existe(self,banyo: str):
        consulta = self.session.query(exists().where(Banyo.Banyo == banyo)).scalar()
        return consulta
        
    def Eliminar(self,banyo: Banyo):
        self.session.delete(banyo)