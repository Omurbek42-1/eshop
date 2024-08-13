from django.urls import path
from .views import DirectorListCreate, DirectorRetrieve, MovieListCreate, MovieRetrieve, ReviewListCreate, ReviewRetrieve

urlpatterns = [
    path('directors/', DirectorListCreate.as_view(), name='director-list'),
    path('directors/<int:pk>/', DirectorRetrieve.as_view(), name='director-detail'),
    path('movies/', MovieListCreate.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieRetrieve.as_view(), name='movie-detail'),
    path('reviews/', ReviewListCreate.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewRetrieve.as_view(), name='review-detail'),
]
