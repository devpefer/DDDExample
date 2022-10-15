import sys
from os import path
sys.path.append(path.dirname(path.dirname( path.abspath(__file__))))
from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from src.API.Controllers.Referencias import referencia
from src.API.Controllers.Acabados import acabado
from src.API.Controllers.Pedidos import pedido
from src.API.Controllers.Clientes import cliente
from src.API.Controllers.Series import serie
from src.API.Controllers.Tamanyos import tamanyo
from src.API.Controllers.Descuentos import descuento
from src.API.Controllers.Banyos import banyo
from src.API.Controllers.Fotos import foto

app = FastAPI()
app.include_router(acabado.router)
app.include_router(banyo.router)
app.include_router(cliente.router)
app.include_router(descuento.router)
app.include_router(pedido.router)
app.include_router(referencia.router)
app.include_router(serie.router)
app.include_router(tamanyo.router)
app.include_router(foto.router)
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_methods=["*"],
                   allow_headers=["*"])
print(f"main.py with :{app}")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="debug", debug=True)