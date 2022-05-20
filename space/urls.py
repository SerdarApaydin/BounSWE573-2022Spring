from django.contrib import admin
from django.urls import path, include
from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse("Home Page")

urlpatterns = [
    path('', home , name= 'home'),
]
