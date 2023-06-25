from pydantic import BaseModel
from modelos.provincias_api import ProvinciaApi

# Modelo para AGREGAR localidades


class LocalidadSinId(BaseModel):
    nombre: str
    caracteristica_telefonica: int
    # Con = None se vuelve opcional, esto es para que no de error cuando trae la lista de localidades
    provincia_id: int = None

    class Config:
        orm_mode = True


class LocalidadLista(BaseModel):
    nombre: str
    caracteristica_telefonica: int
    # Con = None se vuelve opcional, esto es para que no de error cuando trae la lista de localidades
    provincia: ProvinciaApi = None
    # Se crea la clase de nuevo porque ya no hereda de BaseModel

    class Config:
        orm_mode = True


class LocalidadDetalle(LocalidadSinId):
    id: int
