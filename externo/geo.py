import requests


def geocodificar(calle1, calle2, altura=None):
    global address
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
    if calle1 and calle2:
        address = '{}+y+{},+CABA,+AR'.format(calle1, calle2)
    elif calle1 and altura:
        address = '{}+{},+CABA,+AR'.format(altura, calle1)

    url_address = '{}{}'.format(url, address)
    result = requests.get(url_address).json()
    return result['results'][0]['geometry']['location']


#print(geocodificar("rivadavia av", 'cuzco'))