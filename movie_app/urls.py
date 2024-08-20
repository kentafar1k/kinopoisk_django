from django.contrib import admin
from django.urls import path
from . import views

admin.site.site_header = 'Админка'

urlpatterns = [
    path('', views.show_all_movies, name='show_all_movies'),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='one-movie'),
    path('directors', views.show_directors, name='show-directors'),
    path('directors/<int:id_director>', views.one_director, name='one-director'),
    path('actors', views.ListActors.as_view(), name='show-actors'),
    path('actors/<int:pk>', views.OneActor.as_view(), name='one-actor'),
]