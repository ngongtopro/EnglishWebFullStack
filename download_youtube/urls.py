from django.urls import re_path as url
from download_youtube import views

app_name = 'download_youtube'


urlpatterns = [
    url(r'^$', views.YoutubeDownloader.as_view(), name='dashboard'),
    # url(r'^form', views.YoutubeDownloader.youtube_form(), name='youtube_form'),
    url(r'^create', views.YoutubeDownloader.as_view(), name='create'),
    url(r'^detail/(?P<pk>\d+)', views.YoutubeDetail.as_view(), name='detail'),
    url(r'^detail/(?P<pk>\d+)/update', views.YoutubeUpdate.as_view(), name='update'),
    url(r'^detail/(?P<pk>\d+)/delete', views.YoutubeDelete.as_view(), name='delete'),
]