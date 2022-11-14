
from django.http import  HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import MovieModel
from user_registration.models import ProfileModel
from django.views.generic import CreateView, DeleteView



# Create your views here.


def home(request):
     
     movies = MovieModel.objects.all()
     context = {
          'movies': movies
     }
     
     return(render(request, 'list/home.html', context=context))

     

def watched(request):
     movies = MovieModel.objects.all()
     context = {
          'movies': movies
     }
     return(render(request, 'list/watched.html', context=context))
     
#manytomany field-re megoldás ??? 
def mark_as_watched(request,id):
     if request.POST:
          movie =MovieModel.objects.get(id=id)
          print(movie)
          user = ProfileModel.objects.get(id=request.user.id)
          movie.save()
          user.save()
          user.watched_movies.add(movie)
     return HttpResponseRedirect(reverse('list_home'))


