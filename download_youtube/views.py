from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.

class YoutubeDownloader(View):

    def __int__(self):
        pass

    def get(self, request):
        return HttpResponse('Hello')
    # def as_view(self, request):
    #     return render(request, 'download_youtube/index.html')
