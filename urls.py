from django.urls import path
from .views import MovieListView, DirectorListView

urlpatterns = [
    path('api/v1/movies/reviews/', MovieListView.as_view(), name='movie-list'),
    path('api/v1/directors/', DirectorListView.as_view(), name='director-list'),
]
