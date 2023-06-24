from modelos.paises_bd import PaisBd
from modelos.paises_api import PaisSinId
# Necesitamos la session de la bd para poder conectarnos
from sqlalchemy.orm import Session
from sqlalchemy import select


class PaisesRepositorio():

    # Hardcodeado en una lista de python:
    # def get_all(self):
    #     return[
    #         PaisSinId("Argentina"),
    #         PaisSinId("Brasil")
    #     ]

    # Devuelve las rows de la BBDD  transformadas en objetos paises en una lista de python
    def get_all(self, db: Session):  # Importamos Session y Select
        # Crea la consulta SQL x medio de SQLAlchemy
        return db.execute(select(PaisBd).order_by(PaisBd.nombre.desc())).scalars().all()
        # Para sacar las tuplas de adentro de las rows usamos "scalars()"
        # Con .all() me devuelve todo en una lista.

    def get_by_id(self, db: Session, id: int):
        # Devuelve una lista de objetos ROW, entonces lo convertimos a obj paisBd y devolver con scarlar() (en singular)
        result = db.execute(select(PaisBd).where(PaisBd.id == id)).scalar()
        return result

    def agregar(self, db: Session, datos: PaisSinId):
        # Tengo que crear una instancia de paisBd, para poder usar los metodos de SQLAlchemy, como session, add, etc
        # datos(paisSinId) no me sirve para pasar a la BD, entonces lo transformamos en una nueva entida BD
        nueva_entidad_bd: PaisBd = PaisBd(nombre=datos.nombre)  # Transformo
        db.add(nueva_entidad_bd)  # Agrego a la BD
        db.commit()  # Commiteo y devuelvo.
        return nueva_entidad_bd

    def modificar(self, db: Session, id: int, datos: PaisSinId):
        entidad: PaisBd = self.get_by_id(db, id)
        # Si NO lo encuentra:
        if entidad is None:
            return None
        # Si lo encuentra, actualiza los datos y hace el commit, devuelve entidad.
        entidad.nombre = datos.nombre
        db.commit()
        return entidad

    def borrar(self, db: Session, id: int):
        entidad: PaisBd = self.get_by_id(db, id)
        if entidad is None:
            return None
        db.delete(entidad)
        db.commit()
        return entidad
