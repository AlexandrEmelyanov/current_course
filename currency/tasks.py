import logging

import requests
from celery import shared_task
from django.conf import settings

from .models import CurrencyRate

URL = settings.API_URL
API_KEY = settings.API_KEY

logger = logging.getLogger(__name__)


@shared_task(bind=True)
def get_current_rate(self, url=URL, key=API_KEY) -> None:
    """
    Sending a request to the external Currency API.

    If the response is successful, a record about the request is created in the database.
    If an error occurs during the request, the request will be repeated after 15 seconds -> self.retry().

    The task is executed once every 15 seconds (CELERY_BEAT_SCHEDULE в settings.py).
    """
    headers = {'apikey': key}
    params = {
        'base_currency': 'USD',
        'currencies': 'RUB',
    }

    try:
        response = requests.get(url, params=params, headers=headers).json()

    except requests.exceptions.RequestException as e:
        logger.error('An error occurred while executing a request to the currency rate API')
        raise self.retry(exc=e, countdown=15)

    else:
        course = response['data']['RUB']['value']
        last_update = response['meta']['last_updated_at']
        last_request = CurrencyRate.objects.create(course=course, last_update=last_update)
        logger.info(
            f'The request was executed successfully. '
            f'The data about the last request №{last_request.id} is saved in the database.'
        )
