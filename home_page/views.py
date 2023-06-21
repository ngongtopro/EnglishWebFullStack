from django.shortcuts import render

# Create your views here.

def index(request):
    data = {}
    links = {
        'homepage:home': {
            'class': '',
            'content': 'Home',
        }
    }
    data.update({'links': links})
    return render(request, 'home_page/index.html', data)