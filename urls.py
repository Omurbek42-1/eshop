from django.urls import path
from .views import DirectorListCreate, DirectorDetail, MovieListCreate, MovieDetail, ReviewListCreate, ReviewDetail

urlpatterns = [
    path('directors/', DirectorListCreate.as_view(), name='director-list'),
    path('directors/<int:pk>/', DirectorDetail.as_view(), name='director-detail'),
    path('movies/', MovieListCreate.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetail.as_view(), name='movie-detail'),
    path('reviews/', ReviewListCreate.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('movie_app.urls')),
]
