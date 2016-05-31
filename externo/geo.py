import requests


def geocodificar(calle1, calle2):
    GOOGLE_KEY = 'AIzaSyBKUvzwTGE65RwwhrXa67pFfF3PkvynMSY'
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
    address = '{}+y+{},+CABA,+AR'.format(calle1, calle2)
    url_address = '{}{}'.format(url, address)
    result = requests.get(url_address).json()
    return result['results'][0]['geometry']['location']


geocodificar('callao', 'corrientes')