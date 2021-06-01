from django.shortcuts import render
from django.urls import path

from . import views

app_name = "website"
href = "{% url 'website:home' %}"

urlpatterns = [
    path('home', views.home_page_view, name='home')
]
