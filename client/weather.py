import requests
import config

cfg = config.Settings()


def get_gdl_wheather():
    response = requests.get(
        'http://api.openweathermap.org/data/2.5/weather',
        params={'q': 'Zapopan', 'appid': cfg.api_key}
    )
    data = response.json()['main']
    return data
