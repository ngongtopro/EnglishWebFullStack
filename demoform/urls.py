from django.urls import re_path as url
from demoform import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^/demoform', views.form_name_view, name='form_name'),
]