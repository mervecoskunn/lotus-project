"""
URL configuration for lotus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views as lotus_views
from django.conf.urls import handler500
from django.views.generic.base import TemplateView, RedirectView

handler500 = 'lotus.views.custom_500'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lotus_views.home, name="home"),
    path("auth/", include('authentication.urls')),
    path('contact/', lotus_views.contact, name="contact"),
    path('shopping/', include('shopping.urls')),
    path('user/', include('user.urls')),
    path('order/', include('order.urls')),
    path('privacy-policy/', lotus_views.privacy_policy, name="privacy_policy"),
    path('faq/', lotus_views.faq, name="faq"),
    path('blog/', include('blog.urls')),
    path("subscription", lotus_views.subscription, name="subscription"),
    # robots.txt path below
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt",
                             content_type="text/plain"),
    ),
    path('sitemap.xml', TemplateView.as_view(
        template_name='sitemap.xml', content_type='text/xml')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
