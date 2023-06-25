from fastapi import APIRouter, Depends, HTTPException
from database import get_db
# from sqlalchemy.orm import Session
from modelos.paises_api import PaisApi, PaisSinId
from repos.paises_repositorio import PaisesRepositorio  # Importamos el repositorio

# En una instancia de APIRouter, con el prefijo /paises indico que todos los endpoint de este archivo van a empezar con /paises y se lo asigno a la isntancia.
paises_api = APIRouter(prefix='/paises', tags=['Paises'])
paises_repo = PaisesRepositorio()  # Creamos una instancia del repositorio


# '' es lo mismo que '/paises'
# Lo transforma en la respuesta en PaisApi (Ver config)
@paises_api.get('', response_model=list[PaisApi])
# Depends(): Crea la instancia usando la función get_db y cuando termina termina llama al db.close()
def get_all(db= Depends(get_db)):
    # tags sirve para hacer comentarios en los enpoint y las funciones:
    '''
    Este es un comentario de la funcion (Devuelve una lista de todos los paises)
    '''
    result = paises_repo.get_all(db)
    return result


@paises_api.get('/{id}', response_model=PaisApi)
def get_by_id(id: int, db = Depends(get_db)):
    result = paises_repo.get_by_id(db, id)
    # Si no lo encuentra marca un error y un status code
    if result is None:
        raise HTTPException(status_code=404, detail='Pais no encontrado')

    return result


# Devuelve el obj nuevo creado y un cod 201
@paises_api.post('', response_model=PaisApi, status_code=201)
# Resive el JSON con los datos del nuevo pais (Sin ID) y la session.
def nuevo(datos: PaisSinId, db = Depends(get_db)):
    # Utiliza la función agregar del repositorio, pasandole la session y los datos que tiene que agregar
    result = paises_repo.agregar(db, datos)
    # Nos devuelve el nuevo paisBD que devuelve el repo y cuando hace el return lo cambia a paisAPI por el response.
    return result


@paises_api.put('/{id}', response_model=PaisApi)
def modificar(id: int, datos: PaisSinId, db = Depends(get_db)):
    # Creamos la función modoficar en el repo.
    result = paises_repo.modificar(db, id, datos)
    # Opcion si NO lo encontró
    if result is None:
        raise HTTPException(status_code=404, detail='Pais no encontrado')
    # Opcion si lo encontró
    return result


# 204: Significa que no está devolviendo nada pero que está todo OK.
@paises_api.delete('/{id}', status_code=204)
def borrar(id: int, db = Depends(get_db)):
    result = paises_repo.borrar(db, id)
    if result is None:
        raise HTTPException(status_code=404, detail='Pais no encontrado')
    return  # No devuelve nada.
