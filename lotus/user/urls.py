from django.urls import path
from . import views

urlpatterns = [
    path('favorites/', views.favorites, name='favorites'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('remove_from_favorites/<int:id>/',
         views.remove_from_favorites, name='remove_from_favorites'),
    path('add_to_favorites/<int:id>/',
         views.add_to_favorites, name='add_to_favorites'),
]
