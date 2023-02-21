"""Defines URL patterns for the site."""
from django.urls import path
from . import views
app_name = 'sitepages'
urlpatterns = [
    #Homepage
    path('', views.index, name='index'),
]
