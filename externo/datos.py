import csv
import os.path

# Recolecta los datos almacenados en datos_app.csv. Las constantes creadas
# pueden ser usadas en los demas módulos

BASE_DIR = os.path.dirname((os.path.abspath(__file__)))

csv_file = '{}/datos_app.csv'.format(BASE_DIR)

with open(csv_file) as fh:
    reader = csv.DictReader(fh)
    datos_externos = [x for x in reader]

# String que contiene los datos para conectarse a la base de datos (usados por
# create_engine y por sessionmaker)
ENGINE_CONNECTION_STRING = datos_externos[0]['engine']

# Lista con todas las calles, obtenidas del callejero de la USIG (ver callejero.py)
CALLES_LIST = [x['calles'] for x in datos_externos]

TIPO_ARTERIA_LIST = [''] + [x['tipo_arteria'] for x in datos_externos if x['tipo_arteria'] is not '']

TIPO_SINIESTRO_LIST = [''] + [x['tipo_siniestro'] for x in datos_externos if x['tipo_siniestro'] is not '']

TIPO_COLISION_LIST = [''] + [x['tipo_colision'] for x in datos_externos if x['tipo_colision'] is not '']

ENTIDAD_INSTRUCTORA_LIST = [''] + [x['entidad_instructora'] for x in datos_externos if x['entidad_instructora'] is not '']