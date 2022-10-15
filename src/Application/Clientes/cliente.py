from src.Infrastructure.SQLConnection import ExecuteStoredProcedureCommand, ExecuteStoredProcedureQuery

#region Obtener
def ObtenerClientesQuery():
    return ExecuteStoredProcedureQuery('getClientes')

def ObtenerClientePorIdQuery(args: list):
    return ExecuteStoredProcedureQuery('getClienteById',args)
#endregion

#region Insertar
def InsertarClienteCommand(args: tuple):
    return ExecuteStoredProcedureCommand('insertarCliente',args)
#endregion

#region Actualizar
def ModificarClienteCommand(args: tuple):
    return ExecuteStoredProcedureCommand('updateCliente',args)
#endregion

#region Eliminar
def EliminarClienteCommand(args: tuple):
    return ExecuteStoredProcedureCommand('deleteCliente',args)
#endregion