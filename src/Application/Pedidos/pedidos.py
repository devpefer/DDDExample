from Infrastructure.SQLConnection import ExecuteStoredProcedureCommand, ExecuteStoredProcedureQuery

#region Obtener
def ObtenerPedidosQuery():
    return ExecuteStoredProcedureQuery('getPedidos')

def ObtenerPedidoPorIdQuery(args: list):
    return ExecuteStoredProcedureQuery('getPedidoById',args)
#endregion

#region Insertar
def InsertarPedidoCabeceraCommand(args: list):
    return ExecuteStoredProcedureCommand('insertarPedidoCabecera',args)
#endregion