from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def print_hello(request):
    movie_data={
        'movies': [
        {
        'tittle':'oip',
        'year':1584,
        'summary':'doog',
        'sucess': True
    },
    {'tittle':'valibhan',
        'year':1554,
        'summary':'doog',
        'sucess': False
    },
    {'tittle':'bhramayugam',
        'year':1684,
        'summary':'doog',
        'sucess': False
    },
    {
    'tittle':'premalu',
    'year':1774,
    'summary':'doog',
    'sucess': False
    }]}
    return render(request,'hello.html',movie_data)
        