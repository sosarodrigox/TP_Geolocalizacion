from database import BaseBd
from sqlalchemy import Column, Integer, String, ForeignKey

# Crea los modelos de tablas en la BBDD


class PaisBd(BaseBd):  # Definimos los atributos de la tabla (columnas) y nombre de la tabla
    __tablename__ = 'paises'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(80), nullable=False)
