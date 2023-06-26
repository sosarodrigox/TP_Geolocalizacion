import uvicorn  # Importo uvicorn
from fastapi import FastAPI  # Importo FastAPI
from api.paises_api import paises_api  # Importamos paises api
from api.provincias_api import provincias_api
from api.localidades_api import localidades_api
import database  # Importamos el archivo de conexión a la BBDD
# Importamos los modelos de BBDD (POR MAS QUE NO SE USE, EN NECESARIO PARA QUE CREE LA TABLA EN LA BBDD)
import modelos.paises_bd
# Importamos el modelo para que database.create_all() cree la tabla
import modelos.provincias_bd
# Importamos el modelo para que database.create_all() cree la tabla
import modelos.localidades_bd

from fastapi.middleware.cors import CORSMiddleware  # Para solucionar error de CORS

# Crea los modelos de la BBDD, si ya existen no los vuelve a crear.
database.create_all()

app = FastAPI()  # Creo una instancia de FastAPI
# Pedimos que incluya las rutas (endpoints) definidas en el archivo "paises_api"
app.include_router(paises_api)
# NO OLVIDARSE DE IMPORTAR EL ROUTER O NO SE CARGAN LOS ENDPOINTS!!!
app.include_router(provincias_api)
app.include_router(localidades_api)

# Para solucionar erros de CORS POLICY - Valores de Midleware:
# https://fastapi.tiangolo.com/tutorial/cors/
# Importar: from fastapi.middleware.cors import CORSMiddleware
# LUEGO AGREGAR:
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':  # inicializo FastAPI
    uvicorn.run('geolocacion:app', host='127.0.0.1', port=8000, reload=True)
