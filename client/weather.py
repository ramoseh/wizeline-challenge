import requests


def get_gdl_wheather():
    response = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=Zapopan&appid=c2cc4793166f777bbaaca3526275b874'
    )
    data = response.json()['main']
    return data
