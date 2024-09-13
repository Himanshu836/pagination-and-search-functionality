from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator

# Create your views here.


def movie_list(request):
    movie_objs=Movies.objects.all()

    movie_name = request.GET.get('movie_name')

    # search
    if movie_name != '' and movie_name is not None:
        movie_objs= movie_objs.filter(name__icontains = movie_name)


    # Pagination
    paginator = Paginator(movie_objs,3)
    page = request.GET.get('page')
    movie_objs = paginator.get_page(page)
    return render(request,'newapp/movie_list.html',{'movie_objs':movie_objs})

