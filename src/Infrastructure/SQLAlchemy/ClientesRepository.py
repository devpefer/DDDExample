from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from src.Application.Clientes.Commands.commands import InsertarClienteCommand
from src.Domain.Clientes.cliente import Cliente
from src.Infrastructure.SQLAlchemy import secrets

class ClientesRepository():
    def __init__(self):
        engine = create_engine(secrets.CONNECTIONSTRING)
        SessionMaker = sessionmaker(engine)
        SessionMaker.configure()
        
        self.session = SessionMaker()
        
    def CargarTodos(self):
        consulta = self.session.query(Cliente).all()
        return consulta
    
    def Cargar(self,primaryKey: str) -> Cliente:
        consulta = self.session.query(Cliente).get((primaryKey,))
        return consulta
    
    def ObtenerClienteCIF(self, razonSocial: str) -> str:
        consulta = self.session.query(Cliente).filter(Cliente.RazonSocial == razonSocial).first()
        return consulta.CIF
    
    def Eliminar(self,cliente: Cliente):
        self.session.delete(cliente)
    
    def Existe(self,cif: str):
        consulta = self.session.query(exists().where(Cliente.CIF == cif)).scalar()
        return consulta