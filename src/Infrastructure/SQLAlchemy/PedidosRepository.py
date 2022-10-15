from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from src.Domain.Pedidos.pedido import Pedido
from src.Domain.Pedidos.cabecera import PedidoCabecera
from src.Domain.Pedidos.linea import PedidoLinea
from src.Infrastructure.SQLAlchemy import secrets

class PedidosRepository():
    def __init__(self):
        engine = create_engine(secrets.CONNECTIONSTRING)
        SessionMaker = sessionmaker(engine)
        SessionMaker.configure()
        
        self.session = SessionMaker()

    def CargarCabeceras(self):
        consultaCabecera = self.session.query(PedidoCabecera).all()
        return consultaCabecera
        
    def CargarCabecera(self,primaryKey: str) -> PedidoCabecera:
        consultaCabecera = self.session.query(PedidoCabecera).get((primaryKey,))
        return consultaCabecera
    
    def CargarLineasPorCodigoDePedido(self, codigoPedido) -> list:
        consultaLineas = self.session.query(PedidoLinea).filter(PedidoLinea.CodigoPedido == codigoPedido)
        return consultaLineas
        
    def CargarTodos(self):
        listaPedidos = []
        consultaCabeceras = self.session.query(PedidoCabecera).all()
        
        for cabecera in consultaCabeceras:
            listaLineas = []
            consultaLineas = self.session.query(PedidoLinea).filter(PedidoLinea.CodigoPedido == cabecera.CodigoPedido)
            for linea in consultaLineas:
                listaLineas.append(linea)
            pedido = Pedido(cabecera, listaLineas)
            listaPedidos.append(pedido)
        
        return listaPedidos
    
    def ObtenerUltimoCodigoPedido(self) -> PedidoCabecera:
        consultaLineas = self.session.query(PedidoCabecera).order_by(desc(PedidoCabecera.CodigoPedido)).first()
        return consultaLineas
        
    def Existe(self,codigoPedido: str):
        consulta = self.session.query(exists().where(PedidoCabecera.CodigoPedido == codigoPedido)).scalar()
        return consulta
        
    def EliminarCabecera(self,cabecera: PedidoCabecera):
        self.session.delete(cabecera)
        
    def EliminarLinea(self,linea: PedidoLinea):
        self.session.delete(linea)