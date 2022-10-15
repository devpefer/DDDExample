from src.Domain.Series.serie import Serie
from src.Infrastructure.SQLAlchemy.SeriesRepository import SeriesRepository
from src.Application.Series.Commands.commands import CrearSerieCommand, ModificarSerieTituloCommand, ModificarSerieDescripcionCommand

class CommandHandler():
    def __init__(self):
        self.seriesRepository = SeriesRepository()
        
    def Crear(self,command: CrearSerieCommand):
        if self.seriesRepository.Existe(command.Serie):
            raise Exception(f'La serie {command.Serie} ya existe')
        
        serie = Serie.Crear(self, command)
        
        self.seriesRepository.session.add(serie)
        self.seriesRepository.session.commit()
        
        return command
        
    def ModificarTitulo(self,command: ModificarSerieTituloCommand):   
        if not self.seriesRepository.Existe(command.Serie):
            raise Exception(f'La serie {command.Serie} no existe')
        
        serie = self.seriesRepository.Cargar(command.Serie)
        
        serie.ModificarTitulo(serie, command.Titulo)
        
        self.seriesRepository.session.commit()
        
        return command
        
    def ModificarDescripcion(self,command: ModificarSerieDescripcionCommand):   
        if not self.seriesRepository.Existe(command.Serie):
            raise Exception(f'La serie {command.Serie} no existe')
        
        serie = self.seriesRepository.Cargar(command.Serie)
        
        serie.ModificarDescripcion(command.Descripcion)
        
        self.seriesRepository.session.commit()
        
        return command
        
    def Eliminar(self,serie):   
        if not self.seriesRepository.Existe(serie):
            raise Exception(f'La serie {serie} no existe')
        
        objSerie = self.seriesRepository.Cargar(serie)
        
        self.seriesRepository.Eliminar(objSerie)
        
        self.seriesRepository.session.commit()