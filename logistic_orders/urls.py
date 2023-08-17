from django.urls import re_path as url
from . import views
app_name = 'logistic_orders'

urlpatterns = [
    url(r'^&', views, name='index'),
]