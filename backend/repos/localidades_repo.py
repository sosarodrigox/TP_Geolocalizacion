from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from modelos.localidades_api import LocalidadSinId
from modelos.provincias_bd import ProvinciaBd
from modelos.localidades_bd import LocalidadBd
from sqlalchemy.orm import Session


class LocalidadesRepositorio():

    def get_all(self, db: Session):
        # return [
        #     LocalidadBd(id=1, nombre='Localidad1'), #Hardcode para probar
        #     LocalidadBd(id=2, nombre='Localidad2'),
        # ]

        # INNER JOIN:return db.execute(select(LocalidadBd).join(ProvinciaBd)).scalars().all()

        # LEFT OUTER JOIN: Le pedimos que haga un JOIN entre localidad y provincia (Traeme todos los datos de (TablaPrincipal)localidades y (TablaSecundaria)provincias) y
        # hacé un left outer join con provincias. Podría hacer otro outer join con paises para que lo muestre. (El modelo de response (api) tiene que contener esos datos que pido)
        # https://stackoverflow.com/questions/39619353/how-to-perform-a-left-join-in-sqlalchemy
        return db.execute(select(LocalidadBd, ProvinciaBd).join(ProvinciaBd, isouter=True)).scalars().all()

    def get_by_id(self, db: Session, id: int):
        result = db.execute(select(LocalidadBd).where(
            LocalidadBd.id == id)).scalar()
        return result

    def agregar(self, db: Session, datos: LocalidadSinId):
        # pydantic ofrece el método .dict() que devuelve todoslos atributos de esa instancia como un diccionario
        # en formato clave=valor, y el ** significa que pasa x todos los elementos del diccionario uno por uno
        # y se lo asigna a los valores de esta instancia.
        # LocalidadBd(**datos.disct())) es equivalente a:
        # LocalidadBd(nombre=datos.nombre, caracteristica_telefononica = datos.caracteristica_telefonica, provincia_id = datos.provincia_id)
        nueva_entidad_bd: LocalidadBd = LocalidadBd(**datos.dict())
        try:
            db.add(nueva_entidad_bd)
            db.commit()
            # El error de integridad es cuando el id de provincia que agrego no existe en la tabla.
        except IntegrityError.exc.IntegrityError as e:
            raise RuntimeError(f'Error al agregar una provincia: {e}')
        return nueva_entidad_bd

    def modificar(self, db: Session, id: int, datos: LocalidadSinId):
        # Orimero busco los datos que ya tengo en la BBDD y quiero modificar
        entidad: LocalidadBd = self.get_by_id(db, id)
        if entidad is None:
            return None
        # Me fijo todos los datos que traigo para cambiar, paso x todos los atributos de esa instancia
        # por cada uno de esos valores tengo que asignarselo a la entidad que tengo en la bbdd,

        # entonces el bucle for siguiente es equivalente a estas tres lineas:
        # entidad.nombre = datos.nombre
        # entidad.caracteristica_telefonica = datos.caracteristica_telefonica
        # entidad.provincia_id = datos.provincia_id

        for k, v in datos.dict(exclude_unset=True).items():
            # exclude_unset = excluye los datos que no se pasan, paso los atributos que fueron asignados solamente
            # setattr = Le dice que tome esta instancia de la clase y le asigne al atributo k, el valor que está en la variable v. (Que son los items del diccionario)
            setattr(entidad, k, v)

        db.commit()
        return entidad

    def borrar(self, db: Session, id: int):
        entidad: LocalidadBd = self.get_by_id(db, id)
        if entidad is None:
            return None
        db.delete(entidad)
        db.commit()
        return entidad
