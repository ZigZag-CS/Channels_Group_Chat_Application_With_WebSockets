from django.urls import path, include
from .views import *

app_name = "chat"

urlpatterns = [
    path('', homepageview, name='home_page'),
    path('room/', roomview, name='room_page')
]