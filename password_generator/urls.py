from django.contrib import admin
from django.urls import path, include
from password_generator import views

app_name = 'password_generator'

urlpatterns = [
    path('', views.home, name='home'),
    path('password/', views.password, name='password'),
]