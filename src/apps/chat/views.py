from django.shortcuts import render

from .models import *

def homepageview(request):

    context = {
        "title": "This is homepage !"
    }

    return render(request,'chat/index.html', context)


def roomview(request):

    room_no = request.POST['room_no']
    name = request.POST['name']

    messages = []
    for obj in ChatModel.objects.filter(room_no=room_no):
        messages.append(obj.message)

    context = {
    'room_no': room_no,
    'name': name,
    'messages': messages
    }

    return render(request, 'chat/room.html', context)