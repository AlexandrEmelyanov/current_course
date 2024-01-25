import requests

from django.conf import settings

from .models import CurrencyRate

URL = settings.API_URL
API_KEY = settings.API_KEY


def get_current_rate(url=URL, key=API_KEY):
    result = None
    headers = {'apikey': key}
    params = {
        'base_currency': 'USD',
        'currencies': 'RUB',
    }

    try:
        response = requests.get(url, params=params, headers=headers).json()

    except requests.exceptions.RequestException:
        result = 'error requesting'

    else:
        course = response['data']['RUB']['value']
        last_update = response['meta']['last_updated_at']
        CurrencyRate.objects.create(course=course, last_update=last_update)
        result = course

    finally:
        return result
