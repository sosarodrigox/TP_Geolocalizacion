from fastapi import APIRouter, Depends, HTTPException
from modelos.localidades_api import LocalidadSinId
from modelos.localidades_api import LocalidadDetalle
from modelos.localidades_api import LocalidadLista
from database import get_db
from repos.localidades_repo import LocalidadesRepositorio
# Esta capa que es la de acceso a endpoints no debería tener NADA DE SQL Alchemy
# ya que esa librería solo tiene que estar en la de acceso a las BBDD, esta capa
# no debería tener ninguna relación con el ORM, por si en el futuro cambio de librería.
# from sqlalchemy.orm import Session

localidades_api = APIRouter(prefix='/localidades', tags=['Localidades'])
repo = LocalidadesRepositorio()


# Pido que devuelva una lista!
@localidades_api.get('', response_model=list[LocalidadLista])
def get_all(db=Depends(get_db)):  # Inyección de dependencias
    result = repo.get_all(db)
    return repo.get_all(db)


@localidades_api.get('/{id}', response_model=LocalidadDetalle)
def get_by_id(id: int, db=Depends(get_db)):
    result = repo.get_by_id(db, id)
    if result is None:
        raise HTTPException(status_code=404, detail='Localidad no encontrada')
    return result


@localidades_api.post('', response_model=LocalidadDetalle, status_code=201)
def new(datos: LocalidadSinId, db=Depends(get_db)):
    try:
        result = repo.agregar(db, datos)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return result


@localidades_api.put('/{id}', response_model=LocalidadDetalle)
def modify(id: int, datos: LocalidadSinId, db=Depends(get_db)):
    result = repo.modificar(db, id, datos)
    if result is None:
        raise HTTPException(status_code=404, detail='Localidad no encontrada')
    return result


@localidades_api.delete('/{id}', status_code=204)
def borrar(id: int, db=Depends(get_db)):
    result = repo.borrar(db, id)
    if result is None:
        raise HTTPException(status_code=404, detail='Localidad no encontrada')
    return
