from django.shortcuts import render
from . import form

# Create your views here.

def index(request):

    return render(request, 'demoform/index.html')


def form_name_view(request):
    form_1 = form.FormName()
    return render(request, 'demoform/form_page.html', {'form': form_1})