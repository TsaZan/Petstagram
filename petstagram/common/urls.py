from django.contrib import admin
from django.urls import path, include

from petstagram.common import views

urlpatterns = [
    path('', views.index, name='index'),
]