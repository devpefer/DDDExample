from src.Application.Descuentos.Queries.readmodels import ObtenerDescuentoReadModel
from src.Infrastructure.SQLAlchemy.DescuentosRepository import DescuentosRepository

class QueryHandler():
    def __init__(self):
        self.descuentosRepository = DescuentosRepository()
        
    def ObtenerDescuentos(self):
        descuentos = self.descuentosRepository.CargarTodos()
        
        listDescuentosReadModel = []
        for descuento in descuentos:
            descuentosReadModel = ObtenerDescuentoReadModel()
            descuentosReadModel.Descuento = descuento.Descuento
            descuentosReadModel.Descripcion = descuento.Descripcion
            descuentosReadModel.Precio = descuento.Precio
            listDescuentosReadModel.append(descuentosReadModel)
        
        return listDescuentosReadModel
    
    def ObtenerDescuento(self, descuento: str):
        if not self.descuentosRepository.Existe(descuento):
            raise Exception(f"El descuento {descuento} no existe")
        
        objDescuento = self.descuentosRepository.Cargar(descuento)

        descuentoReadModel = ObtenerDescuentoReadModel()
        descuentoReadModel.Descuento = objDescuento.Descuento
        descuentoReadModel.Descripcion = objDescuento.Descripcion
        descuentoReadModel.Precio = objDescuento.Precio
        
        return descuentoReadModel