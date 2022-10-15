from fastapi import APIRouter
from src.Application.Series.Commands.commandhandler import CommandHandler
import src.Application.Series.Commands.commands as commands
from src.Application.Series.Queries.queryhandler import QueryHandler
import src.Application.Series.Queries.querymodel as queries


router = APIRouter(
    prefix="/Series",
    tags=["Series"],
)

#region GET
@router.get("/ObtenerSeries")
async def ObtenerSeries():
    queryHandler = QueryHandler()
    return queryHandler.ObtenerSeries()

@router.get("/ObtenerSerie/{serie}")
async def ObtenerSeries(serie):
    queryHandler = QueryHandler()
    return queryHandler.ObtenerSerie(serie)
#endregion

#region POST
@router.post("/Crear")
async def Crear(peinetaSerie: commands.CrearSerieCommand):
    commandHandler = CommandHandler()
    return commandHandler.Crear(peinetaSerie)
    
@router.post("/ModificarTitulo")
async def ModificarDescripcion(peinetaSerie: commands.ModificarSerieTituloCommand):
    commandHandler = CommandHandler()
    return commandHandler.ModificarTitulo(peinetaSerie)
        
@router.post("/ModificarDescripcion")
async def ModificarDescripcion(peinetaSerie: commands.ModificarSerieDescripcionCommand):
    commandHandler = CommandHandler()
    return commandHandler.ModificarDescripcion(peinetaSerie)

#endregion

#region DELETE
@router.delete("/Eliminar/{serie}")
async def Eliminar(serie):
    commandHandler = CommandHandler()
    return commandHandler.Eliminar(serie)
#endregion