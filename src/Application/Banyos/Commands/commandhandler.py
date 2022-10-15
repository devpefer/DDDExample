from src.Domain.Banyos.banyo import Banyo
from src.Infrastructure.SQLAlchemy.BanyosRepository import BanyosRepository
from src.Application.Banyos.Commands.commands import InsertarBanyosCommand, ModificarBanyosDescripcionCommand, ModificarBanyosPrecioCommand

class CommandHandler():
    def __init__(self):
        self.banyosRepository = BanyosRepository()
        
    def Crear(self,command: InsertarBanyosCommand):
        if self.banyosRepository.Existe(command.Banyo):
            raise Exception(f'El banyo {command.Banyo} ya existe')
        
        banyo = Banyo.Crear(self,command)
        
        self.banyosRepository.session.add(banyo)
        self.banyosRepository.session.commit()
        
        return command
        
    def ModificarDescripcion(self,command: ModificarBanyosDescripcionCommand):   
        if not self.banyosRepository.Existe(command.Banyo):
            raise Exception(f'El banyo {command.Banyo} no existe')
        
        banyo = self.banyosRepository.Cargar(command.Banyo)
        
        banyo.ModificarDescripcion(command.NuevaDescripcion)
        
        self.banyosRepository.session.commit()
        
        return command
        
    def ModificarPrecio(self,command: ModificarBanyosPrecioCommand):   
        if not self.banyosRepository.Existe(command.Banyo):
            raise Exception(f'El banyo {command.Banyo} no existe')
        
        banyo = self.banyosRepository.Cargar(command.Banyo)
        
        banyo.ModificarPrecio(command.NuevoPrecio)
        
        self.banyosRepository.session.commit()
        
        return command
        
    def Eliminar(self,banyo):   
        if not self.banyosRepository.Existe(banyo):
            raise Exception(f'El banyo {banyo} no existe')
        
        objBanyo = self.banyosRepository.Cargar(banyo)
        
        self.banyosRepository.Eliminar(objBanyo)
        
        self.banyosRepository.session.commit()