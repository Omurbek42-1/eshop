from django.urls import path
from .views import IndexView, MyModelDetailView, MyModelCreateView, MyModelUpdateView, MyModelDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('detail/<int:pk>/', MyModelDetailView.as_view(), name='detail'),
    path('create/', MyModelCreateView.as_view(), name='create'),
    path('update/<int:pk>/', MyModelUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', MyModelDeleteView.as_view(), name='delete'),
]
