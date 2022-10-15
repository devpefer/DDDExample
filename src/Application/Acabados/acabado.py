from src.Infrastructure.SQLConnection import ExecuteStoredProcedureCommand, ExecuteStoredProcedureQuery

#region Obtener
def ObtenerAcabadosQuery():
    return ExecuteStoredProcedureQuery('getAcabados')
#endregion

#region Insertar
def InsertarAcabadoCommand(args: tuple):
    return ExecuteStoredProcedureCommand('insertarAcabado',args)
#endregion

#region Modificar
def ModificarAcabadoCommand(args: tuple):
    return ExecuteStoredProcedureCommand('updateAcabado',args)
#endregion

#region Eliminar
def EliminarAcabadoCommand(args: tuple):
    return ExecuteStoredProcedureCommand('eliminarAcabado',args)
#endregion