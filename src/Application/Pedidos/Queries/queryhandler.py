from src.Application.Pedidos.Queries.readmodels import ObtenerPedidosReadModel, ObtenerUltimoCodigoPedidoReadModel
from src.Infrastructure.SQLAlchemy.PedidosRepository import PedidosRepository
from src.Infrastructure.SQLAlchemy.ClientesRepository import ClientesRepository

class QueryHandler():
    def __init__(self):
        self.pedidosRepository = PedidosRepository()
        self.clientesRepository = ClientesRepository()
     
    def ObtenerPedidos(self):        
        cabeceras = self.pedidosRepository.CargarCabeceras()
        
        listaPedidosReadModel = []
        for cabecera in cabeceras:
            cliente = self.clientesRepository.Cargar(cabecera.Cliente)
            pedidoReadModel = ObtenerPedidosReadModel()
            pedidoReadModel.CodigoPedido = cabecera.CodigoPedido
            pedidoReadModel.Cliente = cliente.RazonSocial
            pedidoReadModel.FechaPedido = cabecera.FechaPedido
            pedidoReadModel.FechaEntrega = cabecera.FechaEntrega
            pedidoReadModel.Estado = cabecera.Estado
            pedidoReadModel.Importe = cabecera.Importe
            pedidoReadModel.Observaciones = cabecera.Observaciones
            pedidoReadModel.Lineas = []
            
            lineas = self.pedidosRepository.CargarLineasPorCodigoDePedido(cabecera.CodigoPedido)
            for linea in lineas:
                pedidoReadModel.Lineas.append(linea)

            listaPedidosReadModel.append(pedidoReadModel)
        
        return listaPedidosReadModel    
        
    def ObtenerPedido(self,codigoPedido):
        if not self.pedidosRepository.Existe(codigoPedido):
            raise Exception(f"El pedido {codigoPedido} no existe")
        
        cabecera = self.pedidosRepository.CargarCabecera(codigoPedido)
        lineas = self.pedidosRepository.CargarLineasPorCodigoDePedido(codigoPedido)
        cliente = self.clientesRepository.Cargar(cabecera.Cliente)
        

        pedidoReadModel = ObtenerPedidosReadModel()
        pedidoReadModel.CodigoPedido = cabecera.CodigoPedido
        pedidoReadModel.Cliente = cliente.RazonSocial
        pedidoReadModel.FechaPedido = cabecera.FechaPedido
        pedidoReadModel.FechaEntrega = cabecera.FechaEntrega
        pedidoReadModel.Estado = cabecera.Estado
        pedidoReadModel.Importe = cabecera.Importe
        pedidoReadModel.Observaciones = cabecera.Observaciones
        pedidoReadModel.Lineas = []
        
        for linea in lineas:
            pedidoReadModel.Lineas.append(linea)
        
        return pedidoReadModel
    
    def ObtenerUltimoCodigoPedido(self):
        codigoPedido = self.pedidosRepository.ObtenerUltimoCodigoPedido()
        
        if codigoPedido == None:
            codigoPedido = ObtenerUltimoCodigoPedidoReadModel()
            codigoPedido.CodigoPedido = "1000000000"
        
        codigoPedidoReadModel = ObtenerUltimoCodigoPedidoReadModel()
        codigoPedidoReadModel.CodigoPedido = codigoPedido.CodigoPedido
        
        return codigoPedidoReadModel