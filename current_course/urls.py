from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get-current-usd/', include('currency.urls', namespace='currency')),
]
