from src.Application.Clientes.Queries.readmodels import ObtenerClienteCIFReadModel, ObtenerClienteReadModel
from src.Infrastructure.SQLAlchemy.ClientesRepository import ClientesRepository

class QueryHandler():
    def __init__(self):
        self.clientesRepository = ClientesRepository()
        
    def ObtenerClientes(self):
        clientes = self.clientesRepository.CargarTodos()
        
        listClienteReadModel = []
        for cliente in clientes:
            clienteReadModel = ObtenerClienteReadModel()
            clienteReadModel.CIF = cliente.CIF
            clienteReadModel.RazonSocial = cliente.RazonSocial
            clienteReadModel.Direccion = cliente.Direccion
            clienteReadModel.Telefono = cliente.Telefono
            clienteReadModel.TelefonoMovil = cliente.TelefonoMovil
            clienteReadModel.CuentaBancaria = cliente.CuentaBancaria
            clienteReadModel.CorreoElectronico = cliente.CorreoElectronico
            listClienteReadModel.append(clienteReadModel)
        
        return listClienteReadModel
    
    def ObtenerCliente(self, cif: str):
        if not self.clientesRepository.Existe(cif):
            raise Exception(f"El cliente {cif} no existe")
        
        cliente = self.clientesRepository.Cargar(cif)

        clienteReadModel = ObtenerClienteReadModel()
        clienteReadModel.CIF = cliente.CIF
        clienteReadModel.RazonSocial = cliente.RazonSocial
        clienteReadModel.Direccion = cliente.Direccion
        clienteReadModel.Telefono = cliente.Telefono
        clienteReadModel.TelefonoMovil = cliente.TelefonoMovil
        clienteReadModel.CuentaBancaria = cliente.CuentaBancaria
        clienteReadModel.CorreoElectronico = cliente.CorreoElectronico
        
        return clienteReadModel
    
    def ObtenerClienteCIF(self, razonSocial: str):
        clienteCIF = self.clientesRepository.ObtenerClienteCIF(razonSocial)

        clienteReadModel = ObtenerClienteCIFReadModel()
        clienteReadModel.CIF = clienteCIF
        
        return clienteReadModel