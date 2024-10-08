from django.contrib import admin
from django.urls import path, include

from petstagram.photos import views

urlpatterns = [
    path('add/', views.add_photo, name='add-photo'),
    path('', include([
        path('<int:pk>/', views.photo_details, name='photo-details'),
        path('<int:pk>/edit/', views.photo_edit, name='photo-edit'),
        path('<int:pk>/delete', views.delete_photo, name='photo-delete'),
    ]
    )),
]
