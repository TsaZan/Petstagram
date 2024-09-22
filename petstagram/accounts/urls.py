from django.contrib import admin
from django.urls import path, include

from petstagram.accounts import views

urlpatterns = [
    path('register/', views.register, name='register-page'),
    path('login/', views.login, name='login-page'),
    path('profile/<int:pk>/', include([
        path('', views.profile, name='profile-details'),
        path('edit/', views.edit_profile, name='edit-profile'),
        path('delete/', views.delete_profile, name='delete-profile'),
    ]
    )),

]