from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:admin@localhost/LabIV_2023" #Cadena de conexión

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True) #Motor de conexión

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False) 
#sessionmaker es una función que cuando la ejecuto me devuelve una sesión de conexión a la Base de Datos.
#bind: Indica a qué motor de conexión se va a conectar, en este caso engine, #autocommit: significa que las instrucciones que requieran commit se hagan de forma manual o automática, se sugiere False y colocar un bloque try-catch
#Autoflush: Cada tanto, el engine libera las operaciones que tenemos a la BBDD, junta operaciones y cada tanto las carga todas juntas.


BaseBd = declarative_base() #Es la clase base de donde descienden todas las clases que quiero meter en la BBDD.

def get_db():
    db = SessionLocal() #Se crea la conexión a la BBDD – Inyección de dependencias
    try:
        yield db #Devuelve la variable db como si fuera un return, pero espera que se termine de usar la variable, luego continua con las intrucciones, y despues con el finally que cierra la conexión.
    finally:
        db.close() #Cierra la conexión


def create_all(): #Pasa todas las entidades que tenga definida para crear la BBDD
    BaseBd.metadata.create_all(bind=engine)


def drop_all(): #Borra todas las tablas referidas a las entidades definidas en la BBDD
    BaseBd.metadata.drop_all(bind=engine)

    