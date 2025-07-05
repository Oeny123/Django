from django.shortcuts import render
from django.http import HttpResponse
from .models import Room


rooms = [
    {'id': 1, 'name': 'Flask! Backend'},
    {'id': 2, 'name': 'Django! Backend'},
    {'id': 3, 'name': 'React! Fronend'}
]


# Create your views here.
def Home(request):
    home_content =  {'rooms': rooms}
    return render(request, 'base/home.html', home_content )

def Room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    room_content = {'room': room}
    return render(request, 'base/room.html', room_content )