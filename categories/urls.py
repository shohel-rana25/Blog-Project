from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.add_categorie, name='add_categorie'),
]
