from src.Domain.Acabados.acabado import Acabado
from src.Infrastructure.SQLAlchemy.AcabadosRepository import AcabadosRepository
from src.Application.Acabados.Commands.commands import InsertarAcabadoCommand, ModificarAcabadoDescripcionCommand, ModificarAcabadoPrecioCommand

class CommandHandler():
    def __init__(self):
        self.acabadosRepository = AcabadosRepository()
        
    def Crear(self,command: InsertarAcabadoCommand):
        if self.acabadosRepository.Existe(command.Acabado):
            raise Exception(f'El acabado {command.Acabado} ya existe')
        
        acabado = Acabado.Crear(self,command)
        
        self.acabadosRepository.session.add(acabado)
        self.acabadosRepository.session.commit()
        
        return command
        
    def ModificarDescripcion(self,command: ModificarAcabadoDescripcionCommand):   
        if not self.acabadosRepository.Existe(command.Acabado):
            raise Exception(f'El acabado {command.Acabado} no existe')
        
        acabado = self.acabadosRepository.Cargar(command.Acabado)
        
        acabado.ModificarDescripcion(command.NuevaDescripcion)
        
        self.acabadosRepository.session.commit()

        return command
        
    def ModificarPrecio(self,command: ModificarAcabadoPrecioCommand):   
        if not self.acabadosRepository.Existe(command.Acabado):
            raise Exception(f'El acabado {command.Acabado} no existe')
        
        acabado = self.acabadosRepository.Cargar(command.Acabado)
        
        acabado.ModificarPrecio(command.NuevoPrecio)
        
        self.acabadosRepository.session.commit()

        return command
        
    def Eliminar(self,acabado):   
        if not self.acabadosRepository.Existe(acabado):
            raise Exception(f'El acabado {acabado} no existe')
        
        objAcabado = self.acabadosRepository.Cargar(acabado)
        
        self.acabadosRepository.Eliminar(objAcabado)
        
        self.acabadosRepository.session.commit()