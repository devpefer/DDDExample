from fastapi import APIRouter
from src.Application.Clientes import cliente
from src.Application.Clientes.Commands.commandhandler import CommandHandler
import src.Application.Clientes.Commands.commands as commands
from src.Application.Clientes.Queries.queryhandler import QueryHandler

router = APIRouter(
    prefix="/Clientes",
    tags=["Clientes"],
)

#region GET
@router.get("/ObtenerClientes")
async def ObtenerClientes():
    queryHandler = QueryHandler()
    return queryHandler.ObtenerClientes()

@router.get("/ObtenerClientePorCIF/{cif}")
async def ObtenerClientes(cif):
    queryHandler = QueryHandler()
    return queryHandler.ObtenerCliente(cif)

@router.get("/ObtenerClienteCIF/{razonSocial}")
async def ObtenerClienteCIF(razonSocial):
    queryHandler = QueryHandler()
    return queryHandler.ObtenerClienteCIF(razonSocial)
#endregion

#region POST
@router.post("/Insertar")
async def Insertar(cliente: commands.InsertarClienteCommand):
    commandHandler = CommandHandler()
    return commandHandler.Crear(cliente)

@router.post("/ModificarRazonSocial")
async def ModificarRazonSocial(modificarCliente: commands.ModificarClienteRazonSocialCommand):
    commandHandler = CommandHandler()
    return commandHandler.ModificarRazonSocial(modificarCliente)

@router.post("/ModificarDireccion")
async def ModificarDireccion(modificarCliente: commands.ModificarClienteDireccionCommand):
    commandHandler = CommandHandler()
    return commandHandler.ModificarDireccion(modificarCliente)

@router.post("/ModificarTelefono")
async def ModificarTelefono(modificarCliente: commands.ModificarClienteTelefonoCommand):
    commandHandler = CommandHandler()
    return commandHandler.ModificarTelefono(modificarCliente)

@router.post("/ModificarTelefonoMovil")
async def ModificarTelefonoMovil(modificarCliente: commands.ModificarClienteTelefonoMovilCommand):
    commandHandler = CommandHandler()
    return commandHandler.ModificarTelefonoMovil(modificarCliente)

@router.post("/ModificarCuentaBancaria")
async def ModificarCuentaBancaria(modificarCliente: commands.ModificarClienteCuentaBancariaCommand):
    commandHandler = CommandHandler()
    return commandHandler.ModificarCuentaBancaria(modificarCliente)

@router.post("/ModificarCorreoElectronico")
async def ModificarCorreoElectronico(modificarCliente: commands.ModificarClienteCorreoElectronicoCommand):
    commandHandler = CommandHandler()
    return commandHandler.ModificarCorreoElectronico(modificarCliente)
#endregion

#region DELETE
@router.delete("/Eliminar/{cif}")
async def Eliminar(cif):
    commandHandler = CommandHandler()
    return commandHandler.Eliminar(cif)
#endregion