from django.shortcuts import get_object_or_404

from django.shortcuts import render # type: ignore

from django.http import HttpResponse # type: ignore
from .models import Movie 

# This is the home view
def home(request):
    searchTerm=request.GET.get('searchMovie')
    if searchTerm:
        movies=Movie.objects.filter(title_icontains=searchTerm)
    else:
        movies=Movie.objects.all()
    return render(request, 'home.html', {'searchTerm':searchTerm, 'movies':movies})



    return render(request, "home.html", {"searchTerm":searchTerm, 'movie':movies})



#This is the about view 
#def about(request):
 #   return render(request, "about.html")

# This is the signup view.
def signup(request):
    email=request.GET.get('email')

    return render(request, "signup.html", {"email":email})


def detail(request, movie_id):
    movie=get_object_or_404(Movie, pk=movie_id)
    return render(request, 'detail.html', {'movie':movie})

def about(request):
    return render(request, 'about.html')


