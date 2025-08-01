"""EnglishWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home_page import views
from django.urls import re_path as url
from django.urls import include

urlpatterns = [
    url(r'^', include('home_page.urls')),
    url(r'^first_app/', include('first_app.urls')),
    url(r'^demoform/', include('demoform.urls')),
    url(r'^download_youtube/', include('download_youtube.urls')),
    url(r'^restapi/', include('rest_api.urls')),
    url(r'^new_polls/', include('new_polls.urls')),
    url(r'^chatbot/', include('chatbot.urls')),
    path('admin/', admin.site.urls),
]
