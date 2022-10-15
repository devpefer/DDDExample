from src.Application.Banyos.Queries.readmodels import ObtenerBanyoReadModel
from src.Infrastructure.SQLAlchemy.BanyosRepository import BanyosRepository

class QueryHandler():
    def __init__(self):
        self.banyosRepository = BanyosRepository()
        
    def ObtenerBanyos(self):
        banyos = self.banyosRepository.CargarTodos()
        
        listBanyosReadModel = []
        for banyo in banyos:
            banyoReadModel = ObtenerBanyoReadModel()
            banyoReadModel.Banyo = banyo.Banyo
            banyoReadModel.Descripcion = banyo.Descripcion
            banyoReadModel.Precio = banyo.Precio
            listBanyosReadModel.append(banyoReadModel)
        
        return listBanyosReadModel
    
    def ObtenerBanyo(self, banyo: str):
        if not self.banyosRepository.Existe(banyo):
            raise Exception(f"El banyo {banyo} no existe")
        
        objBanyo = self.banyosRepository.Cargar(banyo)

        acabadoReadModel = ObtenerBanyoReadModel()
        acabadoReadModel.Banyo = objBanyo.Banyo
        acabadoReadModel.Descripcion = objBanyo.Descripcion
        acabadoReadModel.Precio = objBanyo.Precio
        
        return acabadoReadModel