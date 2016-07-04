import csv
import os.path


# Recolecta los datos almacenados en datos_app.csv. Las constantes creadas
# pueden ser usadas en los demas módulos
class ListasCombobox:
    def __init__(self):
        base_dir = os.path.dirname((os.path.abspath(__file__)))
        csv_file = 'datos_app.csv'


        with open(csv_file, encoding='latin1') as fh:
            self.reader = csv.DictReader(fh)
            self.datos_externos = [x for x in self.reader]

    def get_list(self, field):
        return [''] + [x[field].strip() for x in self.datos_externos if x[field] is not '']

    # Devuelve string que contiene los datos para conectarse a la base de datos (usados por
    # create_engine y por sessionmaker)
    def get_engine(self):
        return self.datos_externos[0]['engine']
