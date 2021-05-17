from django.shortcuts import render

def homepageview(request):

    context = {
        "title": "This is homepage !"
    }

    return render(request,'chat/index.html', context)


def roomview(request):

    room_no = request.POST['room_no']
    name = request.POST['name']

    context = {
    'room_no': room_no,
    'name': name
    }

    return render(request, 'chat/room.html', context)