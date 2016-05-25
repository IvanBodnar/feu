import requests
import csv

# Crea un csv con la lista de calles de CABA, obtenida del callejero de USIG.
# Cambiar el nombre del csv por el que se desee

calles = requests.get('http://usig.buenosaires.gov.ar/servicios/Callejero')

csv_calles = 'nuevo_csv.csv'

with open(csv_calles, 'w', newline='') as fh:
    writer = csv.DictWriter(fh, fieldnames=['calles'])
    writer.writeheader()
    for calle in calles.json():
        writer.writerow({'calles': calle[1]})
