from sqlalchemy.orm import relationship  # Sirve para traer objetos
from sqlalchemy import Column, ForeignKey, Integer, String
from database import BaseBd


class LocalidadBd(BaseBd):
    __tablename__ = 'localidades'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(80), nullable=False)
    caracteristica_telefonica = Column(Integer, nullable=True)
    provincia_id = Column(Integer, ForeignKey(
        'provincias.id'))  # 'nombre_tabla.id'

    provincia = relationship('ProvinciaBd')
