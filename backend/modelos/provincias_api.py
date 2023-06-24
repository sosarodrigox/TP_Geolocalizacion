from pydantic import BaseModel
from modelos.paises_api import PaisApi  # Lo necesito para

# Modelo para AGREGAR provincias
class ProvinciaSinId(BaseModel):
    nombre: str
    pais_id: int

    class Config:
        orm_mode = True

# Modelo para mostrar lista de provincias, trae Provincia(nombre, id_pais, objetoPais)
class ProvinciaList(ProvinciaSinId):
    pais: PaisApi

# Modelo para mostrar el detalle de UNA Provincia (id, nombre, id_pais)
class ProvinciaApi(ProvinciaSinId):
    id: int
