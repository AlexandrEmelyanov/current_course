import time

from django.http import JsonResponse

from .utils import get_current_rate
from .models import CurrencyRate


def get_current_usd(request):
    current_usd = get_current_rate()
    last_10_requests = CurrencyRate.objects.order_by('-created')[:10]
    data = list(last_10_requests.values())

    result = {
        'current_usd': current_usd,
        'last_10_requests': data
    }

    return JsonResponse(result)
