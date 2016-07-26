
import json
from sqlalchemy import (create_engine, Column, Integer, String, Date, Time, Float,
                        Text, ForeignKey, func, CheckConstraint)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from externo.datos import *


base_dir = os.path.dirname((os.path.abspath(__file__)))

with open('config.json') as fh:
    db_string = json.loads(fh.read())['db_string']

#combo = ListasCombobox()

engine = create_engine(db_string)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()



# Contiene los datos relacionados al hecho
class Hechos(Base):
    __tablename__ = 'hechos'

    id_hecho = Column(Integer(), primary_key=True)
    fecha = Column(Date())
    hora = Column(Time())
    calle1 = Column(String(100))
    calle2 = Column(String(100))
    altura_calle = Column(Integer())
    tipo_calle1 = Column(String(30))
    tipo_calle2 = Column(String(30))
    caracteristica_calle1 = Column(String(30))
    caracteristica_calle2 = Column(String(30))
    lugar_via_publica = Column(String(30))
    tiempo = Column(String(30))
    via_dividida_por = Column(String(30))
    prioridad_regida_por = Column(String(30))
    total_heridos = Column(Integer())
    total_obitos = Column(Integer())
    entidad_instructora = Column(String(30))
    comisaria = Column(Integer())
    longitud = Column(Float(), default=None)
    latitud = Column(Float(), default=None)
    observaciones = Column(Text())
    id_dgc = Column(Integer())
    sumario = Column(Integer())


# Contiene los participantes (vehículos, peatones, objetos fijos)
class Participantes(Base):
    __tablename__ = 'participantes'

    id_participante = Column(Integer(), primary_key=True)
    id_hecho = Column(Integer(), ForeignKey('hechos.id_hecho'))
    tipo = Column(String(30))
    marca = Column(String(50))
    modelo = Column(String(70))
    dominio = Column(String(30))
    numero_participante = Column(Integer())


    CheckConstraint('numero_participante >= 0', name='check_num_part')



# Contiene las víctimas asociadas a cada hecho
class Victimas(Base):
    __tablename__ = 'victimas'

    id_victima = Column(Integer(), primary_key=True)
    id_hecho = Column(Integer(), ForeignKey('hechos.id_hecho'))
    sexo = Column(String(5))
    edad = Column(Integer())
    rol = Column(String(30))
    dni = Column(Integer())
    apellido = Column(String(50))
    nombre = Column(String(50))
    numero_participante = Column(Integer())


    CheckConstraint('numero_participante >= 0', name='check_num_part')



# Importar desde la terminal para crear todas las tablas
def create_tables():
    Base.metadata.create_all(engine)


def maxima_id():
    return session.query(func.max(Hechos.id_hecho)).first()[0]

