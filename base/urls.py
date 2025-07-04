from django.urls import path
from . import views

urlpatterns = [

    path('', views.Home, name="HOME"),
    path('room/<str:pk>/', views.Room, name="ROOM")
]