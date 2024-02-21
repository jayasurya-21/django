from django.shortcuts import render
from . models import MovieInfo
from . models import MovieForm


# Create your views here.
def create(request):
    frm=MovieForm()
    if request.POST:
        tittle=request.POST.get('tittle')
        year=request.POST.get('year')
        description=request.POST.get('description')
        movie_obj=MovieInfo(tittle=tittle,year=year,description=description)
        movie_obj.save()
        
    return render(request,'create.html',{'frm':frm})

def list(request):
    movie_set=MovieInfo.objects.all       
    print(movie_set) 
    return render(request,'list.html',{'movies':movie_set})

def edit(request):
    return render(request,'edit.html')



