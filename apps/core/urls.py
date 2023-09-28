from django.contrib import admin

from django.urls import path, include
from .views import create_user, entrar, sair

urlpatterns = [
    path('create_user', create_user, name="create_user"),
    path('entrar', entrar, name="entrar"),
    path('sair', sair, name="sair"),
]
