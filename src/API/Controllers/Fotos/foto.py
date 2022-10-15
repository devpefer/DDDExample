from fastapi import APIRouter
from fastapi.responses import FileResponse
router = APIRouter(
    prefix="/Fotos",
    tags=["Fotos"],
)

#region GET
@router.get("/ObtenerFoto/{modelo}")
async def ObtenerFoto(modelo: str):
    return FileResponse(f'/home/pi/Documents/res/images/{modelo}.jpg')
#endregion