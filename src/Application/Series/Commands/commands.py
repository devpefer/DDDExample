from decimal import Decimal
from pydantic import BaseModel

class CrearSerieCommand(BaseModel):
    Serie: str
    Titulo: str
    Descripcion: str
    
class ModificarSerieTituloCommand(BaseModel):
    Serie: str
    Titulo: str
    
class ModificarSerieDescripcionCommand(BaseModel):
    Serie: str
    Descripcion: str