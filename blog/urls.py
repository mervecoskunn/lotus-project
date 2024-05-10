from django.urls import path
from . import views as blog_views

urlpatterns = [
    path('', blog_views.post_list, name='post_list'),
    path('post/<int:pk>/', blog_views.post_detail, name='post_detail'),
    path('post/new/', blog_views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', blog_views.post_edit, name='post_edit'),
    path('post/<int:pk>/post_confirm_delete/', blog_views.post_confirm_delete,
         name='post_confirm_delete'),
    path('post/<int:pk>/delete/', blog_views.post_delete, name='post_delete'),
]
