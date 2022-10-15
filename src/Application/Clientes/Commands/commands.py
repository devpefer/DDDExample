from pydantic import BaseModel

class InsertarClienteCommand(BaseModel):
    CIF: str
    RazonSocial: str
    Direccion: str
    Telefono: str
    TelefonoMovil: str
    CuentaBancaria: str
    CorreoElectronico: str
    
class ModificarClienteRazonSocialCommand(BaseModel):
    CIF: str
    NuevaRazonSocial: str
    
class ModificarClienteDireccionCommand(BaseModel):
    CIF: str
    NuevaDireccion: str
    
class ModificarClienteTelefonoCommand(BaseModel):
    CIF: str
    NuevoTelefono: str
    
class ModificarClienteTelefonoMovilCommand(BaseModel):
    CIF: str
    NuevoTelefonoMovil: str
    
class ModificarClienteCuentaBancariaCommand(BaseModel):
    CIF: str
    NuevaCuentaBancaria: str
    
class ModificarClienteCorreoElectronicoCommand(BaseModel):
    CIF: str
    NuevoCorreoElectronico: str