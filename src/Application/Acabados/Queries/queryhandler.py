from src.Application.Acabados.Queries.readmodels import ObtenerAcabadoReadModel
from src.Infrastructure.SQLAlchemy.AcabadosRepository import AcabadosRepository

class QueryHandler():
    def __init__(self):
        self.acabadosRepository = AcabadosRepository()
        
    def ObtenerAcabados(self):
        acabados = self.acabadosRepository.CargarTodos()
        
        listAcabadosReadModel = []
        for acabado in acabados:
            acabadosReadModel = ObtenerAcabadoReadModel()
            acabadosReadModel.Acabado = acabado.Acabado
            acabadosReadModel.Descripcion = acabado.Descripcion
            acabadosReadModel.Precio = acabado.Precio
            listAcabadosReadModel.append(acabadosReadModel)
        
        return listAcabadosReadModel
    
    def ObtenerAcabado(self, acabado: str):
        if not self.acabadosRepository.Existe(acabado):
            raise Exception(f"El acabado {acabado} no existe")
        
        objAcabado = self.acabadosRepository.Cargar(acabado)

        acabadoReadModel = ObtenerAcabadoReadModel()
        acabadoReadModel.Acabado = objAcabado.Acabado
        acabadoReadModel.Descripcion = objAcabado.Descripcion
        acabadoReadModel.Precio = objAcabado.Precio
        
        return acabadoReadModel