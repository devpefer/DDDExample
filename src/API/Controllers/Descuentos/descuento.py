from fastapi import APIRouter
import src.Application.Descuentos.Commands.commands as commands
from src.Application.Descuentos.Queries.queryhandler import QueryHandler
from src.Application.Descuentos.Commands.commandhandler import CommandHandler


router = APIRouter(
    prefix="/Descuentos",
    tags=["Descuentos"],
)

#region GET
@router.get("/ObtenerDescuentos")
async def ObtenerDescuentos():
    queryHandler = QueryHandler()
    return queryHandler.ObtenerDescuentos()

@router.get("/ObtenerDescuento/{descuento}")
async def ObtenerDescuento(descuento):
    queryHandler = QueryHandler()
    return queryHandler.ObtenerDescuento(descuento)
#endregion

#region POST
@router.post("/Crear")
async def Crear(descuento: commands.InsertarDescuentoCommand):
    commandHandler = CommandHandler()
    return commandHandler.Crear(descuento)

@router.post("/ModificarDescripcion")
async def ModificarDescripcion(modificarCliente: commands.ModificarDescuentoDescripcionCommand):
    commandHandler = CommandHandler()
    return commandHandler.ModificarDescripcion(modificarCliente)

@router.post("/ModificarPrecio")
async def ModificarPrecio(modificarCliente: commands.ModificarDescuentoPrecioCommand):
    commandHandler = CommandHandler()
    return commandHandler.ModificarPrecio(modificarCliente)
#endregion

#region DELETE
@router.delete("/Eliminar/{descuento}")
async def Eliminar(descuento):
    commandHandler = CommandHandler()
    return commandHandler.Eliminar(descuento)
#endregion