from src.Domain.Tamanyos.tamanyo import Tamanyo
from src.Infrastructure.SQLAlchemy.TamanyosRepository import TamanyosRepository
from src.Application.Tamanyos.Commands.commands import CrearTamanyoCommand

class CommandHandler():
    def __init__(self):
        self.tamanyosRepository = TamanyosRepository()
#region Crear
    def Crear(self,command: CrearTamanyoCommand):
        if self.tamanyosRepository.Existe(command.Tamanyo):
            raise Exception(f'El tamaño {command.Tamanyo} ya existe')
        
        tamanyo = Tamanyo.Crear(self, command)
        
        self.tamanyosRepository.session.add(tamanyo)
        self.tamanyosRepository.session.commit()
        
        return command
#endregion

#region Modificar
#endregion

#region Eliminar        
    def Eliminar(self,tamanyoId: str):
        if not self.tamanyosRepository.Existe(tamanyoId):
            raise Exception(f'El tamaño {tamanyoId} no existe')
        
        tamanyo = self.tamanyosRepository.CargarPorId(tamanyoId)
        
        self.tamanyosRepository.Eliminar(tamanyo)
        
        self.tamanyosRepository.session.commit()
#endregion