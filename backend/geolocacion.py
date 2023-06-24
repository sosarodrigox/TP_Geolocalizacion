import uvicorn  # Importo uvicorn
from fastapi import FastAPI  # Importo FastAPI
from api.paises_api import paises_api  # Importamos paises api
import database  # Importamos el archivo de conexión a la BBDD
import modelos.paises_bd  # Importamos los modelos de BBDD

# Crea los modelos de la BBDD, si ya existen no los vuelve a crear.
database.create_all()

app = FastAPI()  # Creo una instancia de FastAPI
# Pedimos que incluya las rutas (endpoints) definidas en el archivo "paises_api"
app.include_router(paises_api)


if __name__ == '__main__':  # inicializo FastAPI
    uvicorn.run('geolocacion:app', host='127.0.0.1', port=8000, reload=True)