from src.Domain.Descuentos.descuento import Descuento
from src.Infrastructure.SQLAlchemy.DescuentosRepository import DescuentosRepository
from src.Application.Descuentos.Commands.commands import InsertarDescuentoCommand, ModificarDescuentoDescripcionCommand, ModificarDescuentoPrecioCommand

class CommandHandler():
    def __init__(self):
        self.descuentosRepository = DescuentosRepository()
        
    def Crear(self,command: InsertarDescuentoCommand):
        if self.descuentosRepository.Existe(command.Descuento):
            raise Exception(f'El acabado {command.Descuento} ya existe')
        
        descuento = Descuento.Crear(command)
        
        self.descuentosRepository.session.add(descuento)
        self.descuentosRepository.session.commit()
        
        return command
        
    def ModificarDescripcion(self,command: ModificarDescuentoDescripcionCommand):   
        if not self.descuentosRepository.Existe(command.Descuento):
            raise Exception(f'El descuento {command.Descuento} no existe')
        
        descuento = self.descuentosRepository.Cargar(command.Acabado)
        
        descuento.ModificarDescripcion(command.NuevaDescripcion)
        
        self.descuentosRepository.session.commit()
        
        return command
        
    def ModificarPrecio(self,command: ModificarDescuentoPrecioCommand):   
        if not self.descuentosRepository.Existe(command.Descuento):
            raise Exception(f'El descuento {command.Descuento} no existe')
        
        descuento = self.descuentosRepository.Cargar(command.Descuento)
        
        descuento.ModificarPrecio(command.NuevoPrecio)
        
        self.descuentosRepository.session.commit()
        
        return command
        
    def Eliminar(self,descuento):   
        if not self.descuentosRepository.Existe(descuento):
            raise Exception(f'El acabado {descuento} no existe')
        
        objDescuento = self.descuentosRepository.Cargar(descuento)
        
        self.descuentosRepository.Eliminar(objDescuento)
        
        self.descuentosRepository.session.commit()