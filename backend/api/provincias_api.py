from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from modelos.provincias_api import ProvinciaApi, ProvinciaSinId, ProvinciaList
from repos.provincias_repo import ProvinciasRepositorio

provincias_api = APIRouter(prefix='/provincias', tags=['Provincias'])
provincias_repo = ProvinciasRepositorio()


@provincias_api.get('', response_model=list[ProvinciaList])
def get_all(db: Session = Depends(get_db)):
    result = provincias_repo.get_all(db)
    return result


@provincias_api.get('/{id}', response_model=ProvinciaApi)
def get_by_id(id: int, db: Session = Depends(get_db)):
    result = provincias_repo.get_by_id(db, id)
    if result is None:
        raise HTTPException(status_code=404, detail='Provincia no encontrada')
    return result


@provincias_api.post('', response_model=ProvinciaApi, status_code=201)
def new(datos: ProvinciaSinId, db: Session = Depends(get_db)):
    try:
        result = provincias_repo.agregar(db, datos)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return result


@provincias_api.put('/{id}', response_model=ProvinciaApi)
def modify(id: int, datos: ProvinciaSinId, db: Session = Depends(get_db)):
    result = provincias_repo.modificar(db, id, datos)
    if result is None:
        raise HTTPException(status_code=404, detail='Provincia no encontrada')
    return result


@provincias_api.delete('/{id}', status_code=204)
def borrar(id: int, db: Session = Depends(get_db)):
    result = provincias_repo.borrar(db, id)
    if result is None:
        raise HTTPException(status_code=404, detail='Provincia no encontrada')
    return
