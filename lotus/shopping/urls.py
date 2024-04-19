from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping, name='shopping'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
]
