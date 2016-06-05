import json
from sqlalchemy import (create_engine, Column, Integer, String, Date, Time, Float,
                        Text, ForeignKey, func)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from externo.datos import *

base_dir = os.path.dirname((os.path.abspath(__file__)))

with open('{}/config.json'.format(base_dir)) as fh:
    db_string = json.loads(fh.read())['db_string']

engine = create_engine(db_string)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
print('conectado')


# Contiene los datos relacionados al hecho
class Hechos(Base):
    __tablename__ = 'hechos'

    id_hecho = Column(Integer(), primary_key=True)
    fecha = Column(Date())
    hora = Column(Time(timezone=True))
    calle1 = Column(String(100))
    calle2 = Column(String(100))
    altura_calle = Column(Integer())
    tipo_calle1 = Column(String(30))
    tipo_calle2 = Column(String(30))
    caracteristica_calle1 = Column(String(30))
    caracteristica_calle2 = Column(String(30))
    total_heridos = Column(Integer())
    total_obitos = Column(Integer())
    tipo_colision = Column(String(30))
    entidad_instructora = Column(String(30))
    longitud = Column(Float(), default=None)
    latitud = Column(Float(), default=None)
    observaciones = Column(Text())


# Contiene los participantes (vehículos, peatones, objetos fijos)
class Participantes(Base):
    __tablename__ = 'participantes'

    id_participante = Column(Integer(), primary_key=True)
    id_hecho = Column(Integer(), ForeignKey('hechos.id_hecho'))
    tipo_participante = Column(String(30))
    marca_participante = Column(String(50))


# Contiene las víctimas asociadas a cada hecho
class Victimas(Base):
    __tablename__ = 'victimas'

    id_victima = Column(Integer(), primary_key=True)
    id_hecho = Column(Integer(), ForeignKey('hechos.id_hecho'))
    sexo = Column(String(5))
    edad = Column(Integer())
    rol = Column(String(30))


# Importar desde la terminal para crear todas las tablas
def create_tables():
    Base.metadata.create_all(engine)


def maxima_id():
    return session.query(func.max(Hechos.id_hecho)).first()[0]

