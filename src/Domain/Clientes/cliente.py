from dataclasses import dataclass
from src.Application.Clientes.Commands.commands import InsertarClienteCommand
from src.Infrastructure.SQLAlchemy.base import Base
from sqlalchemy import Column, String

class Cliente(Base):
    __tablename__ = 'CLIENTES'
    CIF = Column(String, primary_key=True)
    RazonSocial = Column(String)
    Direccion = Column(String)
    Telefono = Column(String)
    TelefonoMovil = Column(String)
    CuentaBancaria = Column(String)
    CorreoElectronico = Column(String)
    
    def __init__(self,CIF, razonSocial, direccion,telefono,telefonoMovil,cuentaBancaria,correoElectronico):
        self.CIF = CIF
        self.RazonSocial = razonSocial
        self.Direccion = direccion
        self.Telefono = telefono
        self.TelefonoMovil = telefonoMovil
        self.CuentaBancaria = cuentaBancaria
        self.CorreoElectronico = correoElectronico
    
    def __repr__(self):
        return f"Cliente({self.CIF}, {self.RazonSocial}, {self.Direccion}, {self.Telefono}, {self.TelefonoMovil}, {self.CuentaBancaria}, {self.CorreoElectronico})"
        
    def __str__(self):
        return self.CIF
    
    def Crear(self,commandCliente: InsertarClienteCommand):
        nuevoCliente = Cliente(commandCliente.CIF,commandCliente.RazonSocial,commandCliente.Direccion, commandCliente.Telefono, commandCliente.TelefonoMovil, commandCliente.CuentaBancaria, commandCliente.CorreoElectronico)
        return nuevoCliente
    
    def ModificarRazonSocial(self, razonSocial):
        self.RazonSocial = razonSocial
        
    def ModificarDireccion(self, direccion):
        self.Direccion = direccion

    def ModificarTelefono(self, telefono):
        self.Telefono = telefono
    
    def ModificarTelefonoMovil(self, telefonoMovil):
        self.TelefonoMovil = telefonoMovil
        
    def ModificarCuentaBancaria(self, cuentaBancaria):
        self.CuentaBancaria = cuentaBancaria
        
    def ModificarCorreoElectronico(self, correoElectronico):
        self.CorreoElectronico = correoElectronico