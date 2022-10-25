from django.contrib import admin
from django.urls import path, include
from . import views 
    
urlpatterns = [
    path('', views.olimp_lists, name="olimp_lists"),
    path('new/', views.olimp_new, name="olimp_new"),
    path('olimp/<int:pk>/', views.olimp_detail, name="olimp_detail"),
    path('user/<int:pk>/', views.user_detail, name="user_detail"),
    path('newUser/', views.user_new, name="user_new"),
    
]
