from django.urls import re_path as url
from . import views


app_name = 'coin_gas_station'


urlpatterns = [
    url(r'^$', views.index, name='index')
]