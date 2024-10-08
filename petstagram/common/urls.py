from django.contrib import admin
from django.urls import path, include

from petstagram.common import views

urlpatterns = [
    path('', views.index, name='index'),
    path('like/<int:photo_id>/', views.like_functionality, name='like'),
    path('share/<int:photo_id>/', views.share_functionality, name='share'),
    path('<int:photo_id>/', views.add_comment, name='add-comment'),

]