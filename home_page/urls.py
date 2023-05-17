from django.urls import re_path as url
from home_page import views

app_name = 'homepage'

urlpatterns = [
    url(r'^$', views.index, name='home'),
]