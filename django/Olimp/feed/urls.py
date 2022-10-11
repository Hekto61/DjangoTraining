from django.contrib import admin
from django.urls import path, include
from . import views 
    
urlpatterns = [
    path('', views.olimp_lists, name="olimp_lists"),
    path('new/', views.olimp_new, name="olimp_new"),
    
]
