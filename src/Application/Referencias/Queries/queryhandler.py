from src.Infrastructure.SQLAlchemy.ReferenciasRepository import ReferenciasRepository
from src.Application.Referencias.Queries.querymodel import ObtenerReferenciasQueryModel
from src.Application.Referencias.Queries.readmodel import ObtenerReferenciasReadModel
from src.Infrastructure.SQLAlchemy.SeriesRepository import SeriesRepository
from src.Infrastructure.SQLAlchemy.TamanyosRepository import TamanyosRepository

class QueryHandler():
    def __init__(self):
        self.referenciasRepository = ReferenciasRepository()
        self.seriesRepository = SeriesRepository()
        self.tamanyosRepository = TamanyosRepository()
        
    def ObtenerReferencias(self): 
        referencias = self.referenciasRepository.CargarTodas()
        
        listReferencias = []
        for referencia in referencias:
            tmpRef = ObtenerReferenciasReadModel(referencia.Serie,referencia.Tamanyo,referencia.Referencia,referencia.Precio)
            listReferencias.append(tmpRef)
        
        return listReferencias
    
    def ObtenerReferencia(self,referencia):
        if not self.referenciasRepository.Existe(referencia):
            raise Exception(f"La referencia {referencia} no existe")
         
        objReferencia = self.referenciasRepository.Cargar(referencia)
        referenciaReadModel = ObtenerReferenciasReadModel(objReferencia.Serie,objReferencia.Tamanyo,objReferencia.Referencia,objReferencia.Precio)
        
        return referenciaReadModel
    
    def ObtenerReferenciasPorSerie(self, serie: str):
        if not self.seriesRepository.Existe(serie):
            raise Exception(f"La serie {serie} no existe")
        
        referencias = self.referenciasRepository.CargarPorSerie(serie)
        
        listReferenciasReadModel = []
        for referencia in referencias:
            referenciaReadModel = ObtenerReferenciasReadModel(referencia.Serie,referencia.Tamanyo,referencia.Referencia,referencia.Precio)
            listReferenciasReadModel.append(referenciaReadModel)
        
        return listReferenciasReadModel
    
    def ObtenerReferenciasPorTamanyo(self, tamanyo: str):
        if not self.tamanyosRepository.Existe(tamanyo):
            raise Exception(f"El tamaño {tamanyo} no existe")
        
        referencias = self.referenciasRepository.CargarPorTamanyo(tamanyo)
        
        listReferenciasReadModel = []
        for referencia in referencias:
            referenciaReadModel = ObtenerReferenciasReadModel(referencia.Serie,referencia.Tamanyo,referencia.Referencia,referencia.Precio)
            listReferenciasReadModel.append(referenciaReadModel)
        
        return listReferenciasReadModel
    
    def ObtenerReferenciasPorSerieYTamanyo(self, serie: str, tamanyo: str):
        if not self.seriesRepository.Existe(serie):
            raise Exception(f"La serie {serie} no existe")
        
        if not self.tamanyosRepository.Existe(tamanyo):
            raise Exception(f"El tamaño {tamanyo} no existe")
        
        referencias = self.referenciasRepository.CargarPorSerieYTamanyo(serie,tamanyo)
        
        listReferenciasReadModel = []
        for referencia in referencias:
            referenciaReadModel = ObtenerReferenciasReadModel(referencia.Serie,referencia.Tamanyo,referencia.Referencia,referencia.Precio)
            listReferenciasReadModel.append(referenciaReadModel)
        
        return listReferenciasReadModel