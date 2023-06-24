# Este es el modelo de FastAPI (pydantic)
from pydantic import BaseModel


class PaisSinId(BaseModel):
    nombre: str

    class Config:  # Sin esta clase interna genera error con las BD!
        orm_mode = True


class PaisApi(PaisSinId):
    id: int
    # Como en este caso PaisApi hereda de PaisSinId que ya tiene la clase interna Config, no es necesario volver a colocarla acá.
    # Pero en caso de que no herede se la agrega dentro de la clase para que no de error.
