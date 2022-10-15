from fastapi import APIRouter
import src.Application.Banyos.Commands.commands as commands
from src.Application.Banyos.Queries.queryhandler import QueryHandler
from src.Application.Banyos.Commands.commandhandler import CommandHandler


router = APIRouter(
    prefix="/Banyos",
    tags=["Baños"],
)

#region GET
@router.get("/ObtenerBanyos")
async def ObtenerBanyos():
    queryHandler = QueryHandler()
    return queryHandler.ObtenerBanyos()

@router.get("/ObtenerBanyo/{banyo}")
async def ObtenerBanyo(banyo):
    queryHandler = QueryHandler()
    return queryHandler.ObtenerBanyo(banyo)
#endregion

#region POST
@router.post("/Crear")
async def Crear(banyo: commands.InsertarBanyosCommand):
    commandHandler = CommandHandler()
    return commandHandler.Crear(banyo)

@router.post("/ModificarDescripcion")
async def ModificarDescripcion(modificarBanyo: commands.ModificarBanyosDescripcionCommand):
    commandHandler = CommandHandler()
    return commandHandler.ModificarDescripcion(modificarBanyo)

@router.post("/ModificarPrecio")
async def ModificarPrecio(modificarBanyo: commands.ModificarBanyosPrecioCommand):
    commandHandler = CommandHandler()
    return commandHandler.ModificarPrecio(modificarBanyo)
#endregion

#region DELETE
@router.delete("/Eliminar/{banyo}")
async def Eliminar(banyo):
    commandHandler = CommandHandler()
    return commandHandler.Eliminar(banyo)
#endregion