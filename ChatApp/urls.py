from django.urls import path

from .views import *

urlpatterns = [
    path("", createRoom, name="create-room"),
    path("<str:room_name>/<str:username>/", messageView, name="room"),

]