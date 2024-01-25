from django.http import JsonResponse

from .models import CurrencyRate
from .tasks import get_current_rate


def get_current_usd(request):
    """
    This function retrieves the current USD exchange rate and
    the 10 most recent requests for the exchange rate.

    If this is the first request it is called directly: get_current_rate.delay().

    Returns: JSON raw data.
    """
    last_request = CurrencyRate.objects.filter().first()

    if not last_request:
        get_current_rate.delay()

    current_usd = CurrencyRate.objects.last().course
    last_10_requests = CurrencyRate.objects.order_by('-created')[:10]
    data = list(last_10_requests.values())

    result = {
        'current_usd': current_usd,
        'last_10_requests': data
    }

    return JsonResponse(result)
