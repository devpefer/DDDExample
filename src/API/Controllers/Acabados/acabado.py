from fastapi import APIRouter
from src.Application.Acabados import acabado
import src.Application.Acabados.Commands.commands as commands
from src.Application.Acabados.Queries.queryhandler import QueryHandler
from src.Application.Acabados.Commands.commandhandler import CommandHandler


router = APIRouter(
    prefix="/Acabados",
    tags=["Acabados"],
)

#region GET
@router.get("/ObtenerAcabados")
async def ObtenerAcabado():
    queryHandler = QueryHandler()
    return queryHandler.ObtenerAcabados()

@router.get("/ObtenerAcabado/{acabado}")
async def ObtenerAcabado(acabado):
    queryHandler = QueryHandler()
    return queryHandler.ObtenerAcabado(acabado)
#endregion

#region POST
@router.post("/Crear")
async def Crear(acabado: commands.InsertarAcabadoCommand):
    commandHandler = CommandHandler()
    return commandHandler.Crear(acabado)

@router.post("/ModificarDescripcion")
async def ModificarDescripcion(modificarAcabado: commands.ModificarAcabadoDescripcionCommand):
    commandHandler = CommandHandler()
    return commandHandler.ModificarDescripcion(modificarAcabado)

@router.post("/ModificarPrecio")
async def ModificarPrecio(modificarAcabado: commands.ModificarAcabadoPrecioCommand):
    commandHandler = CommandHandler()
    return commandHandler.ModificarPrecio(modificarAcabado)
#endregion

#region DELETE
@router.delete("/Eliminar/{acabado}")
async def Eliminar(acabado):
    commandHandler = CommandHandler()
    return commandHandler.Eliminar(acabado)
#endregion