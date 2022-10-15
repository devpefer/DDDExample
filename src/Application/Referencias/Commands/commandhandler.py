from src.Domain.Referencias.referencia import Referencia
from src.Infrastructure.SQLAlchemy.ReferenciasRepository import ReferenciasRepository
from src.Application.Referencias.Commands.commands import CrearReferenciaCommand, ModificarReferenciaPrecioCommand

class CommandHandler():
    def __init__(self):
        self.referenciasRepository = ReferenciasRepository()
#region Crear
    def Crear(self,command: CrearReferenciaCommand):
        if self.referenciasRepository.Existe(command.Referencia):
            raise Exception(f'El modelo {command.Serie} con tamaño {command.Tamanyo} ya existe')
        
        referencia = Referencia.Crear(self,command)
        
        self.referenciasRepository.session.add(referencia)
        self.referenciasRepository.session.commit()
        
        return command
#endregion

#region Modificar
    def ModificarPrecio(self,command: ModificarReferenciaPrecioCommand):        
        if not self.referenciasRepository.Existe(command.Referencia):
            raise Exception(f'La referencia {command.Referencia} no existe')
        
        referencia = self.referenciasRepository.Cargar(command.Referencia)
        
        referencia.ModificarPrecio(referencia, command.Precio)
        
        self.referenciasRepository.session.commit()
        
        return command
#endregion

#region Eliminar        
    def Eliminar(self,referencia: str):
        if not self.referenciasRepository.Existe(referencia):
            raise Exception(f'La referencia {referencia} no existe')
        
        referencia = self.referenciasRepository.Cargar(referencia)
        
        self.referenciasRepository.Eliminar(referencia)
        
        self.referenciasRepository.session.commit()
#endregion