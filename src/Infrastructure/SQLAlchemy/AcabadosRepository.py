from decimal import Decimal
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from src.Application.Acabados.Commands.commands import InsertarAcabadoCommand
from src.Domain.Acabados.acabado import Acabado
from src.Infrastructure.SQLAlchemy import secrets

class AcabadosRepository():
    def __init__(self):
        engine = create_engine(secrets.CONNECTIONSTRING)
        SessionMaker = sessionmaker(engine)
        SessionMaker.configure()
        
        self.session = SessionMaker()
        
    def Cargar(self,primaryKey: str) -> Acabado:
        consulta = self.session.query(Acabado).get((primaryKey,))
        return consulta
        
    def CargarTodos(self):
        consulta = self.session.query(Acabado).all()
        return consulta
        
    def Existe(self,acabado: str):
        consulta = self.session.query(exists().where(Acabado.Acabado == acabado)).scalar()
        return consulta
        
    def Eliminar(self,acabado: Acabado):
        self.session.delete(acabado)