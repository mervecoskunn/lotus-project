from django.contrib import admin
from django.urls import path
from . import views as authentication_views
from django.contrib.auth import views as auth_views

reset_view = auth_views.PasswordResetView.as_view(
    template_name="authentication/password_reset.html")

reset_done_view = auth_views.PasswordResetDoneView.as_view(
    template_name="authentication/password_reset_done.html")

reset_confirm_view = auth_views.PasswordResetConfirmView.as_view(
    template_name="authentication/password_reset_confirm.html")

reset_complete_view = auth_views.PasswordResetCompleteView.as_view(
    template_name="authentication/password_reset_complete.html")


urlpatterns = [
    path('login/', authentication_views.login, name="login"),
    path('register/', authentication_views.register, name="register"),
    path('logout/', authentication_views.logout, name="logout"),
    path('activate/(<uidb64>/<token>/',
         authentication_views.activate, name='activate'),
    path('password-reset/', reset_view, name="password_reset"),
    path('password-reset-done/', reset_done_view, name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',
         reset_confirm_view, name="password_reset_confirm"),
    path('password-reset-complete/', reset_complete_view,
         name="password_reset_complete"),
]
