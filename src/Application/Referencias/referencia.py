from Infrastructure.SQLConnection import ExecuteStoredProcedureCommand, ExecuteStoredProcedureQuery

#region Obtener
def ObtenerPeinetasQuery():
    return ExecuteStoredProcedureQuery('getPeinetas')

def ObtenerPeinetasPorModeloQuery(args: list):
    return ExecuteStoredProcedureQuery('getPeinetasByModelo',args)

def ObtenerPeinetasPorTamanyoQuery(args: list):
    return ExecuteStoredProcedureQuery('getPeinetasByTamanyo',args)

def ObtenerPeinetasPorModeloYTamanyoQuery(args: list):
    return ExecuteStoredProcedureQuery('getPeinetasByModeloYTamanyo',args)

def ObtenerPeinetasTamanyosQuery():
    return ExecuteStoredProcedureQuery('getPeinetasTamanyos')
#endregion

#region Insertar
def InsertarPeinetaModeloCommand(args: tuple):
    return ExecuteStoredProcedureCommand('insertarPeinetaModelo',args)

def InsertarPeinetaReferenciaCommand(args: tuple):
    return ExecuteStoredProcedureCommand('insertarPeinetaReferencia',args)
#endregion

#region Actualizar
def ModificarPeinetaReferenciaCommand(args: tuple):
    return ExecuteStoredProcedureCommand('updatePeinetaReferencia',args)
#endregion

#region Eliminar
def EliminarPeinetaReferenciaCommand(args: tuple):
    return ExecuteStoredProcedureCommand('eliminarPeinetaReferencia',args)
#endregion