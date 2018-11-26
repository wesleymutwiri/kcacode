from django.conf.urls import url,include
from . import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name= 'index'),
    url(r'/about', views.about, name= 'about'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]

