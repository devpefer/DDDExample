from fastapi import APIRouter
from src.Application.Tamanyos.Commands.commandhandler import CommandHandler
import src.Application.Tamanyos.Commands.commands as commands
from src.Application.Tamanyos.Queries.queryhandler import QueryHandler
import src.Application.Tamanyos.Queries.querymodel as queries

router = APIRouter(
    prefix="/Tamanyos",
    tags=["Tamaños"],
)

#region GET
@router.get("/ObtenerTamanyos")
async def ObtenerTamanyos():
    queryHandler = QueryHandler()
    return queryHandler.ObtenerTamanyos()
#endregion

#region POST
@router.post("/Crear")
async def Crear(peinetaTamanyo: commands.CrearTamanyoCommand):
    commandHandler = CommandHandler()
    return commandHandler.Crear(peinetaTamanyo)
#endregion

#region DELETE
@router.delete("/Eliminar/{tamanyo}")
async def Eliminar(tamanyo):
    commandHandler = CommandHandler()
    return commandHandler.Eliminar(tamanyo)
#endregion