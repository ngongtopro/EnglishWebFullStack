from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View, generic

from first_app.models import Hall


# Create your views here.

# CRUD
class YoutubeDownloader(generic.CreateView):
    model = Hall
    fields = ['title']
    template_name = 'download_youtube/create.html'
    success_url = reverse_lazy('download_youtube:youtube_downloader')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(YoutubeDownloader, self).form_valid(form)
        return redirect('download_youtube:youtube_downloader')


class YoutubeDetail(generic.DetailView):
    model = Hall

    template_name = 'download_youtube/detail.html'


class YoutubeUpdate(generic.UpdateView):
    model = Hall
    template_name = 'youtube_download/update.html'
    fields = ['title']
    success_url = reverse_lazy('download_youtube:dashboard')


class YoutubeDelete(generic.DeleteView):
    model = Hall
    template_name = 'youtube_download/delete.html'
    fields = 'title'
    success_url = reverse_lazy('download_youtube:dashboard')
