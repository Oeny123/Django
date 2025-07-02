from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Home(request):
    return HttpResponse('Home Page')

def Room(request):
    return HttpResponse('room')