from products import views
from django.urls import path

urlpatterns = [
    path('', views.product_list_create_api_view),
    path('<int:id./', views.product_detail_api_view),

]