from django.urls import path

from .views import get_current_usd

app_name = 'currency'

urlpatterns = [
    path('', get_current_usd),
]