from src.Application.Series.Queries.readmodel import ObtenerSeriesReadModel
from src.Infrastructure.SQLAlchemy.SeriesRepository import SeriesRepository

class QueryHandler():
    def __init__(self):
        self.seriesRepository = SeriesRepository()
        
    def ObtenerSeries(self):
        series = self.seriesRepository.CargarTodas()
        
        listSeriesReadModel = []
        for serie in series:
            serieReadModel = ObtenerSeriesReadModel()
            serieReadModel.Serie = serie.Serie
            serieReadModel.Titulo = serie.Titulo
            serieReadModel.Descripcion = serie.Descripcion
            listSeriesReadModel.append(serieReadModel)
        
        return listSeriesReadModel
    
    def ObtenerSerie(self, serie: str):
        if not self.seriesRepository.Existe(serie):
            raise Exception(f"La serie {serie} no existe")
        
        objSerie = self.seriesRepository.Cargar(serie)

        serieReadModel = ObtenerSeriesReadModel()
        serieReadModel.Serie = objSerie.Serie
        serieReadModel.Titulo = objSerie.Titulo
        serieReadModel.Descripcion = objSerie.Descripcion
        
        return serieReadModel