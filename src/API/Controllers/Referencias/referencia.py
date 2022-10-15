from fastapi import APIRouter
from src.Application.Referencias.Commands.commandhandler import CommandHandler
import src.Application.Referencias.Commands.commands as commands
from src.Application.Referencias.Queries.queryhandler import QueryHandler
import src.Application.Referencias.Queries.querymodel as queries

router = APIRouter(
    prefix="/Referencias",
    tags=["Referencias"],
)

#region GET
@router.get("/ObtenerReferencias")
async def ObtenerReferencias():
    queryHandler = QueryHandler()
    return queryHandler.ObtenerReferencias()

@router.get("/ObtenerReferencia/{referencia}")
async def ObtenerReferencias(referencia):
    queryHandler = QueryHandler()
    return queryHandler.ObtenerReferencia(referencia)

@router.get("/ObtenerReferenciasPorSerie/{serie}")
async def ObtenerReferenciasPorId(serie):
    queryHandler = QueryHandler()
    return queryHandler.ObtenerReferenciasPorSerie(serie)

@router.get("/ObtenerReferenciasPorTamanyo/{tamanyo}")
async def ObtenerReferenciasPorTamanyo(tamanyo):
    queryHandler = QueryHandler()
    return queryHandler.ObtenerReferenciasPorTamanyo(tamanyo)

@router.get("/ObtenerReferenciasPorSerieYTamanyo/{serie}/{tamanyo}")
async def ObtenerReferenciasPorSerieYTamanyo(serie, tamanyo):
    queryHandler = QueryHandler()
    return queryHandler.ObtenerReferenciasPorSerieYTamanyo(serie, tamanyo)
#endregion

#region POST
@router.post("/Crear")
async def Crear(peinetaReferencia: commands.CrearReferenciaCommand):
    commandHandler = CommandHandler()
    return commandHandler.Crear(peinetaReferencia)
    
@router.post("/ModificarPrecio")
async def ModificarPrecio(modificarPrecio: commands.ModificarReferenciaPrecioCommand):
    commandHandler = CommandHandler()
    return commandHandler.ModificarPrecio(modificarPrecio)
#endregion

#region DELETE
@router.delete("/Eliminar/{referencia}")
async def Eliminar(referencia):
    commandHandler = CommandHandler()
    return commandHandler.Eliminar(referencia)
#endregion