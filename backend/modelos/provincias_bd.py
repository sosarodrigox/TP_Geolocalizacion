from sqlalchemy.orm import relationship  # Sirve para traer objetos
from sqlalchemy import Column, ForeignKey, Integer, String
from database import BaseBd
from modelos.paises_bd import PaisBd


class ProvinciaBd(BaseBd):
    __tablename__ = 'provincias'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(80), nullable=False)
    # Colocamos el campo que hace la relación como FK: ForeignKey('nombre_tabla_en_bd'.'nombre_columna_en_bd')
    # Teoría: Tener en cuenta, que el id no es necario que sea un PK, tambien puede ser un "unique"
    pais_id = Column(Integer, ForeignKey('paises.id'))

    # Atributo de Navegación: Es un objeto de tipo PaisBd, es una instancia TEMPORAL completa de la clase PaisBD,
    # Se usa para que SQL Alchemy me traiga el objeto completo de "país", no solo el ID, esto sirve para
    # agilizar y no tener que estar haciedno muchos select, join, etc. Lo puedo llamar y obtener sus atributos.
    # *LAZY LOADING: Recien cuando lo acceda, por ejemplo haciendo "p.pais.nombre", el ORM automaticamente hace un select a la tabla de paises
    # y me lo trae de forma completa. Por ejemplo si muestro una lista de provincias, solo muestra el id de paises, ahora si en esa lista
    # necesito mostrar el nombre del pais, accedo a esta relationship, el orm hace el select a tabla paises y accedo a su nombre.
    pais = relationship('PaisBd')

    # TEORIA: La relación entre paises y provincias es 1 a muchos (1:n)
    # Si por ej. fuera 1:1 = La relación entre pais y provincia, sería lo mismo poner el FK en provincias o en paises
    # En este caso si colocamos el FK en paises, porque restringimos a cada pais a una sola provincia, entonces:
    # EL ID con el FK SIEMPRE se pone del lado del MUCHOS (Provincias en este caso)

    # Caso 1:1 = Paciente -> Historia Clínica
    # Caso n:n = Cursos:Alumnos. Se hace una tabla intermedia que tiene las dos tablas relacionadas. Se plantea una entidad
    # por ejemplo inscripcion y ponemos los dos id, cada id va a tener una FK a la tabla que correspondan y además
    # ambos id van a ser la PK de la tabla inscripción. (Ver apunte SQL Alchemy como el orm arma automaticamente la tabla)
