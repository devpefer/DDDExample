from src.Infrastructure.SQLAlchemy.TamanyosRepository import TamanyosRepository
from src.Application.Tamanyos.Queries.querymodel import ObtenerTamanyosQueryModel
from src.Application.Tamanyos.Queries.readmodel import ObtenerTamanyosReadModel

class QueryHandler():
    def __init__(self):
        self.tamanyosRepository = TamanyosRepository()
        
    def ObtenerTamanyos(self): 
        tamanyos = self.tamanyosRepository.CargarTodos()
        
        listTamanyos = []
        for tamanyo in tamanyos:
            tmpTamanyo = ObtenerTamanyosReadModel(tamanyo.Tamanyo)
            listTamanyos.append(tmpTamanyo)
        
        return listTamanyos