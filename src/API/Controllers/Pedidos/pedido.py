from fastapi import APIRouter
from src.Application.Pedidos.Commands.commandhandler import CommandHandler
import src.Application.Pedidos.Commands.commands as commands
from src.Application.Pedidos.Queries.queryhandler import QueryHandler


router = APIRouter(
    prefix="/Pedidos",
    tags=["Pedidos"],
)

#region GET
@router.get("/ObtenerPedidos")
async def ObtenerPedidos():
    queryHandler = QueryHandler()
    return queryHandler.ObtenerPedidos()

@router.get("/ObtenerPedido/{pedido}")
async def ObtenerPedido(pedido):
    queryHandler = QueryHandler()
    return queryHandler.ObtenerPedido(pedido)

@router.get("/ObtenerUltimoCodigoPedido")
async def ObtenerUltimoCodigoPedido():
    queryHandler = QueryHandler()
    return queryHandler.ObtenerUltimoCodigoPedido()
#endregion

#region POST
@router.post("/CrearCabecera")
async def CrearCabecera(cabecera: commands.CrearCabeceraCommand):
    commandHandler = CommandHandler()
    return commandHandler.CrearCabecera(cabecera)

@router.post("/CrearLinea")
async def CrearLinea(linea: commands.CrearLineaCommand):
    commandHandler = CommandHandler()
    return commandHandler.CrearLinea(linea)
#endregion

#region DELETE
@router.delete("/Eliminar/{pedido}")
async def Eliminar(pedido):
    commandHandler = CommandHandler()
    return commandHandler.Eliminar(pedido)
#endregion