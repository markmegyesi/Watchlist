
from django.http import  HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import MovieModel
from django.views.generic import CreateView, DeleteView

# Create your views here.


def home(request):
     
     movies = MovieModel.objects.all()
     context = {
          'movies': movies
     }
     
     return(render(request, 'blog/home.html', context=context))

     

def watched(request):
     movies = MovieModel.objects.all()
     context = {
          'movies': movies
     }
     return(render(request, 'blog/watched.html', context=context))
     

def mark_as_watched(request,id):
     if request.POST:
          
          movie = MovieModel.objects.get(id=id)
          movie.is_watched = 'yes'
          movie.save()
     return HttpResponseRedirect(reverse('blog_home'))
