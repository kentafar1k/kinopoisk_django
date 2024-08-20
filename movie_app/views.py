from django.shortcuts import render, get_object_or_404
from .models import Movie, Director, Actor
from django.db.models import F, Sum, Max, Min, Avg, Count, Value
from django.views.generic import ListView, DetailView

def show_all_movies(request):
    movies = Movie.objects.order_by(F('year').asc(nulls_last=True), 'rating')
    agg = movies.aggregate(Sum('budget'), Max('rating'), Min('rating'))
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'agg': agg,
    })

def show_one_movie(request, slug_movie: str):
    movie = Movie.objects.get(slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })

def show_directors(request):
    directors = Director.objects.all
    return render(request, 'movie_app/directors.html', {
        'directors': directors
    })

def one_director(request, id_director: int):
    director = get_object_or_404(Director, id=id_director)
    return render(request, 'movie_app/one_director.html', {
        'director': director
    })

class ListActors(ListView):
    template_name = 'movie_app/actors.html'
    model = Actor
    context_object_name = 'actors'

# def one_actor(request, id_actor: int):
#     actor = get_object_or_404(Actor, id=id_actor)
#     return render(request, 'movie_app/one_actor.html', {
#         'actor': actor
#     })

class OneActor(DetailView):
    template_name = 'movie_app/one_actor.html'
    model = Actor
    context_object_name = 'actor'
