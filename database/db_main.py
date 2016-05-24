from sqlalchemy import (create_engine, Column, Integer, String, Date, Time, Float,
                        ForeignKey)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('postgresql://ivan:ivan@localhost/feu')

def conectar_db(user, password, host, database, port=5432):
    user = user
    password = password
    host = host
    port = port
    database = database
    try:
        engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(user, password, host,
                                                                    port, database))
    except:
        return 'No se pudo conectar'

    return engine


class ConnectToDatabase:
    def __init__(self, user, password, host, database, port=5432):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(self.user, self.password, self.host,
                                                                         self.port, self.database))




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
    total_heridos = Column(Integer())
    total_obitos = Column(Integer())
    tipo_siniestro = Column(String(30))
    tipo_colision = Column(String(30))
    entidad_instructora = Column(String(30))
    longitud = Column(Float())
    latitud = Column(Float())


# Contiene los participantes (vehículos, peatones, objetos fijos)
class Participantes(Base):
    __tablename__ = 'participantes'

    id_hecho = Column(Integer(), ForeignKey('hechos.id_hecho'))
    id_participante = Column(String(10), primary_key=True)
    numero_participante = Column(String(5))
    tipo_participante = Column(String(30))


# Importar desde la terminal para crear todas las tablas
def create_tables():
    Base.metadata.create_all(engine)