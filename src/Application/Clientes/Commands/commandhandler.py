from src.Domain.Clientes.cliente import Cliente
from src.Infrastructure.SQLAlchemy.ClientesRepository import ClientesRepository
from src.Application.Clientes.Commands.commands import InsertarClienteCommand, ModificarClienteCorreoElectronicoCommand, ModificarClienteCuentaBancariaCommand, ModificarClienteDireccionCommand, ModificarClienteRazonSocialCommand, ModificarClienteTelefonoCommand, ModificarClienteTelefonoMovilCommand

class CommandHandler():
    def __init__(self):
        self.clientesRepository = ClientesRepository()
#region Crear
    def Crear(self,command: InsertarClienteCommand):
        if self.clientesRepository.Existe(command.CIF):
            raise Exception(f'El cliente {command.CIF} ya existe')
        
        cliente = Cliente.Crear(self,command)
        
        self.clientesRepository.session.add(cliente)
        self.clientesRepository.session.commit()
        
        return command
#endregion

#region Modificar
    def ModificarRazonSocial(self,command: ModificarClienteRazonSocialCommand):        
        if not self.clientesRepository.Existe(command.CIF):
            raise Exception(f'El cliente {command.CIF} no existe')
        
        cliente = self.clientesRepository.Cargar(command.CIF)
        
        cliente.ModificarRazonSocial(cliente, command.NuevaRazonSocial)
        
        self.clientesRepository.session.commit()
        
        return command
        
    def ModificarDireccion(self,command: ModificarClienteDireccionCommand):        
        if not self.clientesRepository.Existe(command.CIF):
            raise Exception(f'El cliente {command.CIF} no existe')
        
        cliente = self.clientesRepository.Cargar(command.CIF)
        
        cliente.ModificarDireccion(cliente, command.NuevaDireccion)
        
        self.clientesRepository.session.commit()
        
        return command
        
    def ModificarTelefono(self,command: ModificarClienteTelefonoCommand):        
        if not self.clientesRepository.Existe(command.CIF):
            raise Exception(f'El cliente {command.CIF} no existe')
        
        cliente = self.clientesRepository.Cargar(command.CIF)
        
        cliente.ModificarTelefono(cliente, command.NuevoTelefono)
        
        self.clientesRepository.session.commit()
        
        return command
        
    def ModificarTelefonoMovil(self,command: ModificarClienteTelefonoMovilCommand):        
        if not self.clientesRepository.Existe(command.CIF):
            raise Exception(f'El cliente {command.CIF} no existe')
        
        cliente = self.clientesRepository.Cargar(command.CIF)
        
        cliente.ModificarTelefonoMovil(cliente, command.NuevoTelefonoMovil)
        
        self.clientesRepository.session.commit()
        
        return command
        
    def ModificarCuentaBancaria(self,command: ModificarClienteCuentaBancariaCommand):        
        if not self.clientesRepository.Existe(command.CIF):
            raise Exception(f'El cliente {command.CIF} no existe')
        
        cliente = self.clientesRepository.Cargar(command.CIF)
        
        cliente.ModificarCuentaBancaria(cliente, command.NuevaCuentaBancaria)
        
        self.clientesRepository.session.commit()
        
        return command
        
    def ModificarCorreoElectronico(self,command: ModificarClienteCorreoElectronicoCommand):        
        if not self.clientesRepository.Existe(command.CIF):
            raise Exception(f'El cliente {command.CIF} no existe')
        
        cliente = self.clientesRepository.Cargar(command.CIF)
        
        cliente.ModificarCorreoElectronico(cliente, command.NuevoCorreoElectronico)
        
        self.clientesRepository.session.commit()
        
        return command
#endregion

#region Eliminar        
    def Eliminar(self,cif: str):
        if not self.clientesRepository.Existe(cif):
            raise Exception(f'El cliente {cif} no existe')
        
        cliente = self.clientesRepository.Cargar(cif)
        
        self.clientesRepository.Eliminar(cliente)
        
        self.clientesRepository.session.commit()
#endregion