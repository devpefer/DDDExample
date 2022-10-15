from src.Domain.Pedidos.cabecera import PedidoCabecera
from src.Domain.Pedidos.linea import PedidoLinea
from src.Infrastructure.SQLAlchemy.PedidosRepository import PedidosRepository
from src.Infrastructure.SQLAlchemy.ReferenciasRepository import ReferenciasRepository
from src.Infrastructure.SQLAlchemy.SeriesRepository import SeriesRepository
from src.Infrastructure.SQLAlchemy.TamanyosRepository import TamanyosRepository
from src.Infrastructure.SQLAlchemy.AcabadosRepository import AcabadosRepository
from src.Infrastructure.SQLAlchemy.ClientesRepository import ClientesRepository
from src.Infrastructure.SQLAlchemy.BanyosRepository import BanyosRepository
from src.Infrastructure.SQLAlchemy.DescuentosRepository import DescuentosRepository
from src.Application.Pedidos.Commands.commands import CrearCabeceraCommand, CrearLineaCommand

class CommandHandler():
    def __init__(self):
        self.pedidosRepository = PedidosRepository()
        self.referenciasRepository = ReferenciasRepository()
        self.seriesRepository = SeriesRepository()
        self.tamanyosRepository = TamanyosRepository()
        self.acabadosRepository = AcabadosRepository()
        self.clientesRepository = ClientesRepository()
        self.banyosRepository = BanyosRepository()
        self.descuentosRepository = DescuentosRepository()
        
    def CrearCabecera(self,command: CrearCabeceraCommand):
        if not self.clientesRepository.Existe(command.Cliente):
            raise Exception(f'El cliente {command.Cliente} no existe')
                
        cabecera = PedidoCabecera.CrearCabecera(self,command)
        
        self.pedidosRepository.session.add(cabecera)
        self.pedidosRepository.session.commit()

        return command
        
    def CrearLinea(self,command: CrearLineaCommand):
        if not self.banyosRepository.Existe(command.Banyo):
            raise Exception(f'El baño {command.Banyo} no existe')
        
        if not self.acabadosRepository.Existe(command.Acabado) and command.Acabado != '':
            raise Exception(f'El acabado {command.Acabado} no existe')
        
        if not self.referenciasRepository.Existe(command.Referencia):
            raise Exception(f'La referencia {command.Referencia} no existe')
        
        if not self.descuentosRepository.Existe(command.Descuento) and command.Descuento != '':
            raise Exception(f'El descuento {command.Descuento} no existe')
        
        referencia = self.referenciasRepository.Cargar(command.Referencia)
        banyo = self.banyosRepository.Cargar(command.Banyo)
        descuento = self.descuentosRepository.Cargar(command.Descuento)
        acabado = self.acabadosRepository.Cargar(command.Acabado)
        
        if acabado == None:
            acabado = self.acabadosRepository.Cargar('NINGUNO')
            command.Acabado = acabado.Acabado
        
        precio = referencia.Precio + banyo.Precio + acabado.Precio
        
        if descuento != None:
            precio -= descuento.Precio
            
        subtotal = command.Unidades * precio
        
        linea = PedidoLinea.CrearLinea(self,command,referencia.Serie,referencia.Tamanyo,precio,subtotal)
        
        self.pedidosRepository.session.add(linea)
        self.pedidosRepository.session.commit()

        return command
        
    def Eliminar(self,codigoPedido):   
        if not self.pedidosRepository.Existe(codigoPedido):
            raise Exception(f'El pedido {codigoPedido} no existe')
        
        objPedidoCabecera = self.pedidosRepository.CargarCabecera(codigoPedido)
        listaObjPedidoLinea = self.pedidosRepository.CargarLineasPorCodigoDePedido(codigoPedido)
        
        for linea in listaObjPedidoLinea:
            self.pedidosRepository.EliminarLinea(linea)
        
        self.pedidosRepository.session.commit()
        
        self.pedidosRepository.EliminarCabecera(objPedidoCabecera)
        
        self.pedidosRepository.session.commit()
        