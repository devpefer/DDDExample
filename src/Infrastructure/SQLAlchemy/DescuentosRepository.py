from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from src.Application.Descuentos.Commands.commands import InsertarDescuentoCommand
from src.Domain.Descuentos.descuento import Descuento
from src.Infrastructure.SQLAlchemy import secrets

class DescuentosRepository():
    def __init__(self):
        engine = create_engine(secrets.CONNECTIONSTRING)
        SessionMaker = sessionmaker(engine)
        SessionMaker.configure()
        
        self.session = SessionMaker()
        
    def Cargar(self,primaryKey: str) -> Descuento:
        consulta = self.session.query(Descuento).get((primaryKey,))
        return consulta
        
    def CargarTodos(self):
        consulta = self.session.query(Descuento).all()
        return consulta
        
    def Existe(self,descuento: str):
        consulta = self.session.query(exists().where(Descuento.Descuento == descuento)).scalar()
        return consulta
        
    def Eliminar(self,serie: Descuento):
        self.session.delete(serie)