from django.urls import re_path as url
from download_youtube import views

app_name = 'download_youtube'


urlpatterns = [
    url(r'^$', views.YoutubeDownloader.as_view(), name='youtube_downloader'),
    # url(r'^form', views.YoutubeDownloader.youtube_form(), name='youtube_form'),
]