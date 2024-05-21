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
    path('drafts/', blog_views.draft_post_list, name='draft_post_list'),
    path('drafts/<int:pk>', blog_views.draft_post_detail, name='draft_post_detail'),
    path('drafts/<int:pk>/edit/', blog_views.draft_post_edit,
         name='draft_post_edit'),
    path('drafts/<int:pk>/delete/', blog_views.draft_post_delete,
         name='draft_post_delete'),
    path('drafts/<int:pk>/draft_post_confirm_delete/',
         blog_views.draft_post_confirm_delete, name='draft_post_confirm_delete'),

]
